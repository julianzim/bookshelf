import datetime
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    series: Mapped[str]
    short_description: Mapped[str]
    full_description: Mapped[str]
    pub_date: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    author: Mapped[str]
    image: Mapped[str]
    pages: Mapped[int]
    language: Mapped[str]
    min_age: Mapped[int]
    max_age: Mapped[int]
    reviews_count: Mapped[int]
    ratings_count: Mapped[int]
    mean_rating: Mapped[float]
    amazon_link: Mapped[str]
    aloud_link: Mapped[str]
    active: Mapped[bool] = mapped_column(nullable=False, default=False)
