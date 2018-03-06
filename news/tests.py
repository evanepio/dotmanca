import datetime

from django.test import TestCase

from .models import NewsArticle


class TestNewsArticleGetAbsoluteUrl(TestCase):
    def test_date_appears_in_url(self):
        sut = NewsArticle()
        sut.published_date = datetime.date(2018, 1, 6)
        sut.slug = "dont-care"

        result = sut.get_absolute_url()

        self.assertTrue("2018/01/06" in result)

    def test_slug_appears_in_url(self):
        slug_value = "my-slug-value"
        sut = NewsArticle()
        sut.published_date = datetime.date.today()
        sut.slug = slug_value

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)
