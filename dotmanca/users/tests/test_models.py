from django.test import TestCase

from ..models import User


class TestUser(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             email=None,
                                             password='notalamodespassword')

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )
