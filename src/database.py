from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import db_config


DATABASE_URL = f"postgresql+asyncpg://{db_config.DB_USER}:{db_config.DB_PASS}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}"

async_engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
