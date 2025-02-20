from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

import datetime


class Articles(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False
    )
    theme: Mapped[int] = mapped_column(
        ForeignKey("themes.id", ondelete="CASCADE"),
        nullable=True
    )
    title: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    preview: Mapped[str] = mapped_column(nullable=True)
    header_image: Mapped[str] = mapped_column(nullable=True)
    read_time: Mapped[int] = mapped_column(nullable=False, default=5)
    active: Mapped[bool] = mapped_column(nullable=False, default=False)