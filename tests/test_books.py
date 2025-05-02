import pytest

from httpx import AsyncClient, ASGITransport
from bs4 import BeautifulSoup

from src.main import app


@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.get("/books")
        assert response.status_code == 200

        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('div', class_='book-item')
        assert len(books) == 15
        


@pytest.mark.asyncio
async def test_get_book_details():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.get(f"/books/My%20Friend%20Joy")
        assert response.status_code == 200

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1', class_='book-title-right')
        assert 'My Friend Joy' in title.text

        img = soup.find('img', class_='book-cover-details')
        assert '/static/images/covers/MyFriendJoy.png' in img['src']

        