import statistics
import logging
import os

from docx import Document

from src.reviews.models import Reviews


async def get_reviews_statistics(reviews: list[Reviews]):
    ratings = [review.rating for review in reviews]
    reviews_texts = [review.text for review in reviews]
    if ratings:
        average_rating = round(statistics.mean(ratings), 1)
    else:
        average_rating = 0
    ratings_count = len(ratings)
    reviews_count = len(reviews_texts)
        
    return {
        "average_rating": average_rating,
        "ratings_count": ratings_count,
        "reviews_count": reviews_count
    }


def get_logger(name: str = None, log_level: str = None, set_sqla_logger: bool = False):
    """
    Returns a configured logger with the specified name and logging level.
    The logging level can be set either via an argument or the LOG_LEVEL environment variable.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        log_format = "%(asctime)s - %(levelname)-8s - %(name)s - %(message)s"
        formatter = logging.Formatter(log_format)

        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        if log_level is None:
            log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        if isinstance(log_level, str):
            log_level = getattr(logging, log_level.upper(), logging.INFO)
        elif isinstance(log_level, int):
            pass
        else:
            raise ValueError("Log level must be either a string or an integer.")
        
        logger.setLevel(log_level)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        if set_sqla_logger:
            sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
            sqlalchemy_logger.setLevel(logging.WARNING)
            sqlalchemy_logger.addHandler(file_handler)

    return logger


def format_runs(runs):
    formatted_text = ""
    
    for run in runs:
        text = run.text
        if run.bold:
            text = f'<b class="bold-text">{text}</b>'
        if run.italic:
            text = f'<i class="italic-text">{text}</i>'
        if run.underline:
            text = f'<u class="underline-text">{text}</u>'
        formatted_text += text
    
    return formatted_text


def convert_docx_to_html(input_file: str, output_file: str):
    
    doc = Document(input_file)
    
    html_content = ""
    for paragraph in doc.paragraphs:
        if not paragraph.text.strip():
            continue

        if paragraph.style.name.startswith("Heading"):
            level = int(paragraph.style.name[-1])
            html_content += ((level-1) * "\t" + f'<h{level} class="article-header{level}">{format_runs(paragraph.runs)}</h{level}>\n')
        else:
            if paragraph.runs != "":
                html_content += (level * "\t" + f'<p class="artile-paragraph">{format_runs(paragraph.runs)}</p>\n')
            else:
                html_content += ("\n")
    
    return html_content
