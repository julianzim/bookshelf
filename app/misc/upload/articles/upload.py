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

BASE_DIR = Path("misc/upload/articles/blog")
PROD_DIR = Path("static/images/")


def find_image_file(folder: Path, name_prefix: str):
    for ext in (".jpg", ".png", ".jpeg"):
        file = folder / f"{name_prefix}{ext}"
        if file.exists():
            return file
    return None


async def upload_articles(base_dir: Path, prod_dir: Path):
    articles = []
    
    for folder in sorted(base_dir.iterdir()):
        if not folder.is_dir():
            continue
        
        docx_file = folder / f"{folder.name}.docx"
        preview_file = find_image_file(folder, f"{folder.name}_preview")
        header_image_file = find_image_file(folder, f"{folder.name}_header")
        
        if not docx_file.exists() or not preview_file.exists() or not header_image_file.exists():
            print(f"Skipping {folder.name}: missing required files. {docx_file,preview_file,header_image_file}")
            continue
        
        parsed_docx = convert_docx_to_html(docx_file)
        theme_name = parsed_docx["theme"]
        
        async with async_session() as session:
            query = select(Themes.id).where(Themes.name == theme_name)
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
                theme=theme_id,
                title=parsed_docx["title"],
                summary=parsed_docx["summary"],
                text=parsed_docx["html_content"],
                created_at=parsed_docx["pub_date"],
                preview=preview_file.name,
                header_image=header_image_file.name,
                read_time=parsed_docx["read_time"],
                active=True
            )
        )
        
        shutil.move(preview_file, prod_dir / 'previews' / preview_file.name)
        shutil.move(header_image_file, prod_dir / 'header_images' / header_image_file.name)
        shutil.rmtree(folder)
    
    async with async_session() as session:
        session.add_all(articles)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(upload_articles(base_dir=BASE_DIR, prod_dir=PROD_DIR))
