import os
import sys
import asyncio
import pandas as pd
from pathlib import Path
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sqlalchemy import select

from src.books.models import Books, BookInfo, Themes
from src.database import async_session


TABLE_PATH = Path("misc/upload/books/books.xlsx")


async def upload_books(table_path: Path):
    
    df = pd.read_excel(table_path)
    df['summary'] = df['summary'].apply(lambda x: '\n'.join(f'<p>{line}</p>' for line in x.split('\n')))
    books, books_infos = [], []
    
    for _, row in df.iterrows():
        query = (
            select(Themes.id)
            .where(Themes.name == row["theme"])
        )
        async with async_session() as session:
            result = await session.execute(query)
            theme_id = result.scalar()
            if not theme_id:
                new_theme = Themes(name=row["theme"])
                session.add(new_theme)
                await session.commit()
                await session.refresh(new_theme)
                theme_id = new_theme.id

        books.append(
            Books(
                series = row["series"],
                theme = theme_id,
                title = row["title"],
                summary = row["summary"],
                pub_date = row["pub_date"],
                author = row["author"],
                cover = row["cover"],
                pages = row["pages"],
                language = row["language"],
                min_age = row["min_age"],
                max_age = row["max_age"],
                amazon_link = row["amazon_link"],
                aloud_link = row["aloud_link"],
                hc_price = row["hc_price"],
                pb_price = row["pb_price"],
                active = True
            )
        )
        books_infos.append(
            BookInfo(
                pub_date = row["pub_date"],
                author = row["author"],
                cover = row["cover"],
                pages = row["pages"],
                language = row["language"],
                min_age = row["min_age"],
                max_age = row["max_age"],
                amazon_link = row["amazon_link"],
                aloud_link = row["aloud_link"],
                hc_price = row["hc_price"],
                pb_price = row["pb_price"]
            )
        )
    
    async with async_session() as session:
            session.add_all(books)
            session.add_all(books_infos)
            await session.commit()


if __name__ == "__main__":
    asyncio.run(upload_books(table_path=TABLE_PATH))