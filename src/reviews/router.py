"""reviews/router.py"""

from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import ValidationError

from src.config import app_config
from src.queries import get_review_by_id
from src.database import get_async_session
from src.auth.base_config import current_user
from src.auth.models import User
from src.books.models import Books
from src.reviews.models import Reviews
from src.reviews.schemas import ReviewCreate
from src.tasks.email_tasks import send_email_task
from misc.utils import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix = "/reviews", tags = ["Reviews"])

templates = Jinja2Templates(directory="templates/")


@router.post(
    path="/{book_title}/create",
    response_class=HTMLResponse
)
async def create_review(
    request: Request,
    book_title: str,
    title: str = Form(...),
    text: str = Form(...),
    rating: int = Form(...),
    curr_user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Submit a new review for a specific book.

    This endpoint allows an authenticated user to create a review for a given book by its title.
    The review is saved in the database and sent to moderators for approval before it becomes 
    publicly visible.

    ---
    **Path Parameters**:
    - **book_title** (str): The title of the book to review. Used to find the book in the database.

    **Form Data**:
    - **title** (str): The title of the review.
    - **text** (str): The content/body of the review.
    - **rating** (int): The numerical rating given to the book (e.g., from 1 to 5).

    **Dependencies**:
    - **curr_user** (User): The currently authenticated user. Retrieved via dependency injection.
    - **session** (AsyncSession): The SQLAlchemy asynchronous database session.

    ---
    **Behavior**:
    1. Validates the incoming review data using `ReviewCreate`.
    2. Checks if the book with the given title exists. Returns 404 if not found.
    3. Checks if the user has already submitted a published review for this book. Returns 400 if so.
    4. Creates and stores a new review with `approved=False`.
    5. Sends an email to moderators with a link to the moderation page.
    6. Renders a feedback page notifying the user that their review is pending moderation.

    ---
    **Returns**:
    - An HTML response (`feedback.html`) confirming that the review has been submitted 
    for moderation.

    ---
    **Raises**:
    - **HTTPException 422**: If review form validation fails.
    - **HTTPException 404**: If the specified book is not found.
    - **HTTPException 400**: If the user has already reviewed the book.

    ---
    **Side Effects**:
    - Sends an email to the moderators.
    - Logs the review creation and notification process.
    """
    logger.debug('%s requests to add a new review', curr_user)

    try:
        review_data = ReviewCreate(title=title, text=text, rating=rating)
    except ValidationError as e:
        logger.error("%s", e.errors())
        raise HTTPException(status_code=422, detail=e.errors()) from e

    query = select(Books).where(Books.title == book_title)
    result = await session.execute(query)
    book = result.scalars().first()

    if not book:
        logger.error("Book %s not found", book_title)
        raise HTTPException(status_code=404, detail="Book not found")

    existing_review_query = select(Reviews).where(
        Reviews.book_id == book.id, Reviews.user_id == curr_user.id, Reviews.published
    )
    existing_review_result = await session.execute(existing_review_query)
    existing_review = existing_review_result.scalars().first()

    if existing_review is not None:
        logger.error("%s has already reviewed this book", curr_user)
        raise HTTPException(status_code = 400, detail = "User has already reviewed this book")

    new_review = Reviews(
        book_id=book.id,
        user_id=curr_user.id,
        title=review_data.title,
        text=review_data.text,
        rating=review_data.rating,
        approved=False
    )
    session.add(new_review)
    await session.commit()
    await session.refresh(new_review)

    logger.info(
        "New review %s was created by %s at %s",
        new_review.id, curr_user, new_review.created_at
    )

    subject = f"Moderation required for review of \"{book.title}\""
    html = templates.get_template("mails/review_moderation_request.html").render(
        {
            "book_title": book.title,
            "review": new_review,
            "user": curr_user,
            "moderation_url": (
                f"https://{app_config.APP_DOMAIN}/reviews/{book.title}/moderation/{new_review.id}"
            )
        }
    )
    email_result = send_email_task.delay(
        subject=subject, body=html, recipients=app_config.APP_MODERATORS, subtype="html"
    )

    logger.info(
        "New review %s sent for moderation to %s. Result: %s",
        new_review.id, app_config.APP_MODERATORS, email_result
    )

    feedback_content = f"Your review for book \"{book_title}\" has been sent for moderation"

    return templates.TemplateResponse(
        request=request,
        name="pages/feedback.html",
        context={"content": feedback_content}
    )


@router.get(
    path="/{book_title}/moderation/{review_id}",
    response_class=HTMLResponse
)
async def get_review_moderation(
    request: Request,
    book_title: str,
    review_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Retrieve the moderation page for a specific review.

    This endpoint is used to display the moderation interface for a particular review of a book.
    It retrieves the review details and renders an HTML template where a moderator can 
    approve or reject the review.

    ---
    **Path Parameters**:
    - **book_title** (str): The title of the book associated with the review (used for display).
    - **review_id** (int): The unique identifier of the review to be moderated.

    **Dependencies**:
    - **session** (AsyncSession): Asynchronous database session injected via dependency.

    ---
    **Behavior**:
    1. Retrieves the review with the given `review_id` from the database.
    2. Passes the review data, the book title, and the user who submitted the review 
    into the HTML context.
    3. Renders the `review_moderation.html` template.

    ---
    **Returns**:
    - An HTML response containing the moderation interface for the review.

    ---
    **Raises**:
    - **HTTPException 404**: If the review is not found (expected to be raised 
    inside `get_review_by_id`).

    ---
    **Side Effects**:
    - None. This is a read-only operation.
    """
    review = await get_review_by_id(review_id=review_id, session=session)

    return templates.TemplateResponse(
        request=request,
        name="pages/review_moderation.html",
        context={
            "review": review,
            "book_title": book_title,
            "user": review.user
        }
    )


@router.patch(
    path="/{book_title}/moderation/{review_id}/approve",
    response_class=HTMLResponse
)
async def approve_review(
    request: Request,
    book_title: str,
    review_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Approve a user-submitted book review.

    This endpoint is used by moderators to approve a specific review for a book. 
    Once approved, the review becomes publicly visible and the user is notified via email.

    ---
    **Path Parameters**:
    - **book_title** (str): The title of the book associated with the review 
    (used for display/logging purposes).
    - **review_id** (int): The unique identifier of the review to be approved.

    **Dependencies**:
    - **session** (AsyncSession): Asynchronous database session injected via dependency.

    ---
    **Behavior**:
    1. Retrieves the review using the provided `review_id`.
    2. Sets review attributes:
       - `approved = True`
       - `rejection_reason = None`
       - `moderated = True`
       - `published = True`
    3. Commits the changes to the database.
    4. Sends an email notification to the review's author indicating that their review was approved.
    5. Logs the action and returns an HTML feedback page confirming the operation.

    ---
    **Returns**:
    - An HTML response (`feedback.html`) confirming successful approval of the review.

    ---
    **Raises**:
    - **HTTPException 404**: If the review is not found (this is expected to be handled 
    inside `get_review_by_id`).

    ---
    **Side Effects**:
    - Modifies the review record in the database.
    - Sends an approval email to the review's author.
    - Writes logs related to moderation approval and notification.
    """
    review = await get_review_by_id(review_id=review_id, session=session)
    review.approved = True
    review.rejection_reason = None
    review.moderated = True
    review.published = True
    await session.commit()

    feedback_content = f"Review {review.id} for book \"{book_title}\" was approved successfully"
    logger.info(feedback_content)

    subject = "Your Review Has Been Approved!"
    html = (
        templates
        .get_template("mails/review_moderation_feedback_approved.html")
        .render(
            {
                "book_title": book_title,
                "review": review,
            }
        )
    )
    email_result = send_email_task.delay(
        subject=subject,
        body=html,
        recipients=[review.user.email],
        subtype="html"
    )

    logger.info(
        "Feedback on review (id=%s) moderation has been sent to user (%s) via email. Result: %s",
        review.id, review.user.email, email_result
    )

    return templates.TemplateResponse(
        request=request,
        name="pages/feedback.html",
        context={"content": feedback_content}
    )


@router.patch(
    path="/{book_title}/moderation/{review_id}/reject",
    response_class=HTMLResponse
)
async def reject_review(
    request: Request,
    book_title: str,
    review_id: int,
    reason: str = Form(...),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Reject a user-submitted book review.

    This endpoint is used by moderators to reject a specific review for a book. 
    The moderator must provide a reason for rejection,
    which will be saved in the database and communicated to the user via email.

    ---
    **Path Parameters**:
    - **book_title** (str): The title of the book associated with the review 
    (used for logging and display).
    - **review_id** (int): The unique identifier of the review to reject.

    **Form Data**:
    - **reason** (str): The explanation for why the review is being rejected.

    **Dependencies**:
    - **session** (AsyncSession): Asynchronous SQLAlchemy session injected via dependency.

    ---
    **Behavior**:
    1. Retrieves the review with the specified `review_id`.
    2. Sets the review's `rejection_reason` to the provided reason and 
    marks it as `moderated = True`.
    3. Commits the changes to the database.
    4. Sends an email to the user informing them of the rejection and the reason.
    5. Logs the action and renders an HTML page confirming the rejection.

    ---
    **Returns**:
    - An HTML response (`feedback.html`) confirming that the review has been rejected and 
    showing the reason.

    ---
    **Raises**:
    - **HTTPException 404**: If the review is not found (expected to be raised 
    inside `get_review_by_id`).

    ---
    **Side Effects**:
    - Updates the review record in the database.
    - Sends an email notification to the review's author.
    - Logs the moderation rejection and email dispatch.
    """
    review = await get_review_by_id(review_id=review_id, session=session)
    review.rejection_reason = reason
    review.moderated = True
    await session.commit()

    feedback_content = (
        f"Review {review.id} for book \"{book_title}\" was rejected successfully. "
        f"Reason: {reason}"
    )
    logger.info(feedback_content)

    subject = "Your Review Has Been Rejected"
    html = (
        templates
        .get_template("mails/review_moderation_feedback_rejected.html")
        .render(
            {
                "book_title": book_title,
                "review": review,
            }
        )
    )
    email_result = send_email_task.delay(
        subject=subject, body=html, recipients=[review.user.email], subtype="html"
    )

    logger.info(
        "Feedback on review (id=%s) moderation has been sent to user (%s) via email. Result: %s",
        review.id, review.user.email, email_result
    )

    return templates.TemplateResponse(
        request=request,
        name="pages/feedback.html",
        context={"content": feedback_content}
    )
