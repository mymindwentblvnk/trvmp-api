import json

import pytest
from assertpy import assert_that

from starlette.testclient import TestClient

from app.main import app
from app.database import engine, Base

client = TestClient(app)


@pytest.fixture(autouse=True)
def resource():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


class TestUsersEnpoint(object):

    def test_user_creation(self):
        user_data_input = {
            'email': 'a_email',
            'password': 'a_password'
        }

        response = client.post('/users/', json=user_data_input)

        user_data_actual = json.loads(response.text)
        user_data_expected = {
            'user_id': 1,
            'email': 'a_email',
            'name': None,
            'is_active': True,
        }

        assert_that(response.status_code).is_equal_to(200)
        assert_that(user_data_actual).is_equal_to(user_data_expected)
