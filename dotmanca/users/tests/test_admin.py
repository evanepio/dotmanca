import pytest

from ..admin import MyUserCreationForm


@pytest.mark.django_db
def test_clean_username_success():
    # Instantiate the form with a new username
    form = MyUserCreationForm(
        {
            "username": "alamode",
            "password1": "7jefB#f@Cc7YJB]2v",
            "password2": "7jefB#f@Cc7YJB]2v",
        }
    )
    # Run is_valid() to trigger the validation
    valid = form.is_valid()
    assert valid

    # Run the actual clean_username method
    username = form.clean_username()
    assert "alamode" == username


@pytest.mark.django_db
def test_clean_username_false(create_user):
    user = create_user(username="some_user")
    # Instantiate the form with the same username as self.user
    form = MyUserCreationForm(
        {
            "username": user.username,
            "password1": "notalamodespassword",
            "password2": "notalamodespassword",
        }
    )
    # Run is_valid() to trigger the validation, which is going to fail
    # because the username is already taken
    valid = form.is_valid()
    assert not valid

    # The form.errors dict should contain a single error called 'username'
    assert len(form.errors) == 1
    assert "username" in form.errors
