from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.articles.models import Articles


router = APIRouter(prefix="/articles", tags=["Articles"])

templates = Jinja2Templates(directory="templates")


@router.get(path="/", response_class=HTMLResponse)
async def get_all_books(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(Articles)
    result = await session.execute(query)
    articles = result.scalars().all()
    return templates.TemplateResponse("articles.html", {"request": request, "articles": articles})


@router.get(path="/{article_id}")
async def get_book(article_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Articles).where(Articles.id == article_id)
    result = await session.execute(query)
    article = result.scalars().all()
    return article
