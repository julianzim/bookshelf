from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from src.database import get_async_session
from src.articles.models import Articles
from src.articles.schemas import GetAllArticles


router = APIRouter(prefix="/articles", tags=["Articles"])


@router.get(path="", response_model=List[GetAllArticles])
async def get_all_articles(session: AsyncSession = Depends(get_async_session)):
    query = select(Articles)
    result = await session.execute(query)
    articles = result.scalars().all()
    return articles


@router.get(path="/{article_id}")
async def get_article(article_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Articles).where(Articles.id == article_id)
    result = await session.execute(query)
    article = result.scalars().all()
    return article

