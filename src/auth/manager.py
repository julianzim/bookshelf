from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas
from fastapi.responses import Response

from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import SECRET_AUTH
from misc.utils import get_logger


logger = get_logger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

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
            last_page = request.query_params.get("next") or request.headers.get("Referer") or "/"
            logger.debug(f"User id={user.id} redirecting to the page {last_page}")
            response.status_code = 302
            response.headers["Location"] = last_page

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


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
