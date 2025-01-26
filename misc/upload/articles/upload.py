import os
import shutil
from pathlib import Path

from src.articles.models import Articles
from misc.utils import convert_docx_to_html


PROD_DIR = Path("/static/images/")
BASE_DIR = Path("/misc/upload/articles")
DOCX_DIR = BASE_DIR / "docx_files"
PREVIEWS_DIR = BASE_DIR / "previews"
HEADER_IMAGES_DIR = BASE_DIR / "header_images"

docx_files = sorted(DOCX_DIR.glob("*.docx"))
preview_files = sorted(PREVIEWS_DIR.glob("*"))
header_files = sorted(HEADER_IMAGES_DIR.glob("*"))

print(docx_files)
print(preview_files)
print(header_files)

# # Создаем статьи, перемещаем изображения
# articles = []
# for docx_file, preview_file, header_file in zip(docx_files, preview_files, header_files):
#     # Читаем текст из .docx
#     text = read_docx(docx_file)

#     # Создаем объект модели
#     article = Articles(text, preview_file.name, header_file.name)
#     articles.append(article)

#     # Перемещаем изображения
#     shutil.move(preview_file, PROD_DIR / preview_file.name)
#     shutil.move(header_file, PROD_DIR / header_file.name)

# # Вывод результата
# for article in articles:
#     print(article)



# def prepare_articles(
#     theme_id: int,
#     docx_dir: str = '/misc/docx_files/to_db'
# ):
#     docx_files = Path(docx_dir).glob("*.docx")
#     n = 1
#     articles = []
#     for docx in docx_files:
#         parsed_docx = convert_docx_to_html(docx)
#         articles.append(
#             Articles(
#                 theme = theme_id,
#                 title = parsed_docx["title"],
#                 summary = parsed_docx["summary"],
#                 text = parsed_docx["html_content"],
#                 created_at = parsed_docx["pub_date"],
#                 preview = ...,
#                 header_image = ...,
#                 read_time = parsed_docx["read_time"],
#                 active = True
#             )
#         )
#         n += 1
        
#     return articles