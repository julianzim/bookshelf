import asyncio

from src.database import async_session
from src.queries import reset_database

from misc.examples import example_books, example_articles


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


async def remake():
    await reset_database()
    await add_books()
    await add_articles()


if __name__ == "__main__":
    asyncio.run(remake())
    # asyncio.run(reset_database())
    # asyncio.run(add_books())
    # asyncio.run(add_articles())
