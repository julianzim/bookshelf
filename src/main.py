from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead
from src.books.router import router as router_books
from src.articles.router import router as router_articles
from src.pages.router import router as router_pages


app = FastAPI(title="Yassya Lil")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)
app.include_router(router_books)
app.include_router(router_articles)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
