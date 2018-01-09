from django.test import TestCase

from .models import Character, Team

class TeamGetAbsoluteUrl(TestCase):
    def test_slug_appears_in_url(self):
        slug_value = "slug-value"

        team = Team()
        team.slug = "dont-care"

        sut = Character()

        sut.slug = slug_value
        sut.team = team

        result = sut.get_absolute_url()

        self.assertTrue(slug_value in result)

    def test_team_slug_appears_in_url(self):
        team_slug = "team-slug"

        team = Team()
        team.slug = team_slug

        sut = Character()

        sut.slug = "dont-care"
        sut.team = team

        result = sut.get_absolute_url()

        self.assertTrue(team_slug in result)
