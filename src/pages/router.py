from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from src.auth.base_config import current_user_optional
from src.books.router import get_book, get_related_books


router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates/")


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
