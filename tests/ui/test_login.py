import pytest
import allure
from pages.login_page import LoginPage
from config.environment import env

BASE_URL = env.get("base_url")+"/login"
EMAIL=env.get("email")
PASSWORD=env.get("password")

@allure.epic("UI Automation")
@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Validate Successful Login")
@pytest.mark.ui
def test_valid_login(driver):
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
        login_page.open_login_page(BASE_URL)
    with allure.step("Perform login"):
        login_page.login(
            EMAIL,
            PASSWORD
        )
    with allure.step("Validate login success"):
        assert login_page.is_login_successful()


@pytest.mark.parametrize(
    "email,password,expected_error",
    [
        ("wrong@test.com", "Password123", "incorrect"),
        ("", "Password123", "email address is required"),
        ("", "", "email address is required")
    ]
)
@pytest.mark.ui
def test_invalid_login(driver, email, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open_login_page(BASE_URL)
    login_page.login(email, password)
    actual_error = login_page.get_error_message().lower()
    assert expected_error in actual_error