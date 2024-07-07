from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

import datetime


class Articles(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    created_at: Mapped[datetime.datetime]
