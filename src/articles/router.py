from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import get_active_articles, get_article_by_id
from src.database import get_async_session
from src.auth.base_config import current_user_optional
from misc.utils import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix = "/blog", tags = ["Blog"])

templates = Jinja2Templates(directory = "templates/")


@router.get(path="", response_class=HTMLResponse)
async def get_blog(
    request: Request,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'
    logger.debug(f'{current_user_log} requests the Blog page')

    articles = await get_active_articles(session=session)
    logger.info(f"Articles found: {len(articles)} for {current_user_log}")
    
    return templates.TemplateResponse(
        request=request,
        name="pages/blog.html",
        context={
            "articles": articles,
            "current_user": current_user
        }
    )


@router.get(path="/article_{article_id}", response_class=HTMLResponse)
async def get_article(
    request: Request,
    article_id: int,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'
    logger.debug(f'{current_user_log} requests page of article "{article_id}"')

    article, theme = await get_article_by_id(
        id = article_id,
        session = session
    )
    logger.info(f'Article id={article.id} found for {current_user_log}')

    return templates.TemplateResponse(
        request=request,
        name="pages/article.html",
        context={
            "article": article,
            "theme": theme,
            "current_user": current_user
        }
    )
