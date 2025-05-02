# TODO: make more informative tests
import pytest
import random

from httpx import AsyncClient, ASGITransport
from bs4 import BeautifulSoup
from typing import AsyncGenerator

from src.main import app


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_blog(async_client: AsyncClient) -> None:
    response = await async_client.get("/blog")
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('a', class_='card')
    assert len(articles) >= 13


@pytest.mark.asyncio
async def test_get_article(async_client: AsyncClient) -> None:
    random_id = random.randint(1, 10)   # TODO: make articles count query from db
    response = await async_client.get(f"/blog/article_{random_id}")
    assert response.status_code == 200
