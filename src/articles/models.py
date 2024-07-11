from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

import datetime


class Articles(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    short_description: Mapped[str]
    full_description: Mapped[str]
    created_at: Mapped[datetime.datetime]
