from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from src.books.router import get_all_books, get_book
from src.articles.router import get_all_articles



router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_index(request: Request, books=Depends(get_all_books)):
    return templates.TemplateResponse("index.html", {"request": request, "books": books})


@router.get("/about")
async def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/books")
async def get_books(request: Request, books=Depends(get_all_books)):
    return templates.TemplateResponse("books.html", {"request": request, "books": books})


@router.get("/books/{book_name}")
async def get_book_detail(request: Request, book=Depends(get_book)):
    return templates.TemplateResponse("book_details.html", {"request": request, "book": book})


@router.get("/articles")
async def get_articles(request: Request, articles=Depends(get_all_articles)):
    return templates.TemplateResponse("articles.html", {"request": request, "articles": articles})


@router.get("/auth")
async def get_registration(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})
