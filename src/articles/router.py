from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.articles.models import Articles


router = APIRouter(prefix="/articles", tags=["Articles"])


@router.get(path="/")
async def get_all_books(session: AsyncSession = Depends(get_async_session)):
    query = select(Articles)
    result = await session.execute(query)
    articles = result.scalars().all()
    return articles
