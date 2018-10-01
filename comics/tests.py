from django.test import TestCase


from .models import Issue, Arc


class IssueGetAbsoluteUrl(TestCase):
    def test_slug_appears_in_url(self):
        slug_value = "slug_value"

        arc = Arc()
        arc.slug = "dont-care"

        sut = Issue()
        sut.slug = slug_value
        sut.arc = arc

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)

    def test_arc_slug_appears_in_url(self):
        arc_slug = "arc-slug"

        arc = Arc()
        arc.slug = arc_slug

        sut = Issue()

        sut.slug = "dont-care"
        sut.arc = arc

        result = sut.get_absolute_url()

        self.assertTrue(arc_slug in result)
