from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse, Response

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Optional


from src.auth.base_config import current_user
from src.database import get_async_session
from src.books.models import Books, Reviews
from src.books.schemas import GetAllBooks

router = APIRouter(prefix="/books", tags=["Books"])


@router.get(path="", response_model=List[GetAllBooks])
async def get_all_books(session: AsyncSession = Depends(get_async_session)):
    query = select(Books)
    result = await session.execute(query)
    books = result.scalars().all()
    return books


@router.get(path="/{book_name}")
async def get_book(book_name: str, session: AsyncSession = Depends(get_async_session)):
    # book_name_split = " ".join(book_name.split("_"))
    query = select(Books).where(Books.title == book_name)
    result = await session.execute(query)
    book = result.scalars().one()
    return book


@router.get(path="/{book_name}")
async def get_related_books(book_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Books)
    result = await session.execute(query)
    books = result.scalars().all()
    return books


@router.post(path="/{book_name}/review")
async def create_review(
    book_name: str,
    title: str = Form(...),
    description: str = Form(...),
    rating: int = Form(...),
    session: AsyncSession = Depends(get_async_session),
    curr_user=Depends(current_user),
):

    query = select(Books).where(Books.title == book_name)
    result = await session.execute(query)
    book = result.scalars().one()

    new_review = Reviews(
        book=book.id,
        reviewer=curr_user.id,
        title=title,
        description=description,
        rating=rating
    )
    session.add(new_review)
    await session.commit()
    await session.refresh(new_review)

    return {"message": "Review created successfully", "review_id": new_review.id}
