from .models import Character, Team


def test_character_slug_appears_in_url():
    slug_value = "slug-value"

    team = Team()
    team.slug = "dont-care"

    sut = Character()

    sut.slug = slug_value
    sut.team = team

    result = sut.get_absolute_url()

    slug_value in result


def test_character_team_slug_appears_in_url():
    team_slug = "team-slug"

    team = Team()
    team.slug = team_slug

    sut = Character()

    sut.slug = "dont-care"
    sut.team = team

    result = sut.get_absolute_url()

    team_slug in result
