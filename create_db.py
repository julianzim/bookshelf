from sqlalchemy.orm import Session
from database import engine
from models import Base, Book
from datetime import date

Base.metadata.create_all(bind=engine)

session = Session(bind=engine)

books = [
    Book(name="My friend Joy", description="Description 1", pub_date=date(2023, 12, 17), author="Yassya Lil", image="JoyCover.jpg"),
    Book(name="My friend Sadness", description="Description 2", pub_date=date(2024, 4, 25), author="Yassya Lil", image="SadnessCover.jpg"),
    Book(name="My friend Anger", description="Description 2", pub_date=date(2024, 4, 1), author="Yassya Lil", image="AngerCover.jpg"),
    Book(name="My friend Fear", description="Description 2", pub_date=date(2024, 2, 2), author="Yassya Lil", image="FearCover.jpg"),
    Book(name="My friend Envy", description="Description 2", pub_date=date(2024, 3, 14), author="Yassya Lil", image="EnvyCover.png")
]

for book in books:
    session.add(book)

session.commit()
session.close()

print("Таблица инициализирована и данные добавлены.")
