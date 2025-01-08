import statistics

from src.reviews.models import Reviews


async def get_reviews_statistics(reviews: list[Reviews]):
    ratings = [review.rating for review in reviews]
    reviews_texts = [review.text for review in reviews]
    if ratings:
        average_rating = statistics.mean(ratings)
    else:
        average_rating = 0
    ratings_count = len(ratings)
    reviews_count = len(reviews_texts)
        
    return {
        "average_rating": average_rating,
        "ratings_count": ratings_count,
        "reviews_count": reviews_count
    }
