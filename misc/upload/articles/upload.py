import os
import sys
import shutil
import asyncio
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sqlalchemy import select

from src.database import async_session
from src.articles.models import Articles
from src.books.models import Themes
from misc.utils import convert_docx_to_html


PROD_DIR = Path("static/images/")
BASE_DIR = Path("misc/upload/articles")
DOCX_DIR = BASE_DIR / "docx_files"
PREVIEWS_DIR = BASE_DIR / "previews"
HEADER_IMAGES_DIR = BASE_DIR / "header_images"


async def upload_articles(
    docx_dir: Path, 
    previews_dir: Path, 
    header_images_dir: Path
):
    docx_files = sorted(docx_dir.glob("*.docx"))
    preview_files = sorted(previews_dir.glob("*"))
    header_images_files = sorted(header_images_dir.glob("*"))

    articles = []
    for docx, preview, header_image in zip(
        docx_files, 
        preview_files, 
        header_images_files
    ):
        parsed_docx = convert_docx_to_html(docx)
        theme_name = parsed_docx["theme"]
        print(parsed_docx)
        query = (
            select(Themes.id)
            .where(Themes.name == theme_name)
        )
        async with async_session() as session:
            result = await session.execute(query)
            theme_id = result.scalar()
            if not theme_id:
                new_theme = Themes(name=theme_name)
                session.add(new_theme)
                await session.commit()
                await session.refresh(new_theme)
                theme_id = new_theme.id

        articles.append(
            Articles(
                theme = theme_id,
                title = parsed_docx["title"],
                summary = parsed_docx["summary"],
                text = parsed_docx["html_content"],
                created_at = parsed_docx["pub_date"],
                preview = preview.name,
                header_image = header_image.name,
                read_time = parsed_docx["read_time"],
                active = True
            )
        )

        async with async_session() as session:
            session.add_all(articles)
            await session.commit()
            
        shutil.move(preview, PROD_DIR / 'previews' / preview.name)
        shutil.move(header_image, PROD_DIR / 'header_images' / header_image.name)
        docx.unlink()


if __name__ == "__main__":
    asyncio.run(
        upload_articles(
            docx_dir=DOCX_DIR,
            previews_dir=PREVIEWS_DIR,
            header_images_dir=HEADER_IMAGES_DIR
        )
    )
