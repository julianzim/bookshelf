import asyncio

from src.database import async_session
from src.books.models import Books
from src.articles.models import Articles
from src.queries import reset_database

from datetime import date


example_books = [
    Books(
        title="My friend Joy",
        short_description="Description 1",
        full_description="Description 1",
        pub_date=date(2023, 12, 17),
        author="Yassya Lil",
        image="JoyCover.jpg"
    ),
    Books(
        title="My friend Sadness",
        short_description="Description 2",
        full_description="Description 1",
        pub_date=date(2024, 4, 25),
        author="Yassya Lil",
        image="SadnessCover.jpg"
    ),
    Books(
        title="My friend Anger",
        short_description="Description 3",
        full_description="Description 1",
        pub_date=date(2024, 4, 1),
        author="Yassya Lil",
        image="AngerCover.jpg"
    ),
    Books(
        title="My friend Fear",
        short_description="Description 4",
        full_description="Description 1",
        pub_date=date(2024, 2, 2),
        author="Yassya Lil",
        image="FearCover.jpg"
    ),
    Books(
        title="My friend Envy",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="EnvyCover.png"
    )
]

example_articles = [
    Articles(
        title="Article 1",
        short_description="Article description 1",
        full_description="Article description 1",
        created_at=date(2024, 1, 10)
    ),
    Articles(
        title="Article 2",
        short_description="Article description 2",
        full_description="Article description 1",
        created_at=date(2024, 3, 15)
    ),
    Articles(
        title="Article 3",
        short_description="Article description 3",
        full_description="Article description 1",
        created_at=date(2024, 5, 20)
    )
]


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


asyncio.run(remake())
