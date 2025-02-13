from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import get_all_books, get_active_articles
from src.database import get_async_session
from src.auth.base_config import auth_backend, fastapi_users, current_user_optional
from src.auth.schemas import UserCreate, UserRead
from src.books.router import router as router_books
from src.reviews.router import router as router_reviews
from src.articles.router import router as router_blog
from misc.utils import get_logger


APP_MODE = "dev"

root_logger = get_logger(
    name = __name__,
    log_level = "DEBUG",
    set_sqla_logger = False
)

templates = Jinja2Templates(directory = "templates/")

docs_url=None if APP_MODE == "production" else "/docs"
redoc_url=None if APP_MODE == "production" else "/redoc"
openapi_url=None if APP_MODE == "production" else "/openapi.json"

app = FastAPI(
    title = "Yassya Lil",
    docs_url=docs_url,
    redoc_url=redoc_url,
    openapi_url=openapi_url
)

app.mount("/static", StaticFiles(directory = "static"), name = "static")

app.include_router(router_books)
app.include_router(router_reviews)
app.include_router(router_blog)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix = "/auth",
    tags = ["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix = "/auth",
    tags = ["Auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix = "/auth",
    tags = ["Auth"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    root_logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    root_logger.info(f"Response: status {response.status_code}")
    return response


@app.get("/")
async def get_home(
    request: Request,
    current_user = Depends(current_user_optional),
    session: AsyncSession = Depends(get_async_session)
):
    current_user_log = current_user or 'Unauthenticated user'
    
    root_logger.debug(f"{current_user_log} requests the Home page")
    
    books_data = await get_all_books(session=session)
    books = [
        {
            "id": book[0],
            "title": book[1], 
            "image": book[2]
        } for book in books_data
    ]
    
    root_logger.info(f"Books found: {len(books)} for {current_user_log}")

    articles_data = await get_active_articles(session=session)
    articles = [
        {
            'id': article[0],
            'title': article[1],
            'summary': article[2],
            'created_at': article[3],
            'preview': article[4]
        } for article in articles_data
    ]

    root_logger.info(f"Articles found: {len(articles)} for {current_user_log}")

    return templates.TemplateResponse(
        "pages/home.html", 
        {
            "request": request,
            "books": books,
            "articles": articles,
            "current_user": current_user
        }
    )


@app.get("/about")
async def get_about(
    request: Request,
    current_user = Depends(current_user_optional)
):
    current_user_log = current_user or 'Unauthenticated user'

    root_logger.debug(f"{current_user_log} requests the About page")
    
    return templates.TemplateResponse(
        "pages/about.html", 
        {
            "request": request,
            "current_user": current_user
        }
    )


@app.get("/auth/reset-password")
async def reset_password_page(request: Request, token: str):
    return templates.TemplateResponse(
        "pages/reset-password.html",
        {
            "request": request,
            "token": token
        }
    )


@app.get("/policies/{doc_name}")
async def get_policies(request: Request, doc_name: str):
    return templates.TemplateResponse(
        f"docs/{doc_name}.html",
        {
            "request": request
        }
    )


@app.exception_handler(HTTPException)
async def http_exc_handler(
    request: Request,
    exc: HTTPException
):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        root_logger.warning("Unauthorized access, redirecting to the login page")
        return RedirectResponse(
            url="/auth/login", 
            status_code = status.HTTP_303_SEE_OTHER
        )
    else:
        root_logger.error(f"HTTPException: {exc.detail}")
        return HTMLResponse(
            content=f"""
            <html>
                <head><title>Error {exc.status_code}</title></head>
                <body>
                    <h1>Error {exc.status_code}</h1>
                    <p>{exc.detail}</p>
                    <a href="/">Back to the Home</a>
                </body>
            </html>
            """,
            status_code=exc.status_code
        )
    
