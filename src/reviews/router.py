from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import ValidationError

from src.database import get_async_session
from src.auth.base_config import current_user
from src.books.models import Books
from src.reviews.models import Reviews
from src.reviews.schemas import ReviewCreate


router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.post(path="/{book_title}/create")
async def create_review(
    book_title: str,
    title: str = Form(...),
    text: str = Form(...),
    rating: int = Form(...),
    curr_user=Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    try:
        review_data = ReviewCreate(title=title, text=text, rating=rating)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    
    query = select(Books).where(Books.title == book_title)
    result = await session.execute(query)
    book = result.scalars().first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    existing_review_query = select(Reviews).where(
        Reviews.book == book.id, Reviews.reviewer == curr_user.id
    )
    existing_review_result = await session.execute(existing_review_query)
    existing_review = existing_review_result.scalars().first()

    if existing_review:
        raise HTTPException(status_code=400, detail="User has already reviewed this book")

    new_review = Reviews(
        book=book.id,
        reviewer=curr_user.id,
        title=review_data.title,
        text=review_data.text,
        rating=review_data.rating
    )
    session.add(new_review)
    await session.commit()
    await session.refresh(new_review)

    return RedirectResponse(url=f"/books/{book_title}", status_code=303)