import datetime
import sqlalchemy as sa

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base



class Reviews(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=sa.text("TIMEZONE('utc', now())"),
        nullable=False
    )
    rating: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    approved: Mapped[bool] = mapped_column(nullable=False, server_default=sa.text("false"))
    rejection_reason: Mapped[str] = mapped_column(nullable=True)
    moderated: Mapped[bool] = mapped_column(nullable=False, server_default=sa.text("false"))
    published: Mapped[bool] = mapped_column(nullable=False, server_default=sa.text("false"))

    user: Mapped["User"] = relationship(
        back_populates="reviews"
    )
    book: Mapped["Books"] = relationship(
        back_populates="reviews"
    )
