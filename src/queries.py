from fastapi import FastAPI

from src.database import async_engine, Base


async def reset_database(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    print('База данных сброшена')
