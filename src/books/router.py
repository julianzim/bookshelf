from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import (
    get_all_books,
    get_book_by_title,
    get_related_books_by_title,
    get_all_book_reviews
)
from src.database import get_async_session
from src.auth.base_config import current_user_optional
from misc.utils import localize_reviews, get_reviews_statistics, get_logger


logger = get_logger(__name__)

router = APIRouter(prefix = "/books", tags = ["Books"])

templates = Jinja2Templates(directory = "templates/")


@router.get(path="", response_class=HTMLResponse)
async def get_books(
    request: Request,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'
    logger.debug(f'{current_user_log} requests the Books page')

    books = await get_all_books(session=session)
    logger.info(f"Books found: {len(books)} for {current_user_log}")
    
    return templates.TemplateResponse(
        request=request,
        name="pages/books.html",
        context={
            "books": books,
            "current_user": current_user
        }
    ) 


@router.get(path="/{book_title}", response_class=HTMLResponse)
async def get_book_details(
    book_title: str,
    request: Request,
    sort_by: str = 'rating',
    order: str = 'desc',
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'
    logger.debug(f'{current_user_log} requests page of book "{book_title}"')
    
    client_timezone = request.cookies.get("timezone", "UTC")
    try:
        local_tz = ZoneInfo(client_timezone)
    except ValueError:
        local_tz = ZoneInfo("UTC")

    book = await get_book_by_title(title = book_title, session = session)
    
    related_books = await get_related_books_by_title(
        title = book_title,
        session = session
    )
    book_reviews = await get_all_book_reviews(
        title = book_title,
        order_by = sort_by,
        order_method = order,
        session = session
    )
    book_reviews_stats = await get_reviews_statistics(reviews = book_reviews)
    book_reviews_localized = await localize_reviews(
        reviews = book_reviews,
        timezone = local_tz
    )

    logger.info(f'Book {book.title} found for {current_user_log}')

    return templates.TemplateResponse(
        request=request,
        name="pages/book_details.html",
        context={
            "book": book,
            "related_books": related_books,
            "current_user": current_user,
            "book_reviews": book_reviews_localized,
            "book_reviews_stats": book_reviews_stats,
            "sort_by": sort_by,
            "order": order
        }
    )
