import datetime

from .models import NewsArticle


def test_news_article_date_appears_in_url():
    sut = NewsArticle()
    sut.published_date = datetime.date(2018, 1, 6)
    sut.slug = "dont-care"

    result = sut.get_absolute_url()

    "2018/01/06" in result


def test_news_article_slug_appears_in_url():
    slug_value = "my-slug-value"
    sut = NewsArticle()
    sut.published_date = datetime.date.today()
    sut.slug = slug_value

    result = sut.get_absolute_url()

    slug_value in result
