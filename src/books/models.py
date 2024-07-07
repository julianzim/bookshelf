from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

import datetime


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    pub_date: Mapped[datetime.datetime]
    author: Mapped[str]
    image: Mapped[str]
