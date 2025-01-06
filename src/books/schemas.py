from datetime import datetime

from pydantic import BaseModel


class GetAllBooks(BaseModel):
    id: int
    title: str
    series: str
    short_description: str
    full_description: str
    pub_date: datetime
    image: str
    pages: int
    language: str
    age: str
    reviews_count: int


class ReviewCreate(BaseModel):
    title: str
    text: str
    rating: int
