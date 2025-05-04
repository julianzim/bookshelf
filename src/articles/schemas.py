import datetime

from pydantic import BaseModel, ConfigDict, Field


class BaseArticle(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ArticleCard(BaseArticle):
    id: int
    title: str
    summary: str = Field(max_length=2000)
    created_at: datetime.datetime
    preview: str = Field(pattern=r".+\.(png|jpg|jpeg)$")


class ArticleDetail(ArticleCard):
    theme: int
    text: str
    read_time: int = Field(gt=0, lt=60)
    header_image: str = Field(pattern=r".+\.(png|jpg|jpeg)$")


class ThemeDetail(BaseArticle):
    name: str
