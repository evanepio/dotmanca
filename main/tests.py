import datetime

from django.test import TestCase

from .views import AboutChasView, AboutEvanView, HomePageView


class TestAboutChasViewGetContextData(TestCase):
    def test_context_contains_age(self):
        view = AboutChasView()

        context = view.get_context_data()

        self.assertTrue('age' in context.keys())

    def test_age_ten_years_after_birthday_is_ten(self):
        view = AboutChasView()

        # Inject the method used to get current date
        view.get_todays_date = lambda: datetime.date(1990, 4, 21)

        context = view.get_context_data()

        self.assertEquals(10, context['age'])

    def test_age_ten_years_minus_one_day_after_birthday_is_nine(self):
        view = AboutChasView()

        # Inject the method used to get current date
        view.get_todays_date = lambda: datetime.date(1990, 4, 20)

        context = view.get_context_data()

        self.assertEquals(9, context['age'])


class TestAboutEvanViewGetContextData(TestCase):
    def test_context_contains_age(self):
        view = AboutEvanView()

        context = view.get_context_data()

        self.assertTrue('age' in context.keys())

    def test_age_ten_years_after_birthday_is_ten(self):
        view = AboutEvanView()

        # Inject the method used to get current date
        view.get_todays_date = lambda: datetime.date(1990, 12, 6)

        context = view.get_context_data()

        self.assertEquals(10, context['age'])

    def test_age_ten_years_minus_one_day_after_birthday_is_nine(self):
        view = AboutEvanView()

        # Inject the method used to get current date
        view.get_todays_date = lambda: datetime.date(1990, 12, 5)

        context = view.get_context_data()

        self.assertEquals(9, context['age'])


class TestHomePageViewGetContextData(TestCase):
    def test_context_contains_news_articles(self):
        view = HomePageView()

        # Inject so we don't try to hit database
        view.get_published_news_articles = lambda: []

        context = view.get_context_data()

        self.assertTrue('news_articles' in context.keys())

    def test_context_contains_only_three_news_articles_when_4_come_back(self):
        view = HomePageView()

        # Inject so we return 4 test double news articles
        view.get_published_news_articles = lambda: [{}, {}, {}, {}]

        context = view.get_context_data()

        self.assertTrue('news_articles' in context.keys())
