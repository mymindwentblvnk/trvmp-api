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


class TestTokenEndpoint(object):

    def test_user_login(self):
        input_data = {
            "username": "johndoe",
            "password": "secret",
        }
        response = client.post("/token", data=input_data)
        assert response.status_code == 200
        assert response.json() == {"access_token": "johndoe", "token_type": "bearer"}
