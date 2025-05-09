from typing import Optional

from fastapi import Depends, Request
from fastapi.responses import Response
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas
from fastapi_mail import FastMail, MessageSchema

from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import app_config, mail_conf
from misc.utils import get_logger


logger = get_logger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = app_config.APP_SECRET_AUTH
    verification_token_secret = app_config.APP_SECRET_AUTH


    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        # if user_create.password != user_create.confirm_password:      # TODO
        #     raise HTTPException(status_code=400, detail="Passwords do not match")

        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            logger.warning(f"User with email {user_create.email} already exists")
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        logger.info(f"{user} has registered")

    async def on_after_login(
        self,
        user: models.UP,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ) -> None:
        logger.info(f"{user} has login")
        if response:
            last_page = "/"     # request.query_params.get("next") or request.headers.get("Referer") or "/"
            logger.debug(f"User id={user.id} redirecting to the page {last_page}")
            response.status_code = 302
            response.headers["Location"] = last_page
            
    async def send_reset_password_email(self, email: str, token: str):
        subject = "Password Recovery"
        reset_url = f"http://yassyalil.com/auth/reset-password?token={token}"
        body = f"To reset your password, click on the following link:\n\n{reset_url}"

        message = MessageSchema(
            subject=subject,
            recipients=[email],  
            body=body,
            subtype="plain"
        )

        fm = FastMail(mail_conf)
        await fm.send_message(message)
    
    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        await self.send_reset_password_email(user.email, token)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
