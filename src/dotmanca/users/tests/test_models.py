def test__str__(create_user):
    user = create_user(username="testuser", email=None)
    assert user.__str__() == "testuser"


def test_get_absolute_url(create_user):
    user = create_user(username="testuser", email=None)
    assert user.get_absolute_url() == "/users/testuser/"
