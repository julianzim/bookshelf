from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from src.queries import get_article_by_id
from src.database import get_async_session
from src.articles.models import Articles
from src.articles.schemas import GetAllArticles
from src.auth.base_config import current_user_optional


router = APIRouter(prefix="/blog", tags=["Blog"])

templates = Jinja2Templates(directory="templates/")


@router.get(path="")
async def get_all_articles(
    request: Request,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(
        Articles.id,
        Articles.title,
        Articles.summary,
        Articles.created_at,
        Articles.preview
    )
    result = await session.execute(query)
    articles = result.fetchall()
    articles_rows = [
        {
            'id': article[0],
            'title': article[1],
            'summary': article[2],
            'created_at': article[3],
            'preview': article[4]
        } for article in articles
    ]
    
    return templates.TemplateResponse(
        "pages/blog.html",
        {
            "request": request,
            "articles": articles_rows,
            "current_user": current_user
        }
    )


@router.get(path="/article_{article_id}")
async def get_article(
    article_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    article = await get_article_by_id(
        id = article_id,
        session = session
    )
    
    return article

