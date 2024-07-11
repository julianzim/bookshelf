from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.books.models import Books

router = APIRouter(prefix="/books", tags=["Books"])

templates = Jinja2Templates(directory="templates")


@router.get(path="/", response_class=HTMLResponse)
async def get_all_books(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(Books)
    result = await session.execute(query)
    books = result.scalars().all()
    return templates.TemplateResponse("books.html", {"request": request, "books": books})


@router.get(path="/book_{book_id}")
async def get_book(book_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Books).where(Books.id == book_id)
    result = await session.execute(query)
    book = result.scalars().all()
    return book
