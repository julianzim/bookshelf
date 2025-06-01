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
    amazon_link: HttpUrl
    aloud_link: HttpUrl
    eb_price: float = Field(ge=0.0)
    pb_price: float = Field(ge=0.0)
    summary: str = Field(max_length=2000)
    language: str = Field(max_length=23)
    min_age: int = Field(gt=0, lt=100)
    max_age: int = Field(gt=0, lt=100)
    pages: int = Field(gt=0)


class BookDetailRel(BookDetail):
    reviews: list["ReviewOutRel"]
