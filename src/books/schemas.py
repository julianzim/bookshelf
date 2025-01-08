from pydantic import BaseModel


class GetAllBooks(BaseModel):
    id: int
    title: str
    image: str


class ReviewCreate(BaseModel):
    title: str
    text: str
    rating: int
