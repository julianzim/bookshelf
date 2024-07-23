from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.books.router import router as router_books
from src.articles.router import router as router_articles
from src.pages.router import router as router_pages


app = FastAPI(title="Yassya Lil")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)
app.include_router(router_books)
app.include_router(router_articles)


# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
