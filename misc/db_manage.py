import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import async_session
from src.queries import reset_database

from misc.examples import example_reviews, example_books, example_articles, roles


async def add_roles():
    async with async_session() as session:
        session.add_all(roles)
        await session.commit()
        print("Роли добавлены.")


async def add_books():
    async with async_session() as session:
        session.add_all(example_books)
        await session.commit()
        print("Книги добавлены.")


async def add_articles():
    async with async_session() as session:
        session.add_all(example_articles)
        await session.commit()
        print("Статьи добавлены.")


async def add_reviews():
    async with async_session() as session:
        session.add_all(example_reviews)
        await session.commit()
        print("Отзывы добавлены.")


async def remake():
    await reset_database()
    await add_books()
    await add_articles()
    await add_roles()
    # await add_reviews()


if __name__ == "__main__":
    asyncio.run(remake())
    # asyncio.run(reset_database())
    # asyncio.run(add_books())
    # asyncio.run(add_articles())
    # asyncio.run(add_roles())
