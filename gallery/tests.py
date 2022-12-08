from .models import Gallery, GalleryImage


def test_gallery_slug_appears_in_url():
    slug_value = "slug_value"
    sut = Gallery()
    sut.slug = slug_value

    result = sut.get_absolute_url()

    slug_value in result


def test_gallery_image_slug_appears_in_url():
    slug_value = "slug-value"

    gallery = Gallery()
    gallery.slug = "dont-care"

    sut = GalleryImage()

    sut.slug = slug_value
    sut.gallery = gallery

    result = sut.get_absolute_url()

    slug_value in result


def test_gallery_image_gallery_slug_appears_in_url():
    gallery_slug = "gallery-slug"

    gallery = Gallery()
    gallery.slug = gallery_slug

    sut = GalleryImage()

    sut.slug = "dont-care"
    sut.gallery = gallery

    result = sut.get_absolute_url()

    gallery_slug in result
