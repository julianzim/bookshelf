import pathlib

from src.articles.models import Articles
from misc.utils import convert_docx_to_html



def generate_example_articles_list(
    theme_id: int,
    docx_dir: str = '/misc/docx_files/to_db'
):
    docx_files = pathlib.Path(docx_dir).glob("*.docx")
    n = 1
    articles = []
    for docx in docx_files:
        parsed_docx = convert_docx_to_html(docx)
        articles.append(
            Articles(
                theme = theme_id,
                title = parsed_docx["title"],
                summary = parsed_docx["summary"],
                text = parsed_docx["html_content"],
                created_at = parsed_docx["pub_date"],
                preview = ...,
                header_image = ...,
                read_time = parsed_docx["read_time"],
                active = True
            )
        )
        n += 1
        
    return articles