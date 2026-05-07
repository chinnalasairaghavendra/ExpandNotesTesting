from api.auth_api import AuthAPI
from config.environment import env

API_URL = env.get("api_url")
EMAIL=env.get("email")
PASSWORD=env.get("password")


def test_valid_api_login():
    api = AuthAPI(API_URL)
    response = api.login(
        EMAIL,
        PASSWORD
    )
    assert response.status_code == 200
    assert "token" in response.json()["data"]


def test_invalid_api_login():
    api = AuthAPI(API_URL)
    response = api.login(
        "wrong@test.com",
        "wrongpass"
    )
    assert response.status_code == 401


def test_empty_credentials():
    api = AuthAPI(API_URL)
    response = api.login("", "")
    assert response.status_code in [400, 401]