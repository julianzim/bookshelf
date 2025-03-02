from pydantic import BaseModel


class GetAllBooks(BaseModel):
    id: int
    title: str
    image: str
