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
from misc.utils import get_logger, send_email


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
        Reviews.book_id == book.id, Reviews.user_id == curr_user.id, Reviews.published is True
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
    await send_email(subject=subject, emails=app_config.APP_MODERATORS, body=html, subtype="html")

    logger.info(
        "New review %s sent for moderation to %s",
        new_review.id, app_config.APP_MODERATORS
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
    await send_email(subject=subject, emails=[review.user.email], body=html, subtype="html")

    logger.info(
        "Feedback on review (id=%s) moderation has been sent to user (%s) via email",
        review.id, review.user.email
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
    await send_email(subject=subject, emails=[review.user.email], body=html, subtype="html")

    logger.info(
        "Feedback on review (id=%s) moderation has been sent to user (%s) via email",
        review.id, review.user.email
    )

    return templates.TemplateResponse(
        request=request,
        name="pages/feedback.html",
        context={"content": feedback_content}
    )
