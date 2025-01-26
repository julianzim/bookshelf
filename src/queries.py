from sqlalchemy import select, join, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.books.models import Books, Themes
from src.reviews.models import Reviews
from src.articles.models import Articles
from src.database import async_engine, Base
from misc.utils import get_logger


logger = get_logger(__name__, log_level="DEBUG")


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
        select(Books.id, Books.title, Books.cover)
        .where(Books.active == True)
        .order_by(Books.id)     # после деплоя сделать сортировку по pub_date desc
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
        .order_by(Books.id)     # после деплоя сделать сортировку по pub_date desc
    )
    result = await session.execute(query)

    return result.scalars().all()


async def get_all_book_reviews(
    title: str,
    order_by: str,
    order_method: str,
    session: AsyncSession
):
    valid_order_columns = ['created_at', 'rating']
    valid_order_methods = ['asc', 'desc']
    
    if order_by not in valid_order_columns:
        raise ValueError(f"Invalid order_by value. Must be one of {valid_order_columns}. Got {order_by}")
    if order_method not in valid_order_methods:
        raise ValueError(f"Invalid order_method value. Must be one of {valid_order_methods}. Got {order_method}")

    order_func = asc if order_method == 'asc' else desc

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
        .order_by(order_func(getattr(Reviews, order_by)))
    )
    result = await session.execute(query)

    return result.fetchall()


async def get_active_articles(
    session: AsyncSession
):
    query = (
        select(
            Articles.id,
            Articles.title,
            Articles.summary,
            Articles.created_at,
            Articles.preview
        )
        .where(Articles.active == True)
        .order_by(Articles.id)     # после деплоя сделать сортировку по created_at desc
    )
    result = await session.execute(query)
    return result.fetchall()


async def get_article_by_id(
    id: int,
    session: AsyncSession
):
    query = (
        select(Articles, Themes)
        .join(Themes, Articles.theme == Themes.id)
        .where(
            Articles.id == id,
            Articles.active == True
        )
    )
    result = await session.execute(query)
    article, theme = result.fetchall()[0]

    if article:
        logger.debug(f'get_article_by_id found article: {article}, theme: {theme}')
    else:
        logger.debug(f'get_article_by_id found no article with id {id}')
    
    return article, theme
