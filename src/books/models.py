import datetime
from typing import Annotated
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    series: Mapped[str]
    short_description: Mapped[str]
    full_description: Mapped[str]
    pub_date: Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
    author: Mapped[str]
    image: Mapped[str]
    pages: Mapped[int]
    language: Mapped[str]
    age: Mapped[str]
    reviews_count: Mapped[int]


class Reviews(Base):
    __tablename__ = "reviews"

    id: Mapped[int] - mapped_column(primary_key=True)
    book: mapped_column(ForeignKey("books.id", ondelete="CASCADE"))
    reviewer: mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    rating: Mapped[int]
    title: Mapped[str]
    description: Mapped[str]
    created_at: Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
