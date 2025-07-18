import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class BaseBook(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

class BookCard(BaseBook):
    title: str
    cover: str = Field(pattern=r".+\.(png|jpg|jpeg)$")
    active: bool


class BookDetail(BookCard):
    series: str
    pub_date: datetime.datetime
    video_id: str = Field(min_length=11, max_length=11, description="YouTube video ID (11 symbols)")
    eb_asin: str = Field(min_length=10, max_length=10, description="Amazon ASIN (10 symbols)")
    pb_asin: str = Field(min_length=10, max_length=10, description="Amazon ASIN (10 symbols)")
    eb_price: float = Field(ge=0.0)
    pb_price: float = Field(ge=0.0)
    summary: str = Field(max_length=2000)
    language: str = Field(max_length=23)
    min_age: int = Field(gt=0, lt=100)
    max_age: int = Field(gt=0, lt=100)
    pages: int = Field(gt=0)


class BookDetailRel(BookDetail):
    reviews: list["ReviewOutRel"]
