from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession

from src.queries import get_active_books
from src.database import get_async_session
from src.auth.base_config import auth_backend, fastapi_users, current_user_optional
from src.auth.schemas import UserCreate, UserRead
from src.books.router import router as router_books
from src.reviews.router import router as router_reviews
from src.articles.router import router as router_blog
from misc.utils import get_logger


root_logger = get_logger(
    name = __name__,
    log_level = "DEBUG",
    set_sqla_logger = False
)

templates = Jinja2Templates(directory = "templates/")

app = FastAPI(title = "Yassya Lil")

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
    
    books_data = await get_active_books(session=session)
    books = [
        {
            "id": book[0],
            "title": book[1], 
            "image": book[2]
        } for book in books_data
    ]
    
    root_logger.info(f"Books found: {len(books)} for {current_user_log}")

    return templates.TemplateResponse(
        "pages/home.html", 
        {
            "request": request,
            "books": books,
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


@app.exception_handler(HTTPException)
async def exc_401_handler(
    request: Request,
    exc: HTTPException
):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        root_logger.warning("Unauthorized access, redirecting to the login page")
        return RedirectResponse(
            url="/auth/login", 
            status_code = status.HTTP_303_SEE_OTHER
        )
    
    root_logger.error(f"HTTPException: {exc.detail}")
    
    return JSONResponse(
        status_code = exc.status_code, 
        content = {"detail": exc.detail}
    )
