import random

from src.books.models import Books, Reviews
from src.articles.models import Articles
from src.auth.models import Role

from datetime import date


pub_date = date(2023, 12, 17)
language = "English"
min_age, max_age = 3, 6
series = "Our Emotions - Our Friends"
author = "Yassya Lil"
description = """
Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, dolor eget aliquet auctor, 
dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. Aliquam vitae leo tincidunt, 
convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex pellentesque rhoncus et quis felis. 
Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.
"""
amazon_link = 'https://www.amazon.com/Friend-Anger-Our-Emotions-Friends/dp/B0C1J1H9MM/ref=sr_1_1?crid=XONPX6TL9F9U&dib=eyJ2IjoiMSJ9.Au1UgCc2IzRqX61k25GpwA.gO2PsLVmjAp6nuOLokGEBMECjoUwdCyvnd99QhpFb-A&dib_tag=se&keywords=yassya+lil+anger&qid=1726409665&s=books&sprefix=yassya+lil+anger%2Cstripbooks-intl-ship%2C169&sr=1-1'
aloud_link = 'https://www.youtube.com/embed/jMCXFGdSbH4'


example_books = [
    Books(
        title="My Friend Joy",
        image="JoyCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Sadness",
        image="SadnessCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Anger",
        image="AngerCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Fear",
        image="FearCover.jpg",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Envy",
        image="EnvyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Love",
        image="LoveCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Jealousy",
        image="JealousyCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Resentment",
        image="ResentmentCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Shame",
        image="ShameCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Guilt",
        image="GuiltCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Loneliness",
        image="LonelinessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Shyness",
        image="ShynessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Indifference",
        image="IndifferenceCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Helplessness",
        image="HelplessnessCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
    ),
    Books(
        title="My Friend Boredom",
        image="BoredomCover.png",
        series=series,
        short_description=description,
        full_description=description,
        pub_date=pub_date,
        author=author,
        min_age=min_age,
        max_age=max_age,
        pages=random.randint(28, 38),
        language=language,
        reviews_count=random.randint(50, 500),
        ratings_count=random.randint(50, 500),
        mean_rating=round(random.uniform(4.6, 5.0), 1),
        amazon_link=amazon_link,
        aloud_link=aloud_link
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

example_reviews = [
    Reviews(
        book=1,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    ),
    Reviews(
        book=2,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    ),
    Reviews(
        book=3,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    ),
    Reviews(
        book=4,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    ),
    Reviews(
        book=5,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    ),
    Reviews(
        book=6,
        reviewer=1,
        rating=5,
        title="Great story and great purchase",
        text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
        dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
        Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
        pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
    )
]

'''
insert into roles values (1, 'user', null), (2, 'admin', null)
'''

