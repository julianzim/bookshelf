import datetime

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    series: Mapped[str] = mapped_column(nullable=True)
    theme: Mapped[int] = mapped_column(
        ForeignKey("themes.id", ondelete="CASCADE"),
        nullable=True
    )
    title: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
    pub_date: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), 
        nullable=False
    )
    author: Mapped[str] = mapped_column(nullable=False, default="Yassya Lil")
    cover: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(nullable=True)
    min_age: Mapped[int] = mapped_column(nullable=True)
    max_age: Mapped[int] = mapped_column(nullable=True)
    amazon_link: Mapped[str] = mapped_column(nullable=False)
    aloud_link: Mapped[str] = mapped_column(nullable=False)
    hc_price: Mapped[float] = mapped_column(nullable=False, server_default="9.99")
    pb_price: Mapped[float] = mapped_column(nullable=False, server_default="9.99")
    active: Mapped[bool] = mapped_column(nullable=False, default=False)


class Themes(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class BookInfo(Base):
    __tablename__ = "books_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(nullable=False, default="Yassya Lil")
    cover: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(nullable=True)
    min_age: Mapped[int] = mapped_column(nullable=True)
    max_age: Mapped[int] = mapped_column(nullable=True)
    amazon_link: Mapped[str] = mapped_column(nullable=False)
    aloud_link: Mapped[str] = mapped_column(nullable=False)
    # hc_price: Mapped[float] = mapped_column(nullable=False, server_default="9.99")
    # pb_price: Mapped[float] = mapped_column(nullable=False, server_default="9.99")
    pub_date: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), 
        nullable=False
    )
