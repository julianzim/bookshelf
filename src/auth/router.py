from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.auth.base_config import current_user_optional


router = APIRouter(prefix="/auth", tags=["Auth"])

templates = Jinja2Templates(directory="templates/")


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        request=request,
        name="pages/login.html",
        context={"current_user": current_user}
    )


@router.get("/register", response_class=HTMLResponse)
async def get_register_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        request=request,
        name="pages/register.html",
        context={"current_user": current_user}
    )


@router.get("/forgot-password", response_class=HTMLResponse)
async def get_forgot_password_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        request=request,
        name="pages/forgot-password.html",
        context={"current_user": current_user}
    )


@router.get("/reset-password", response_class=HTMLResponse)
async def get_reset_password_page(request: Request, token: str):
    return templates.TemplateResponse(
        request=request,
        name="pages/reset-password.html",
        context={"token": token}
    )