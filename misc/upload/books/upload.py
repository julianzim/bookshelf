import os
import sys
import pandas as pd
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.books.models import Books, BookInfo, Themes


file_path = Path("misc/upload/books/books.xlsx")

df = pd.read_excel(file_path)

books = []
books_infos = []
for _, row in df.iterrows():
    books.append(
        Books(
            series=row["series"],
            theme=row["theme"],
            title=row["title"],
            summary=row["summary"],
            pub_date=row["pub_date"],
            author=row["author"],
            cover=row["cover"],
            pages=row["pages"],
            language=row["language"],
            min_age=row["min_age"],
            max_age=row["max_age"],
            amazon_link=row["amazon_link"],
            aloud_link=row["aloud_link"],
            hc_price=row["hc_price"],
            pb_price=row["pb_price"],
            active=True
        )
    )
    books_infos.append(
        BookInfo(
            pub_date=row["pub_date"],
            author=row["author"],
            cover=row["cover"],
            pages=row["pages"],
            language=row["language"],
            min_age=row["min_age"],
            max_age=row["max_age"],
            amazon_link=row["amazon_link"],
            aloud_link=row["aloud_link"],
            hc_price=row["hc_price"],
            pb_price=row["pb_price"]
        )
    )