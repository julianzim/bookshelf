import asyncio

from database import async_engine, async_session, Base
from models import Books
from datetime import date


books = [
    Books(name="My friend Joy", description="Description 1", pub_date=date(2023, 12, 17), author="Yassya Lil", image="JoyCover.jpg"),
    Books(name="My friend Sadness", description="Description 2", pub_date=date(2024, 4, 25), author="Yassya Lil", image="SadnessCover.jpg"),
    Books(name="My friend Anger", description="Description 3", pub_date=date(2024, 4, 1), author="Yassya Lil", image="AngerCover.jpg"),
    Books(name="My friend Fear", description="Description 4", pub_date=date(2024, 2, 2), author="Yassya Lil", image="FearCover.jpg"),
    Books(name="My friend Envy", description="Description 5", pub_date=date(2024, 3, 14), author="Yassya Lil", image="EnvyCover.png")
]


async def reset_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_books():
    async with async_session() as session:
        session.add_all(books)
        await session.commit()
        print("Данные добавлены.")

async def main():
    await reset_database()
    await add_books()

asyncio.run(main())
