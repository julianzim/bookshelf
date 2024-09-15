from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from src.books.router import get_all_books, get_book, get_related_books
from src.articles.router import get_all_articles


router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/")
async def get_home(request: Request, books=Depends(get_all_books)):
    return templates.TemplateResponse("pages/home.html", {"request": request, "books": books})


@router.get("/about")
async def get_about(request: Request):
    return templates.TemplateResponse("pages/about.html", {"request": request})


@router.get("/books")
async def get_books(request: Request, books=Depends(get_all_books)):
    return templates.TemplateResponse("pages/books.html", {"request": request, "books": books})


@router.get("/books/{book_name}")
async def get_book_detail(request: Request, book=Depends(get_book), books=Depends(get_related_books)):
    return templates.TemplateResponse("pages/book_details.html", {"request": request, "book": book, "books": books})


@router.get("/blog")
async def get_blog(request: Request, articles=Depends(get_all_articles)):
    return templates.TemplateResponse("pages/blog.html", {"request": request, "articles": articles})


@router.get("/auth/register")
async def get_registration(request: Request):
    return templates.TemplateResponse("auth_pages/registration.html", {"request": request})


@router.get("/auth/login")
async def get_registration(request: Request):
    return templates.TemplateResponse("auth_pages/login.html", {"request": request})
