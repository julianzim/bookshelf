from src.books.models import Books
from src.articles.models import Articles
from src.auth.models import Role

from datetime import date


reviews_count = 43
pub_date = date(2023, 12, 17)
pages = 35
language = "English"
age = "3-6"
series = "Our Emotions - Our Friends"
author = "Yassya Lil"
description = """
Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, dolor eget aliquet auctor, 
dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. Aliquam vitae leo tincidunt, 
convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex pellentesque rhoncus et quis felis. 
Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.
"""


example_books = [
    Books(
        title="My Friend Joy",
        image="JoyCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Sadness",
        image="SadnessCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Anger",
        image="AngerCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Fear",
        image="FearCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Envy",
        image="EnvyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Love",
        image="LoveCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Jealousy",
        image="JealousyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Resentment",
        image="ResentmentCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Shame",
        image="ShameCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Guilt",
        image="GuiltCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Loneliness",
        image="LonelinessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Shyness",
        image="ShynessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Indifference",
        image="IndifferenceCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Helplessness",
        image="HelplessnessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    ),
    Books(
        title="My Friend Boredom",
        image="BoredomCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language,
        reviews_count=reviews_count
    )
]

example_articles = [
    Articles(
        title="Article 1",
        short_description=description,
        full_description=description,
        created_at=pub_date
    ),
    Articles(
        title="Article 2",
        short_description=description,
        full_description=description,
        created_at=pub_date
    ),
    Articles(
        title="Article 3",
        short_description=description,
        full_description=description,
        created_at=pub_date
    )
]

roles = [
    Role(
        id=1,
        name='user',
        permissions=None
    ),
    Role(
        id=2,
        name='admin',
        permissions=None
    )
]

'''
insert into roles values (1, 'user', null), (2, 'admin', null)
'''

