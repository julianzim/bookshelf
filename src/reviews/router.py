from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Form, Query, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi_mail import FastMail, MessageSchema

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import ValidationError

from src.config import app_config, mail_conf
from src.queries import get_review_by_id
from src.database import get_async_session
from src.auth.base_config import current_user
from src.auth.models import User
from src.books.models import Books
from src.reviews.models import Reviews
from src.reviews.schemas import ReviewCreate
from misc.utils import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix = "/reviews", tags = ["Reviews"])

templates = Jinja2Templates(directory="templates/")


@router.post(path="/{book_title}/create")
async def create_review(
    book_title: str,
    title: str = Form(...),
    text: str = Form(...),
    rating: int = Form(...),
    curr_user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    logger.debug(f'{curr_user} requests to add a new review')

    try:
        review_data = ReviewCreate(title=title, text=text, rating=rating)
    except ValidationError as e:
        logger.error(f"{e.errors()}")
        raise HTTPException(status_code=422, detail=e.errors())
    
    query = select(Books).where(Books.title == book_title)
    result = await session.execute(query)
    book = result.scalars().first()

    if not book:
        logger.error(f"Book {book_title} not found")
        raise HTTPException(status_code=404, detail="Book not found")
    
    existing_review_query = select(Reviews).where(
        Reviews.book_id == book.id, Reviews.user_id == curr_user.id
    )
    existing_review_result = await session.execute(existing_review_query)
    existing_review = existing_review_result.scalars().first()

    if existing_review is not None:
        logger.error(f"{curr_user} has already reviewed this book")
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

    logger.info(f"New review {new_review.id} was created by {curr_user} at {new_review.created_at}")

    # TODO: Sendind for moderation
    subject = f"Moderation required for review of \"{book.title}\""
    html = templates.get_template("mails/review_moderation_request.html").render(
        {
            "book_title": book.title,
            "review": new_review,
            "user": curr_user,
            "approve_url": f"http://{app_config.APP_DOMAIN}/reviews/{book.title}/approve?review_id={new_review.id}", # TODO: HTTPS
            "reject_url": f"http://{app_config.APP_DOMAIN}/reviews/{book.title}/reject?review_id={new_review.id}", # TODO: HTTPS
            "year": datetime.now(timezone.utc).year
        }
    )
    message = MessageSchema(
        subject=subject,
        recipients=app_config.APP_MODERATORS,  
        body=html,
        subtype="html"
    )
    fm = FastMail(mail_conf)
    await fm.send_message(message)

    logger.info(f"New review {new_review.id} sent for moderation to {app_config.APP_MODERATORS}")

    return RedirectResponse(url=f"/books/{book_title}", status_code=303)


@router.patch(path="/{book_title}/approve")
async def approve_review(
    book_title: str,
    review_id: int = Query(...),
    session: AsyncSession = Depends(get_async_session)
):
    review = await get_review_by_id(
        review_id=review_id,
        session=session
    )
    review.approved = True
    await session.commit()

    logger.info(f"Review {review.id} for book \"{book_title}\" was approved")

    return {"detail": "Review approved"}


@router.post(path="/{book_title}/reject")
async def reject_review(
    book_title: str,
    review_id: int = Query(...),
    reason: str = Form(...),
    session: AsyncSession = Depends(get_async_session)
):
    '''
    This endpoint is called only from the moderation HTML form sent via email.
    It uses the POST method due to HTML limitations, but internally performs a PATCH-like update operation.
    '''
    review = await get_review_by_id(
        review_id=review_id,
        session=session
    )
    review.approved = False
    review.rejection_reason = reason
    await session.commit()

    logger.info(f"Review {review.id} for book '{book_title}' was rejected. Reason: {reason}")

    return {"details": "Review rejected"}
