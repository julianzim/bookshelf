from sqlalchemy import select, join, desc
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.books.models import Books
from src.reviews.models import Reviews
from src.articles.models import Articles
from src.database import async_engine, Base


async def reset_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    # yield
    print('База данных сброшена')


async def get_active_books(
    session: AsyncSession
):
    query = (
        select(Books.id, Books.title, Books.image)
        .where(Books.active == True)
        .order_by(Books.id)     # после деплоя сделать сортировку по pub_date
    )
    result = await session.execute(query)

    return result.fetchall()


async def get_book_by_title(
    title: str,
    session: AsyncSession
):
    query = (
        select(Books)
        .where(
            Books.title == title,
            Books.active == True
        )
    )
    result = await session.execute(query)

    return result.scalars().first()


async def get_related_books_by_title(
    title: str,
    session: AsyncSession
):
    query = (
        select(Books)
        .where(
            Books.title != title,
            Books.active == True
        )
        .order_by(Books.id)     # после деплоя сделать сортировку по pub_date
    )
    result = await session.execute(query)

    return result.scalars().all()


async def get_all_book_reviews(
    title: str,
    session: AsyncSession
):
    query = (
        select(
            User.username,
            Reviews.title,
            Reviews.text,
            Reviews.rating,
            Reviews.created_at
        )
        .select_from(
            join(Reviews, Books, Reviews.book_id == Books.id)
            .join(User, Reviews.user_id == User.id)
        )
        .where(Books.title == title)
        .order_by(desc(Reviews.created_at))
    )
    result = await session.execute(query)

    return result.fetchall()


async def get_article_by_id(
    id: int,
    session: AsyncSession
):
    query = select(Articles).where(Articles.id == id)
    result = await session.execute(query)
    
    return result.scalars().first()
