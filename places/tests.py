from django.test import TestCase

from .models import Place


class PlaceGetAbsoluteUrl(TestCase):
    def test_slug_appears_in_url(self):
        slug_value = "slug_value"
        sut = Place()
        sut.slug = slug_value

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)
