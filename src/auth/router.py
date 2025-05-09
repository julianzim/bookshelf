from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.auth.base_config import current_user_optional


router = APIRouter(prefix="/auth", tags=["Auth"])

templates = Jinja2Templates(directory="templates/")


@router.get("/login")
async def get_login_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/login.html",
        {
            "request": request,
            "current_user": current_user
        }
    )


@router.get("/register")
async def get_register_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/register.html",
        {
            "request": request,
            "current_user": current_user
        }
    )


@router.get("/forgot-password")
async def get_forgot_password_page(
    request: Request,
    current_user = Depends(current_user_optional)
):
    return templates.TemplateResponse(
        "pages/forgot-password.html",
        {
            "request": request,
            "current_user": current_user
        }
    )


@router.get("/reset-password")
async def get_reset_password_page(request: Request, token: str):
    return templates.TemplateResponse(
        "pages/reset-password.html",
        {
            "request": request,
            "token": token
        }
    )