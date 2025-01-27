import random
from datetime import date

from src.books.models import Books, Themes
from src.reviews.models import Reviews
from src.articles.models import Articles
from src.auth.models import Role
from misc.utils import convert_docx_to_html


read_times = [3, 5, 7, 10, 15]
docx_file = "misc/docx_files/test.docx"
review_title = "Very cute story and great storylines"
pub_date = date(2023, 12, 17)
language = "English"
min_age, max_age = 3, 6
series = "Our Emotions are Our Friends"
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
    "My Friend Joy": "MyFriendJoy.jpg",
    "My Friend Sadness": "MyFriendSadness.jpg",
    "My Friend Anger": "MyFriendAnger.jpg",
    "My Friend Fear": "MyFriendFear.jpg",
    "My Friend Envy": "MyFriendEnvy.png",
    "My Friend Love": "MyFriendLove.png",
    "My Friend Jealousy": "MyFriendJealousy.png",
    "My Friend Resentment": "MyFriendResentment.png",
    "My Friend Shame": "MyFriendShame.png",
    "My Friend Guilt": "MyFriendGuilt.png",
    "My Friend Loneliness": "MyFriendLoneliness.png",
    "My Friend Shyness": "MyFriendShyness.png",
    "My Friend Indifference": "MyFriendIndifference.png",
    "My Friend Helplessness": "MyFriendHelplessness.png",
    "My Friend Boredom": "MyFriendBoredom.png"
}
article_image_map = {
    "Example article 1 title": "NoImage.jpg",
    "Example article 2 title": "NoImage.jpg",
    "Example article 3 title": "NoImage.jpg",
    "Example article 4 title": "NoImage.jpg",
    "Example article 5 title": "NoImage.jpg",
    "Example article 6 title": "NoImage.jpg",
    "Example article 7 title": "NoImage.jpg",
    "Example article 8 title": "NoImage.jpg",
    "Example article 9 title": "NoImage.jpg",
    "Example article 10 title": "NoImage.jpg",
    "Example article 11 title": "NoImage.jpg"
}
example_themes_info = {
    "names": [
        'Child\'s Joy',
        'Child\'s Sadness',
        'Child\'s Anger',
        'Child\'s Fear',
        'Child\'s Envy',
        'Child\'s Love',
        'Child\'s Jealousy',
        'Child\'s Resentment',
        'Child\'s Shame',
        'Child\'s Guilt',
        'Child\'s Loneliness',
        'Child\'s Shyness',
        'Child\'s Indifference',
        'Child\'s Helplessness',
        'Child\'s Boredom'
    ]
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
    "pub_date": pub_date,
    "docx_file": docx_file
}

example_reviews_info = {
    "n_reviews": 50,
    "n_books": len(book_image_map),
    "n_users": 10,
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
    count = 1
    for title, image in book_image.items():
        books.append(
            Books(
                series=series,
                theme=count,
                title=title,
                cover=image,
                summary=description,
                pub_date=pub_date,
                author=author,
                pages=random.randint(28, 38),
                language=language,
                min_age=min_age,
                max_age=max_age,
                amazon_link=amazon_link,
                aloud_link=aloud_link,
                active=True
            )
        )
        count += 1
    return books


def generate_example_articles_list(
    article_image: dict,
    description: str,
    pub_date,
    docx_file: str
):
    converted_text = convert_docx_to_html(docx_file)
    articles = []
    for title, image in article_image.items():
        articles.append(
            Articles(
                theme=random.randint(1, 15),
                title=title,
                summary=description,
                text=converted_text["html_content"],
                created_at=pub_date,
                preview=image,
                read_time=random.choice(read_times),
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


def generate_example_themes_list(names: list[str]):
    themes = []
    for name in names:
        themes.append(Themes(name=name))
    return themes


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
