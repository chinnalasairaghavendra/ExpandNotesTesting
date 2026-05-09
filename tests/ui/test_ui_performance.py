from utils.performance_utils import (
    PerformanceUtils
)

from config.environment import env


LOGIN_URL = (
    env.get("base_url")
) + "/login"


def test_ui_load_performance(driver):

    driver.get(LOGIN_URL)

    load_time = (
        PerformanceUtils
        .get_page_load_time(driver)
    )

    print(
        f"\nPage Load Time: "
        f"{load_time} seconds"
    )

    assert load_time < 5