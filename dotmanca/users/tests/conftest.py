import uuid

import pytest

from ..models import User


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        kwargs["password"] = "DigiSuperCowNinja123!"
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return User.objects.create_user(**kwargs)

    return make_user
