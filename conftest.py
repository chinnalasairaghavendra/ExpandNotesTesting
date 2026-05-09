import os
import pytest
import allure
import requests

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.environment import env
from pages.login_page import LoginPage
from pages.notes_page import NotesPage

from api.auth_api import AuthAPI
from api.notes_api import NotesAPI

from utils.logger import get_logger

from ai.failure_analyzer import (
    FailureAnalyzer
)

logger = get_logger("conftest")

BASE_URL = env.get("base_url")

LOGIN_URL = BASE_URL + "/login"

API_URL = env.get("api_url")

EMAIL = env.get("email")

PASSWORD = env.get("password")


@pytest.fixture
def driver():

    logger.info("Launching Chrome browser")

    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    options.add_experimental_option(
        "prefs",
        prefs
    )

    # Stable Chrome options
    options.add_argument(
        "--disable-save-password-bubble"
    )

    options.add_argument(
        "--disable-notifications"
    )

    options.add_argument(
        "--disable-popup-blocking"
    )

    options.add_argument(
        "--disable-infobars"
    )

    options.add_argument(
        "--disable-extensions"
    )

    options.add_argument(
        "--window-size=1920,1080"
    )

    options.add_argument(
        "--no-sandbox"
    )

    options.add_argument(
        "--disable-dev-shm-usage"
    )

    options.add_argument(
        "--disable-features=TranslateUI"
    )

    options.add_argument(
        "--disable-session-crashed-bubble"
    )

    options.add_argument(
        "--disable-hang-monitor"
    )

    options.add_argument(
        "--disable-sync"
    )

    options.add_argument(
        "--no-first-run"
    )

    options.add_argument(
        "--ignore-certificate-errors"
    )

    options.add_argument(
        "--log-level=3"
    )

    # Detect environment
    inside_docker = os.path.exists(
        "/.dockerenv"
    )

    # Grid URL
    if inside_docker:

        grid_url = (
            "http://host.docker.internal:4444"
        )

    else:

        grid_url = (
            "http://localhost:4444"
        )

    use_grid = False

    # Detect Selenium Grid
    try:

        response = requests.get(
            f"{grid_url}/status",
            timeout=5
        )

        if response.status_code == 200:

            use_grid = True

            logger.info(
                f"Selenium Grid detected at {grid_url}"
            )

    except Exception as e:

        logger.info(
            f"Selenium Grid not detected: {e}"
        )

    # GRID MODE
    if use_grid:

        options.add_argument(
            "--headless=new"
        )

        logger.info(
            "Running tests on Selenium Grid"
        )

        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )

    # LOCAL MODE
    else:

        logger.info(
            "Running tests locally"
        )

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    driver.set_page_load_timeout(60)

    driver.implicitly_wait(5)

    yield driver

    logger.info("Closing browser")

    try:

        driver.quit()

    except Exception as e:

        logger.warning(
            f"Error while quitting driver: {e}"
        )


@pytest.fixture
def login(driver):

    logger.info(
        "Performing login fixture setup"
    )

    login_page = LoginPage(driver)

    login_page.open_login_page(
        LOGIN_URL
    )

    login_page.login(
        EMAIL,
        PASSWORD
    )

    logger.info(
        "Login fixture completed"
    )

    return driver


@pytest.fixture
def notes_page(login):

    return NotesPage(login)


@pytest.fixture
def auth_api():

    api = AuthAPI(API_URL)

    response = api.login(
        EMAIL,
        PASSWORD
    )

    assert response.status_code == 200

    return api


@pytest.fixture
def notes_api(auth_api):

    api = NotesAPI(API_URL)

    api.token = auth_api.token

    return api


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and report.failed
    ):

        driver = item.funcargs.get(
            "driver"
        )

        # Screenshot Capture
        if driver:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            file_name = (
                datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                ) + ".png"
            )

            file_path = (
                f"screenshots/{file_name}"
            )

            driver.save_screenshot(
                file_path
            )

            allure.attach.file(
                file_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # AI Failure Analysis
        try:

            error_message = str(
                report.longrepr
            )

            analysis = (
                FailureAnalyzer.analyze(
                    error_message
                )
            )

            print(
                "\n===== AI FAILURE ANALYSIS =====\n"
            )

            print(analysis)

            allure.attach(
                analysis,
                name="AI Failure Analysis",
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:

            print(
                f"AI analysis failed: {e}"
            )