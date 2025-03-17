import os
import sys
import asyncio
import contextlib
import pandas as pd
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from fastapi_users.exceptions import UserAlreadyExists
from datetime import datetime

from src.database import get_async_session
from src.auth.utils import get_user_db
from src.auth.schemas import UserCreate
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.reviews.models import Reviews
from src.queries import get_book_by_title


TABLE_PATH = Path("misc/upload/reviews/reviews.xlsx")

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    email: str,
    password: str,
    username: str,
    is_superuser: bool = False,
    role_id: int = 1
) -> User | None:
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            username=username, 
                            email=email, 
                            password=password, 
                            is_superuser=is_superuser, 
                            role_id=role_id
                        )
                    )
                    print(f"User created {user}")
                    return user
    except UserAlreadyExists:
        print(f"User {email} already exists")


async def create_users_from_xlsx(table_path: Path):
    df = pd.read_excel(table_path)
    
    for _, row in df.iterrows():
        user = await create_user(
            username=row["name"],
            email=row["email"],
            password=row["password"]
        )


async def upload_reviews_from_xlsx(table_path: Path):
    async for session in get_async_session():
        df = pd.read_excel(table_path)
        reviews = []
        for _, row in df.iterrows():
            user = await create_user(
                username=row["name"],
                email=row["email"],
                password=row["password"]
            )
            book = await get_book_by_title(
                title=row["book"],
                session=session
            )
            reviews.append(
                Reviews(
                    book_id=book.id,
                    user_id=user.id,
                    rating=row["rating"],
                    title=row["title"],
                    text=row["review"],
                    created_at=datetime.strptime(row["datetime"], "%H:%M:%S %d.%m.%Y")
                )
            )
        session.add_all(reviews)
        await session.commit()
        print("Reviews added")


if __name__ == "__main__":
    asyncio.run(upload_reviews_from_xlsx(TABLE_PATH))

