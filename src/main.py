from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from src.queries import reset_database
from src.books.router import router as router_books
from src.articles.router import router as router_articles
from src.router import router as router_index

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await reset_database()
    yield
    print("Выключение")


app = FastAPI(
    title="Blog of Yassya Lil"
    # lifespan=lifespan
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_index)
app.include_router(router_books)
app.include_router(router_articles)






# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
