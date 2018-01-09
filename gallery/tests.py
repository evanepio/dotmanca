from django.test import TestCase

from .models import Gallery, GalleryImage


class GalleryGetAbsoluteUrl(TestCase):
    def test_slug_appears_in_url(self):
        slug_value = "slug_value"
        sut = Gallery()
        sut.slug = slug_value

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)


class GalleryImageGetAbsoluteUrl(TestCase):
    def test_slug_appears_in_url(self):
        slug_value = "slug-value"

        gallery = Gallery()
        gallery.slug = "dont-care"

        sut = GalleryImage()

        sut.slug = slug_value
        sut.gallery = gallery

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)

    def test_gallery_slug_appears_in_url(self):
        gallery_slug = "gallery-slug"

        gallery = Gallery()
        gallery.slug = gallery_slug

        sut = GalleryImage()

        sut.slug = "dont-care"
        sut.gallery = gallery

        result = sut.get_absolute_url()

        self.assertTrue(gallery_slug in result)
