from typing import List

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import (
    get_book_by_title,
    get_related_books_by_title,
    get_all_book_reviews
)
from src.database import get_async_session
from src.auth.base_config import current_user_optional
from src.books.models import Books
from src.books.schemas import GetAllBooks
from misc.utils import get_reviews_statistics


router = APIRouter(prefix="/books", tags=["Books"])

templates = Jinja2Templates(directory="templates/")


@router.get(path="")
async def get_all_books(
    request: Request,
    current_user=Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Books.id, Books.title, Books.image)
    result = await session.execute(query)
    books = result.fetchall()
    books_rows = [
        {
            "id": book[0],
            "title": book[1],
            "image": book[2]
        } for book in books
    ]
    
    return templates.TemplateResponse(
        "pages/books.html", {
            "request": request,
            "books": books_rows,
            "current_user": current_user
        }
    ) 


@router.get(path="/{book_title}")
async def get_book_details(
    book_title: str,
    request: Request,
    current_user=Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    book = await get_book_by_title(
        title=book_title,
        session=session
    )
    related_books = await get_related_books_by_title(
        title=book_title,
        session=session
    )
    book_reviews = await get_all_book_reviews(
        title=book_title,
        session=session
    )
    book_reviews_stats = await get_reviews_statistics(reviews=book_reviews)
    
    return templates.TemplateResponse(
        "pages/book_details.html",
        {
            "request": request,
            "book": book,
            "related_books": related_books,
            "current_user": current_user,
            "book_reviews": book_reviews,
            "book_reviews_stats": book_reviews_stats
        }
    )
