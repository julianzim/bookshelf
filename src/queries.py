from fastapi import HTTPException
from sqlalchemy import select, join, desc, asc
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas import UserRead
from src.books.models import Books, Themes
from src.books.schemas import BookCard, BookDetail
from src.reviews.models import Reviews
from src.reviews.schemas import ReviewOut, ReviewOutRel
from src.articles.models import Articles
from src.articles.schemas import ArticleCard, ArticleDetail, ThemeDetail
from src.database import async_engine, Base
from misc.utils import get_logger


logger = get_logger(__name__, log_level="DEBUG")


async def reset_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    # yield
    print('База данных сброшена')


async def get_all_books(session: AsyncSession) -> list[BookCard]:
    query = select(Books).order_by(asc(Books.pub_date))
    result = await session.execute(query)

    books_orm = result.scalars().all()
    books = [BookCard.model_validate(book) for book in books_orm]

    return books


async def get_book_by_title(title: str, session: AsyncSession) -> BookDetail | None:
    query = select(Books).where(Books.title == title)
    result = await session.execute(query)

    book_orm = result.scalars().first()
    if book_orm is None:
        logger.error("Book \"%s\" not found", title)
        raise HTTPException(status_code=404, detail=f"Book \"{title}\" not found")

    book = BookDetail.model_validate(book_orm)

    return book


async def get_related_books_by_title(title: str, session: AsyncSession) -> list[BookCard]:
    query = (
        select(Books)
        .where(Books.title != title, Books.active)
        .order_by(asc(Books.pub_date))
    )
    result = await session.execute(query)

    books_orm = result.scalars().all()
    books = [BookCard.model_validate(book) for book in books_orm]

    return books


async def get_all_book_reviews(
    title: str,
    order_by: str,
    order_method: str,
    session: AsyncSession
) -> list[ReviewOut]:
    valid_order_columns = ['created_at', 'rating']
    valid_order_methods = ['asc', 'desc']

    if order_by not in valid_order_columns:
        raise ValueError(
            f"Invalid order_by value. Must be one of {valid_order_columns}. Got {order_by}"
        )
    if order_method not in valid_order_methods:
        raise ValueError(
            f"Invalid order_method value. Must be one of {valid_order_methods}. Got {order_method}"
        )

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
        .where(Books.title == title, Reviews.approved)
        .order_by(order_func(getattr(Reviews, order_by)))
    )
    result = await session.execute(query)

    reviews_orm = result.fetchall()
    reviews = [ReviewOut.model_validate(review) for review in reviews_orm]

    return reviews


async def get_review_by_id(
    review_id: int,
    session: AsyncSession
) -> Reviews:
    query = (
        select(Reviews)
        .options(
            joinedload(Reviews.user),
            joinedload(Reviews.book)
        )
        .where(Reviews.id == review_id)
    )
    result = await session.execute(query)
    review_orm = result.unique().scalars().first()
    if not review_orm:
        raise HTTPException(status_code=404, detail=f"Review {review_id} not found")

    if review_orm.published:
        logger.error(
            "Re-moderation is not allowed — review %s has already been moderated and published.",
            review_id
        )
        raise HTTPException(
            status_code = 400,
            detail = (
                f"Re-moderation is not allowed — review {review_id} has already been moderated "
                f"and published."
            )
        )
    # review = ReviewOutRel.model_validate(review_orm)
    return review_orm


async def get_active_articles(session: AsyncSession) -> list[ArticleCard]:
    query = (
        select(Articles)
        .where(Articles.active)
        .order_by(desc(Articles.created_at))
    )
    result = await session.execute(query)

    articles_orm = result.scalars().all()
    articles = [ArticleCard.model_validate(article) for article in articles_orm]

    return articles


async def get_article_by_id(
    id: int,
    session: AsyncSession
) -> tuple[ArticleDetail, ThemeDetail]:
    query = (
        select(Articles, Themes)
        .join(Themes, Articles.theme == Themes.id)
        .where(Articles.id == id, Articles.active)
    )
    result = await session.execute(query)
    if result is None:
        logger.error("Article id=%s not found", id)
        raise HTTPException(status_code=404, detail=f"Article id={id} not found")

    article_orm, theme_orm = result.first()
    article = ArticleDetail.model_validate(article_orm)
    theme = ThemeDetail.model_validate(theme_orm)

    return article, theme


async def get_user_by_id(user_id: int, session: AsyncSession) -> UserRead:
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)

    user_orm = result.scalars().first()
    if user_orm is None:
        logger.error("User id=%s not found", user_id)
        raise HTTPException(status_code=404, detail=f"User id={user_id} not found")

    user = UserRead.model_validate(user_orm)

    return user
