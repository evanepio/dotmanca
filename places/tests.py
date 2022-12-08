from .models import Place


def test_place_slug_appears_in_url():
    slug_value = "slug_value"
    sut = Place()
    sut.slug = slug_value

    result = sut.get_absolute_url()

    slug_value in result
