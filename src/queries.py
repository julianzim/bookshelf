from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.models import Books
from src.reviews.models import Reviews
from src.database import async_engine, Base


async def reset_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    # yield
    print('База данных сброшена')


async def get_book_by_title(
    title: str,
    session: AsyncSession
):
    query = select(Books).where(Books.title == title)
    result = await session.execute(query)
    book = result.scalars().one()
    return book


async def get_related_books_by_title(
    title: str,
    session: AsyncSession
):
    query = select(Books)
    result = await session.execute(query)
    books = result.scalars().all()
    return books


async def get_all_book_reviews(
    title: str,
    session: AsyncSession
):
    query = select(Reviews)
    result = await session.execute(query)
    reviews = result.scalars().all()

    return reviews
