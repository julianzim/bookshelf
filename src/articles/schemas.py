from datetime import datetime

from pydantic import BaseModel


class GetAllArticles(BaseModel):
    id: int
    title: str
    short_description: str
    full_description: str
    created_at: datetime

    class Config:
        orm_mode = True
