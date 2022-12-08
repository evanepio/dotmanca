from ..views import UserRedirectView, UserUpdateView


def test_user_view_get_redirect_url(create_request_with_user):
    view = UserRedirectView()
    view.request = create_request_with_user("/fake-url", username="testuser")
    # Expect: '/users/testuser/', as that is the default username for
    #   self.make_user()
    assert view.get_redirect_url() == "/users/testuser/"


def test_user_view_get_success_url(create_request_with_user):
    view = UserUpdateView()
    view.request = create_request_with_user("/fake-url", username="testuser")
    # Expect: '/users/testuser/', as that is the default username for
    #   self.make_user()
    assert view.get_success_url(), "/users/testuser/"


def test_user_view_get_object(create_request_with_user):
    view = UserUpdateView()
    view.request = create_request_with_user("/fake-url", username="testuser")
    # Expect: self.user, as that is the request's user object
    assert view.get_object().username == "testuser"
