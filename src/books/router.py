from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from src.database import get_async_session
from src.books.models import Books
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
