from pydantic import BaseModel


class ReviewCreate(BaseModel):
    title: str
    text: str
    rating: int
