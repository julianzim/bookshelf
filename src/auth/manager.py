from typing import Optional

from fastapi import Depends, Request
from fastapi.responses import Response
from fastapi_users import (
    BaseUserManager,
    IntegerIDMixin,
    exceptions,
    models,
    schemas
)

from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import app_config
from src.tasks import send_email
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
            logger.warning("User with email %s already exists", user_create.email)
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
        logger.info("%s has registered", user)

    async def on_after_login(
        self,
        user: models.UP,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ) -> None:
        logger.info("%s has login", user)
        if response:
            last_page = "/"
            # request.query_params.get("next") or request.headers.get("Referer") or "/"
            logger.debug("User id=%s redirecting to the page %s", user.id, last_page)
            response.status_code = 302
            response.headers["Location"] = last_page

    async def send_reset_password_email(self, email: str, token: str):
        subject = "Password Recovery"
        reset_url = f"http://{app_config.APP_DOMAIN}/auth/reset-password?token={token}"
        body = f"To reset your password, click on the following link:\n\n{reset_url}"
        email_result = send_email.delay(
            subject=subject,
            body=body,
            recipients=[email],
            subtype="plain"
        )
        logger.info(
            "Email with reset password link sent to user %s successfully. Result: %s",
            email, email_result
        )

    async def on_after_forgot_password(
            self,
            user: User,
            token: str,
            request: Optional[Request] = None
        ):
        await self.send_reset_password_email(user.email, token)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
