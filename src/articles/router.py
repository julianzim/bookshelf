from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from src.database import get_async_session
from src.articles.models import Articles
from src.articles.schemas import GetAllArticles
from src.auth.base_config import current_user_optional


router = APIRouter(prefix="/blog", tags=["Blog"])

templates = Jinja2Templates(directory="templates/")


@router.get(path="", response_model=List[GetAllArticles])
async def get_all_articles(
    request: Request,
    current_user=Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Articles)
    result = await session.execute(query)
    articles = result.scalars().all()
    return templates.TemplateResponse(
        "pages/blog.html",
        {
            "request": request,
            "articles": articles,
            "current_user": current_user
        }
    )


@router.get(path="/{article_id}")
async def get_article(article_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Articles).where(Articles.id == article_id)
    result = await session.execute(query)
    article = result.scalars().all()
    return article

