from fastapi import APIRouter, Depends, Form, Request
from starlette.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from src.queries import (
    get_book_by_title,
    get_related_books_by_title,
    get_all_book_reviews
)
from src.database import get_async_session
from src.auth.base_config import current_user, current_user_optional
from src.books.models import Books, Reviews
from src.books.schemas import GetAllBooks


router = APIRouter(prefix="/books", tags=["Books"])

templates = Jinja2Templates(directory="templates/")


@router.get(path="", response_model=List[GetAllBooks])
async def get_all_books(
    request: Request,
    current_user=Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Books.id, Books.title, Books.image)
    result = await session.execute(query)
    books = result.fetchall()
    books_rows = [{"id": book[0], "title": book[1], "image": book[2]} for book in books]
    
    return templates.TemplateResponse(
        "pages/books.html", {
            "request": request,
            "books": books_rows,
            "current_user": current_user
        }
    ) 


@router.get(path="/{book_name}")
async def get_book(
    book_name: str,
    session: AsyncSession = Depends(get_async_session)
):
    book = await get_book_by_title(
        title=book_name,
        session=session
    )
    return book


@router.get(path="/{book_name}")
async def get_related_books(
    book_name: str,
    session: AsyncSession = Depends(get_async_session)
):
    related_books = await get_related_books_by_title(
        title=book_name,
        session=session
    )
    return related_books


@router.get(path="/{book_name}")
async def get_book_reviews(
    book_name: str,
    session: AsyncSession = Depends(get_async_session)
):
    book_reviews = await get_all_book_reviews(
        title=book_name,
        session=session
    )
    return book_reviews


@router.post(path="/{book_name}/review")
async def create_review(
    book_name: str,
    title: str = Form(...),
    text: str = Form(...),
    rating: int = Form(...),
    session: AsyncSession = Depends(get_async_session),
    curr_user=Depends(current_user)
):
    query = select(Books).where(Books.title == book_name)
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

    return {"message": "Review created successfully", "review_id": new_review.id}
