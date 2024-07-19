from datetime import datetime

from pydantic import BaseModel


class GetAllBooks(BaseModel):
    id: int
    title: str
    short_description: str
    pub_date: datetime
    image: str

    class Config:
        orm_mode = True
