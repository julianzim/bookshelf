import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import async_session
from src.queries import reset_database

from misc.examples import (
    roles,
    example_books_info,
    example_reviews_info,
    example_articles_info,
    example_themes_info,
    generate_example_books_list,
    generate_example_reviews_list,
    generate_example_articles_list,
    generate_example_themes_list
)


async def add_roles():
    async with async_session() as session:
        session.add_all(roles)
        await session.commit()
        print("Роли добавлены.")


async def add_books():
    example_books = generate_example_books_list(**example_books_info)
    async with async_session() as session:
        session.add_all(example_books)
        await session.commit()
        print("Книги добавлены.")


async def add_articles():
    example_articles = generate_example_articles_list(**example_articles_info)
    async with async_session() as session:
        session.add_all(example_articles)
        await session.commit()
        print("Статьи добавлены.")


async def add_reviews():
    example_reviews = generate_example_reviews_list(**example_reviews_info)
    async with async_session() as session:
        session.add_all(example_reviews)
        await session.commit()
        print("Отзывы добавлены.")


async def add_themes():
    example_themes = generate_example_themes_list(**example_themes_info)
    async with async_session() as session:
        session.add_all(example_themes)
        await session.commit()
        print("Темы добавлены")


async def remake():
    await reset_database()
    await add_books()
    await add_articles()
    await add_roles()
    # await add_reviews()


if __name__ == "__main__":
    # asyncio.run(remake())
    # asyncio.run(reset_database())
    # asyncio.run(add_roles())
    # asyncio.run(add_themes())
    # asyncio.run(add_articles())
    # asyncio.run(add_books())
    asyncio.run(add_reviews())
