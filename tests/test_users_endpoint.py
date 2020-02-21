import json

from assertpy import assert_that
from mock import patch

from starlette.testclient import TestClient

from app.main import app as trvmp_api


client = TestClient(trvmp_api)


class TestUsersEnpoint(object):

    @patch('app.database.DATABASE_URL', 'sqlite:///asdf.db')
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
