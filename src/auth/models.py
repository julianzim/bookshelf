from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    JSON,
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    text
)
from sqlalchemy.orm import Mapped, relationship

from src.database import Base
# from src.reviews.models import Reviews


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

    def __repr__(self):
        return f"Role(id={self.id}, name='{self.name}', permissions='{self.permissions}')"


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=text("TIMEZONE('utc', now())"))
    role_id = Column(Integer, ForeignKey(Role.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    reviews: Mapped[list["Reviews"]] = relationship(
        back_populates="user"
    )

    def __repr__(self):
        return f"User(id={self.id}, name='{self.username}', email='{self.email}', registered_at='{self.registered_at}')"
