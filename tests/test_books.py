import pytest

from httpx import AsyncClient, ASGITransport
from bs4 import BeautifulSoup
from typing import AsyncGenerator

from src.main import app


# pytestmark = pytest.mark.skip(reason="Все тесты в этом файле временно отключены")


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_books(async_client: AsyncClient) -> None:
    response = await async_client.get("/books")
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('div', class_='book-item')
    assert len(books) == 15
        

@pytest.mark.asyncio
async def test_get_book_details(async_client: AsyncClient) -> None:
    response = await async_client.get(f"/books/My%20Friend%20Joy")
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1', class_='book-title-right')
    assert 'My Friend Joy' in title.text

    img = soup.find('img', class_='book-cover-details')
    assert '/static/images/covers/MyFriendJoy.png' in img['src']

        