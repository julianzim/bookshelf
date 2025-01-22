from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import get_active_articles, get_article_by_id
from src.database import get_async_session
from src.auth.base_config import current_user_optional
from misc.utils import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix = "/blog", tags = ["Blog"])

templates = Jinja2Templates(directory = "templates/")


@router.get(path="")
async def get_blog(
    request: Request,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'

    logger.debug(f'{current_user_log} requests the Blog page')

    articles_data = await get_active_articles(session=session)
    articles = [
        {
            'id': article[0],
            'theme': article[1],
            'title': article[2],
            'summary': article[3],
            'created_at': article[4],
            'preview': article[5],
            'read_time': article[6]
        } for article in articles_data
    ]

    logger.info(f"Articles found: {len(articles)} for {current_user_log}")
    
    return templates.TemplateResponse(
        "pages/blog.html",
        {
            "request": request,
            "articles": articles,
            "current_user": current_user
        }
    )


@router.get(path="/article_{article_id}")
async def get_article(
    request: Request,
    article_id: int,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'

    logger.debug(f'{current_user_log} requests page of article "{article_id}"')

    article = await get_article_by_id(
        id = article_id,
        session = session
    )

    if not article:
        logger.error(f"Article id={article_id} not found")
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        logger.info(f'Article id={article.id} found for {current_user_log}')

        return templates.TemplateResponse(
            "pages/article.html",
            {
                "request": request,
                "article": article,
                "current_user": current_user
            }
        )
