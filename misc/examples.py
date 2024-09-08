from src.books.models import Books
from src.articles.models import Articles
from src.auth.models import Role

from datetime import date


example_books = [
    Books(
        title="My friend Joy",
        series="Our Emotions - Our Friends",
        short_description="Description 1",
        full_description="Description 1",
        pub_date=date(2023, 12, 17),
        author="Yassya Lil",
        image="JoyCover.jpg"
    ),
    Books(
        title="My friend Sadness",
        series="Our Emotions - Our Friends",
        short_description="Description 2",
        full_description="Description 1",
        pub_date=date(2024, 4, 25),
        author="Yassya Lil",
        image="SadnessCover.jpg"
    ),
    Books(
        title="My friend Anger",
        series="Our Emotions - Our Friends",
        short_description="Description 3",
        full_description="Description 1",
        pub_date=date(2024, 4, 1),
        author="Yassya Lil",
        image="AngerCover.jpg"
    ),
    Books(
        title="My friend Fear",
        series="Our Emotions - Our Friends",
        short_description="Description 4",
        full_description="Description 1",
        pub_date=date(2024, 2, 2),
        author="Yassya Lil",
        image="FearCover.jpg"
    ),
    Books(
        title="My friend Envy",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="EnvyCover.png"
    ),
    Books(
        title="My friend Love",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="LoveCover.png"
    ),
    Books(
        title="My friend Jealousy",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="JealousyCover.png"
    ),
    Books(
        title="My friend Resentment",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="ResentmentCover.png"
    ),
    Books(
        title="My friend Shame",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="ShameCover.png"
    ),
    Books(
        title="My friend Guilt",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="GuiltCover.png"
    ),
    Books(
        title="My friend Loneliness",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="LonelinessCover.png"
    ),
    Books(
        title="My friend Shyness",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="ShynessCover.png"
    ),
    Books(
        title="My friend Indifference",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="IndifferenceCover.png"
    ),
    Books(
        title="My friend Helplessness",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="HelplessnessCover.png"
    ),
    Books(
        title="My friend Boredom",
        series="Our Emotions - Our Friends",
        short_description="Description 5",
        full_description="Description 1",
        pub_date=date(2024, 3, 14),
        author="Yassya Lil",
        image="BoredomCover.png"
    )
]

example_articles = [
    Articles(
        title="Article 1",
        short_description="Article description 1",
        full_description="Article description 1",
        created_at=date(2024, 1, 10)
    ),
    Articles(
        title="Article 2",
        short_description="Article description 2",
        full_description="Article description 1",
        created_at=date(2024, 3, 15)
    ),
    Articles(
        title="Article 3",
        short_description="Article description 3",
        full_description="Article description 1",
        created_at=date(2024, 5, 20)
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

