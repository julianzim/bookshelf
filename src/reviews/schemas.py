from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100, description="Title of the review")
    text: str = Field(min_length=10, max_length=1000, description="Text of the review")
    rating: int = Field(ge=1, le=5, description="Rating between 1 and 5")