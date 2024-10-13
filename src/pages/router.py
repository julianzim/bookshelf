from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from src.auth.base_config import current_user_optional
from src.books.router import get_all_books, get_book, get_related_books
from src.articles.router import get_all_articles


router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/")
async def get_home(
        request: Request,
        books=Depends(get_all_books),
        current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/home.html", {
            "request": request,
            "books": books,
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


@router.get("/books")
async def get_books(
        request: Request,
        books=Depends(get_all_books),
        current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/books.html", {
            "request": request,
            "books": books,
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


@router.get("/blog")
async def get_blog(
        request: Request,
        articles=Depends(get_all_articles),
        current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/blog.html", {
            "request": request,
            "articles": articles,
            "current_user": current_user
        }
    )


@router.get("/auth/register")
async def get_registration(
        request: Request,
        current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "auth_pages/registration.html", {
            "request": request,
            "current_user": current_user
        }
    )


@router.get("/auth/login")
async def get_registration(
        request: Request,
        current_user=Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "auth_pages/login.html", {
            "request": request,
            "current_user": current_user
        }
    )
