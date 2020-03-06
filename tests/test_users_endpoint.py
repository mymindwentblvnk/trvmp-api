import json

import pytest
from assertpy import assert_that

from starlette.testclient import TestClient

from app.main import app
from app.database import engine, Base
from tests.fixtures import TestClientRequestsMixin


@pytest.fixture(autouse=True)
def resource():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


class TestUsersEndpoint(TestClientRequestsMixin):

    client = TestClient(app)

    def test_user_creation(self):
        user_data_input = {
            'email': 'a_email',
            'username': 'a_username',
            'password': 'a_password'
        }
        response = self.post(url='/users', json=user_data_input)

        user_data_actual = json.loads(response.text)
        user_data_expected = {
            'user_id': 1,
            'username': 'a_username',
            'email': 'a_email',
            'disabled': False,
        }
        assert_that(response.status_code).is_equal_to(200)
        assert_that(user_data_actual).is_equal_to(user_data_expected)

    def test_user_creation_with_same_email_returns_400(self):
        user_data_input = {
            'email': 'same_email',
            'username': 'a_username',
            'password': 'a_password'
        }
        response = self.post(url='/users', json=user_data_input)
        assert_that(response.status_code).is_equal_to(200)

        same_user_data_input = {
            'email': 'same_email',
            'username': 'a_username',
            'password': 'a_password'
        }
        response = self.post(url='/users', json=same_user_data_input)
        assert_that(response.status_code).is_equal_to(400)
