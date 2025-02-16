from datetime import datetime

from pydantic import BaseModel


class GetAllArticles(BaseModel):
    id: int
    theme: str
    title: str
    summary: str
    text: str
    created_at: datetime
    read_time: int
    preview: str
