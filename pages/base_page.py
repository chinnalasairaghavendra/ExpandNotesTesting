from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def type(self, locator, text):
        self.logger.info(
            f"Typing '{text}' into element: {locator}"
        )
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):
        self.logger.info(
            f"Getting text from element: {locator}"
        )
        return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator)
        ).text