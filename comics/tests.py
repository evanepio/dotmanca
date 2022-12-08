from .models import Arc, Issue


def test_issue_slug_appears_in_url():
    slug_value = "slug_value"

    arc = Arc()
    arc.slug = "dont-care"

    sut = Issue()
    sut.slug = slug_value
    sut.arc = arc

    result = sut.get_absolute_url()

    slug_value in result


def test_issue_arc_slug_appears_in_url():
    arc_slug = "arc-slug"

    arc = Arc()
    arc.slug = arc_slug

    sut = Issue()

    sut.slug = "dont-care"
    sut.arc = arc

    result = sut.get_absolute_url()

    arc_slug in result
