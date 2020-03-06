import pytest
from assertpy import assert_that
from starlette.testclient import TestClient

from app.database import engine, Base
from app.main import app
from tests.fixtures import TestClientRequestsMixin


@pytest.fixture(autouse=True)
def resource():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


class TestTokenEndpoint(TestClientRequestsMixin):

    client = TestClient(app)

    def create_user(self, username, password, email):
        user_data = {
            'username': username,
            'password': password,
            'email': email,
        }
        return self.post('/users', json=user_data)

    def test_user_login_returns_200(self):
        username = 'the_username'
        password = 'the_password'
        email = 'a_email@trvmp.io'

        # Create user first
        self.create_user(username=username, password=password, email=email)

        # Then try to log in
        response = self.post(url="/token", data={'username': username, 'password': password})
        assert_that(response.status_code).is_equal_to(200)

        response_json = response.json()
        assert_that(response_json).contains_key('access_token')
        assert_that(response_json).contains_key('token_type')

        access_token = response.json()['access_token']
        token_type = response.json()['token_type']
        assert_that(access_token).is_not_none()
        assert_that(token_type).is_equal_to('bearer')
