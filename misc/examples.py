import random

from src.books.models import Books
from src.reviews.models import Reviews
from src.articles.models import Articles
from src.auth.models import Role

from datetime import date


review_title = "Very cute story and great storylines"
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
book_image_map = {
    "My Friend Joy": "JoyCover.jpg",
    "My Friend Sadness": "SadnessCover.jpg",
    "My Friend Anger": "AngerCover.jpg",
    "My Friend Fear": "FearCover.jpg",
    "My Friend Envy": "EnvyCover.png",
    "My Friend Love": "LoveCover.png",
    "My Friend Jealousy": "JealousyCover.png",
    "My Friend Resentment": "ResentmentCover.png",
    "My Friend Shame": "ShameCover.png",
    "My Friend Guilt": "GuiltCover.png",
    "My Friend Loneliness": "LonelinessCover.png",
    "My Friend Shyness": "ShynessCover.png",
    "My Friend Indifference": "IndifferenceCover.png",
    "My Friend Helplessness": "HelplessnessCover.png",
    "My Friend Boredom": "BoredomCover.png"
}
article_image_map = {
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg",
    "Example article title": "NoImage.jpg"
}


example_books_info = {
    "book_image": book_image_map,
    "series": series,
    "description": description,
    "pub_date": pub_date,
    "author": author,
    "min_age": min_age,
    "max_age": max_age,
    "language": language,
    "amazon_link": amazon_link,
    "aloud_link": aloud_link
}

example_articles_info = {
    "article_image": article_image_map,
    "description": description,
    "pub_date": pub_date
}

example_reviews_info = {
    "n_reviews": 50,
    "n_books": len(book_image_map),
    "n_users": 5,
    "title": review_title,
    "text": description
}


def generate_example_books_list(
    book_image: dict,
    series: str,
    description: str,
    pub_date,
    author: str,
    min_age: int,
    max_age: int,
    language: str,
    amazon_link: str,
    aloud_link: str
):
    books = []
    for title, image in book_image.items():
        books.append(
            Books(
                title=title,
                image=image,
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
                aloud_link=aloud_link,
                active=True
            )
        )
    return books


def generate_example_articles_list(
    article_image: dict,
    description: str,
    pub_date
):
    articles = []
    for title, image in article_image.items():
        articles.append(
            Articles(
                title=title,
                summary=description,
                text=description,
                created_at=pub_date,
                preview=image,
                active=True
            )
        )
    return articles


def generate_example_reviews_list(
    n_reviews: int,
    n_books: int,
    n_users: int,
    title: str,
    text: str
):
    reviews = []
    for _ in range(n_reviews):
        reviews.append(
            Reviews(
                book_id = random.randint(1, n_books),
                user_id = random.randint(1, n_users),
                rating = random.randint(1, 5),
                title = title,
                text= text
            )
        )
    return reviews


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



# example_books = [
#     Books(
#         title="My Friend Joy",
#         image="JoyCover.jpg",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Sadness",
#         image="SadnessCover.jpg",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Anger",
#         image="AngerCover.jpg",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Fear",
#         image="FearCover.jpg",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Envy",
#         image="EnvyCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Love",
#         image="LoveCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Jealousy",
#         image="JealousyCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Resentment",
#         image="ResentmentCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Shame",
#         image="ShameCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Guilt",
#         image="GuiltCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Loneliness",
#         image="LonelinessCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Shyness",
#         image="ShynessCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Indifference",
#         image="IndifferenceCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Helplessness",
#         image="HelplessnessCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     ),
#     Books(
#         title="My Friend Boredom",
#         image="BoredomCover.png",
#         series=series,
#         short_description=description,
#         full_description=description,
#         pub_date=pub_date,
#         author=author,
#         min_age=min_age,
#         max_age=max_age,
#         pages=random.randint(28, 38),
#         language=language,
#         reviews_count=random.randint(50, 500),
#         ratings_count=random.randint(50, 500),
#         mean_rating=round(random.uniform(4.6, 5.0), 1),
#         amazon_link=amazon_link,
#         aloud_link=aloud_link,
#         active=True
#     )
# ]
# 
# example_articles = [
#     Articles(
#         title="Article 1",
#         summary=description,
#         text=description,
#         created_at=pub_date,
#         preview='NoImage.jpg',
#         active=True
#     ),
#     Articles(
#         title="Article 2",
#         summary=description,
#         text=description,
#         created_at=pub_date,
#         preview='NoImage.jpg',
#         active=True
#     ),
#     Articles(
#         title="Article 3",
#         summary=description,
#         text=description,
#         created_at=pub_date,
#         preview='NoImage.jpg',
#         active=True
#     )
# ]
# 
# example_reviews = [
#     Reviews(
#         book_id=1,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     ),
#     Reviews(
#         book_id=2,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     ),
#     Reviews(
#         book_id=3,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     ),
#     Reviews(
#         book_id=4,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     ),
#     Reviews(
#         book_id=5,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     ),
#     Reviews(
#         book_id=6,
#         user_id=1,
#         rating=5,
#         title="Great story and great purchase",
#         text="Phasellus ut lorem eu sapien placerat ornare quis ac purus. Aenean consectetur, \
#         dolor eget aliquet auctor, dolor leo laoreet lorem, eu blandit justo nisi eu arcu. Donec et nulla dolor. \
#         Aliquam vitae leo tincidunt, convallis lectus sit amet, convallis felis. Donec sit amet lectus a ex \
#         pellentesque rhoncus et quis felis. Mauris enim justo, congue congue rutrum nec, rhoncus vitae quam.",
#     )
# ]


