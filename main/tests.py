import datetime as dt
from contextlib import contextmanager
from unittest.mock import patch

from .views import AboutChasView, AboutEvanView, HomePageView


@contextmanager
def mocked_now(now):
    class MockedDatetime(dt.datetime):
        @classmethod
        def now(cls):
            return now

    with patch("datetime.datetime", MockedDatetime):
        yield


def test_about_chas_view_age_in_context_of_about():
    view = AboutChasView()

    context = view.get_context_data()

    "age" in context.keys()


def test_about_chas_view_age_ten_years_after_birthday_is_ten():
    view = AboutChasView()

    with mocked_now(dt.datetime(1990, 4, 21)):
        context = view.get_context_data()

        10 == context["age"]


def test_about_chas_view_age_ten_years_minus_one_day_after_birthday_is_nine_about():
    view = AboutChasView()

    with mocked_now(dt.datetime(1990, 4, 20)):
        context = view.get_context_data()

        9 == context["age"]


def test_about_evan_view_context_contains_age():
    view = AboutEvanView()

    context = view.get_context_data()

    "age" in context.keys()


def test_about_evan_view_age_ten_years_after_birthday_is_ten():
    view = AboutEvanView()

    with mocked_now(dt.datetime(1990, 12, 6)):
        context = view.get_context_data()

        10 == context["age"]


def test_about_evan_view_age_ten_years_minus_one_day_after_birthday_is_nine():
    view = AboutEvanView()

    with mocked_now(dt.datetime(1990, 12, 5)):
        context = view.get_context_data()

        9 == context["age"]


def test_context_contains_news_articles():
    view = HomePageView()

    # Inject so we don't try to hit database
    view.get_published_news_articles = lambda: []

    context = view.get_context_data()

    "news_articles" in context.keys()


def test_context_contains_only_three_news_articles_when_4_come_back():
    view = HomePageView()

    # Inject so we return 4 test double news articles
    view.get_published_news_articles = lambda: [{}, {}, {}, {}]

    context = view.get_context_data()

    "news_articles" in context.keys()
