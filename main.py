from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select

from src.database import async_session
from src.queries import reset_database
from src.books.models import Books

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

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    async with async_session() as session:
        query= select(Books)
        result = await session.execute(query)
        books = result.scalars().all()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})







# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
