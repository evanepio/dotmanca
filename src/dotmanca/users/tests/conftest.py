import uuid

import pytest
from django.test import RequestFactory

from ..models import User


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        kwargs["password"] = "DigiSuperCowNinja123!"
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return User.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def create_request_with_user(create_user):
    def make_request(url, **kwargs):
        user = create_user(**kwargs)
        request = RequestFactory().get(url)
        request.user = user
        return request

    return make_request
