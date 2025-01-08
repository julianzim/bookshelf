from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.base_config import current_user
from src.books.models import Books
from src.reviews.models import Reviews


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
    query = select(Books).where(Books.title == book_title)
    result = await session.execute(query)
    book = result.scalars().one()

    new_review = Reviews(
        book=book.id,
        reviewer=curr_user.id,
        title=title,
        text=text,
        rating=rating
    )
    session.add(new_review)
    await session.commit()
    await session.refresh(new_review)

    return RedirectResponse(url=f"/books/{book_title}", status_code=303)