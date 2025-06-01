import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.auth.schemas import UserReadRel
from src.books.schemas import BookDetailRel


class ReviewCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100, description="Title of the review")
    text: str = Field(min_length=10, max_length=1000, description="Text of the review")
    rating: int = Field(ge=1, le=5, description="Rating between 1 and 5")


class ReviewOut(ReviewCreate):
    username: str = Field(min_length=1, max_length=100)
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class BookReviewStats(BaseModel):
    average_rating: float
    ratings_count: int
    reviews_count: int


class ReviewOutRel(ReviewCreate):
    created_at: datetime.datetime

    user: "UserReadRel"
    book: "BookDetailRel"


ReviewOutRel.model_rebuild()
