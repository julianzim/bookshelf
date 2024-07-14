from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


router = APIRouter(tags=["Main"])

templates = Jinja2Templates(directory="templates")


@router.get(path="/", response_class=HTMLResponse)
async def get_all_books(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get(path="/about", response_class=HTMLResponse)
async def get_all_books(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})