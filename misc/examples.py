from src.books.models import Books
from src.articles.models import Articles
from src.auth.models import Role

from datetime import date


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
Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam. Donec imperdiet enim odio, sed posuere 
nibh vulputate vel. Vivamus facilisis in risus nec auctor. Morbi dui diam, efficitur sit amet vulputate 
sit amet, tempus in dolor. Maecenas ullamcorper est et egestas posuere.
"""


example_books = [
    Books(
        title="My friend Joy",
        image="JoyCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Sadness",
        image="SadnessCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Anger",
        image="AngerCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Fear",
        image="FearCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Envy",
        image="EnvyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Love",
        image="LoveCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Jealousy",
        image="JealousyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Resentment",
        image="ResentmentCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Shame",
        image="ShameCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Guilt",
        image="GuiltCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Loneliness",
        image="LonelinessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Shyness",
        image="ShynessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Indifference",
        image="IndifferenceCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Helplessness",
        image="HelplessnessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
    ),
    Books(
        title="My friend Boredom",
        image="BoredomCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        age=age,
        pages=pages,
        language=language
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

