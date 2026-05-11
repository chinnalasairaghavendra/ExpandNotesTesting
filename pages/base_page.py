from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import (
    WebDriverWait
)
from selenium.webdriver.support import (
    expected_conditions as EC
)
from utils.logger import get_logger
from ai.retry_agent import (
    RetryAgent
)
from ai.intelligent_waits import (
    IntelligentWaits
)
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(
            self.__class__.__name__
        )

    def click(self, locator):
        def action():
            self.logger.info(
                f"Clicking element: {locator}"
            )
            element = (
                IntelligentWaits
                .wait_for_clickable(
                    self.driver,
                    locator
                )
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView("
                "{block: 'center'});",
                element
            )
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )
        RetryAgent.execute(action)

    def type(self, locator, text):
        def action():
            self.logger.info(
                f"Typing '{text}' "
                f"into element: {locator}"
            )
            element = (
                IntelligentWaits
                .wait_for_visible(
                    self.driver,
                    locator
                )
            )
            element.clear()
            element.send_keys(text)
        RetryAgent.execute(action)

    def get_text(self, locator):
        self.logger.info(
            f"Getting text from element: {locator}"
        )
        return (
            IntelligentWaits
            .wait_for_visible(
                self.driver,
                locator
            ).text
        )