from typing import Optional

from fastapi_users import schemas
from pydantic import ConfigDict


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    model_config = ConfigDict(from_attributes=True)


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    # confirm_password: str
    role_id: int = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserReadRel(UserRead):
    reviews: list["ReviewOutRel"]
