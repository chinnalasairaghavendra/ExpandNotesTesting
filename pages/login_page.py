from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    ERROR_MESSAGE = (By.CLASS_NAME, "toast-body")

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.logger.info(
            f"Attempting login with email: {email}"
        )
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        self.logger.info("Login button clicked")

    def get_error_message(self):

        try:
            toast = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return toast.text

        except:
            try:
                validation_error = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "invalid-feedback")
                    )
                )
                return validation_error.text

            except:
                return None

    def is_login_successful(self):
        try:
            self.logger.info(
                "Validating login success"
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'a[data-testid="home"]')
                )
            )
            return True
        except:
            return False