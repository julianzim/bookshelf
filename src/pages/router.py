from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.base_config import current_user_optional
from src.books.router import get_book, get_related_books
from src.books.models import Books


router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/")
async def get_home(
    request: Request,
    current_user=Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Books.id, Books.title, Books.image)
    result = await session.execute(query)
    books = result.fetchall()
    books_rows = [{"id": book[0], "title": book[1], "image": book[2]} for book in books]
    
    return templates.TemplateResponse(
        "pages/home.html", {
            "request": request,
            "books": books_rows,
            "current_user": current_user
        }
    )


@router.get("/about")
async def get_about(
    request: Request,
    current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/about.html", {
            "request": request,
            "current_user": current_user
        }
    )


@router.get("/books/{book_name}")
async def get_book_detail(
    request: Request,
    book=Depends(get_book),
    books=Depends(get_related_books),
    current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/book_details.html", {
            "request": request,
            "book": book,
            "books": books,
            "current_user": current_user
        }
    )
