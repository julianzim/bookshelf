from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from src.books.router import get_all_books
from src.articles.router import get_all_articles



router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/about")
async def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/books")
async def get_about(request: Request, books=Depends(get_all_books)):
    return templates.TemplateResponse("books.html", {"request": request, "books": books})


@router.get("/articles")
async def get_about(request: Request, articles=Depends(get_all_articles)):
    return templates.TemplateResponse("articles.html", {"request": request, "articles": articles})
