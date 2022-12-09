import datetime as dt

from .views import AboutChasView, AboutEvanView, HomePageView


def test_about_chas_view_age_in_context_of_about():
    view = AboutChasView()

    context = view.get_context_data()

    assert "age" in context.keys()


def test_about_chas_view_age_ten_years_after_birthday_is_ten(monkeypatch):
    monkeypatch.setattr("main.views.get_today", lambda: dt.datetime(1990, 4, 21))
    view = AboutChasView()
    context = view.get_context_data()

    assert 10 == context["age"]


def test_about_chas_view_age_ten_years_minus_one_day_after_birthday_is_nine_about(
    monkeypatch,
):
    monkeypatch.setattr("main.views.get_today", lambda: dt.datetime(1990, 4, 20))
    view = AboutChasView()
    context = view.get_context_data()

    assert 9 == context["age"]


def test_about_evan_view_context_contains_age():
    view = AboutEvanView()

    context = view.get_context_data()

    assert "age" in context.keys()


def test_about_evan_view_age_ten_years_after_birthday_is_ten(monkeypatch):
    monkeypatch.setattr("main.views.get_today", lambda: dt.datetime(1990, 12, 6))
    view = AboutEvanView()
    context = view.get_context_data()

    assert 10 == context["age"]


def test_about_evan_view_age_ten_years_minus_one_day_after_birthday_is_nine(
    monkeypatch,
):
    monkeypatch.setattr("main.views.get_today", lambda: dt.datetime(1990, 12, 5))
    view = AboutEvanView()
    context = view.get_context_data()

    assert 9 == context["age"]


def test_context_contains_news_articles():
    view = HomePageView()

    # Inject so we don't try to hit database
    view.get_published_news_articles = lambda: []

    context = view.get_context_data()

    assert "news_articles" in context.keys()


def test_context_contains_only_three_news_articles_when_4_come_back():
    view = HomePageView()

    # Inject so we return 4 test double news articles
    view.get_published_news_articles = lambda: [{}, {}, {}, {}]

    context = view.get_context_data()

    assert "news_articles" in context.keys()
