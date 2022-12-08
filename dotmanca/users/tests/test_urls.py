from django.urls import resolve, reverse


def test_user_url_list_reverse():
    """users:list should reverse to /users/."""
    assert reverse("users:list"), "/users/"


def test_user_url_list_resolve():
    """/users/ should resolve to users:list."""
    assert resolve("/users/").view_name, "users:list"


def test_user_url_redirect_reverse():
    """users:redirect should reverse to /users/~redirect/."""
    assert reverse("users:redirect"), "/users/~redirect/"


def test_user_url_redirect_resolve():
    """/users/~redirect/ should resolve to users:redirect."""
    assert resolve("/users/~redirect/").view_name, "users:redirect"


def test_user_url_detail_reverse():
    """users:detail should reverse to /users/testuser/."""
    assert reverse("users:detail", kwargs={"username": "testuser"}), "/users/testuser/"


def test_user_url_detail_resolve():
    """/users/testuser/ should resolve to users:detail."""
    assert resolve("/users/testuser/").view_name, "users:detail"


def test_user_url_update_reverse():
    """users:update should reverse to /users/~update/."""
    assert reverse("users:update"), "/users/~update/"


def test_user_url_update_resolve():
    """/users/~update/ should resolve to users:update."""
    assert resolve("/users/~update/").view_name, "users:update"
