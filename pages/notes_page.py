from selenium.common.exceptions import (
    StaleElementReferenceException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import (
    Select,
    WebDriverWait
)

from pages.base_page import BasePage


class NotesPage(BasePage):

    ADD_NOTE_BUTTON = (
        By.XPATH,
        "//button[text()='+ Add Note']"
    )

    TITLE_INPUT = (By.ID, "title")

    DESCRIPTION_INPUT = (
        By.ID,
        "description"
    )

    CATEGORY_DROPDOWN = (
        By.ID,
        "category"
    )

    CREATE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Create')]"
    )

    NOTE_TITLES = (
        By.CSS_SELECTOR,
        '[data-testid="note-card-title"]'
    )

    NOTE_CARDS = (
        By.CSS_SELECTOR,
        '[data-testid="note-card"]'
    )

    VALIDATION_ERRORS = (
        By.CLASS_NAME,
        "invalid-feedback"
    )

    def click_add_note(self):

        self.logger.info(
            "Clicking Add Note button"
        )

        self.click(self.ADD_NOTE_BUTTON)

    def enter_title(self, title):

        self.logger.info(
            f"Entering title: {title}"
        )

        self.type(self.TITLE_INPUT, title)

    def enter_description(self, description):

        self.logger.info(
            "Entering description"
        )

        self.type(
            self.DESCRIPTION_INPUT,
            description
        )

    def select_category(
        self,
        category="Home"
    ):

        self.logger.info(
            f"Selecting category: {category}"
        )

        dropdown = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.CATEGORY_DROPDOWN
            )
        )

        Select(dropdown).select_by_visible_text(
            category
        )

    def click_save(self):

        self.logger.info(
            "Clicking Create button"
        )

        self.click(self.CREATE_BUTTON)

    def create_note(
        self,
        title,
        description,
        category="Home"
    ):

        self.logger.info(
            f"Creating note | Title: {title}"
        )

        self.click_add_note()

        self.enter_title(title)

        self.enter_description(description)

        self.select_category(category)

        self.click_save()

        # Wait for page refresh/re-render
        WebDriverWait(
            self.driver,
            10
        ).until(
            lambda driver: self.note_exists(title)
        )

        self.logger.info(
            f"Note created successfully | Title: {title}"
        )

    def note_exists(self, title):

        self.logger.info(
            f"Checking if note exists: {title}"
        )

        try:

            WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_all_elements_located(
                    self.NOTE_TITLES
                )
            )

            # Always fetch fresh elements
            titles = self.driver.find_elements(
                *self.NOTE_TITLES
            )

            title_texts = [
                note.text.strip()
                for note in titles
            ]

            if title in title_texts:

                self.logger.info(
                    f"Note found: {title}"
                )

                return True

            self.logger.warning(
                f"Note NOT found: {title}"
            )

            return False

        except StaleElementReferenceException:

            self.logger.warning(
                "Stale element detected. Retrying..."
            )

            titles = self.driver.find_elements(
                *self.NOTE_TITLES
            )

            title_texts = [
                note.text.strip()
                for note in titles
            ]

            return title in title_texts

    def get_all_note_titles(self):

        self.logger.info(
            "Fetching all note titles"
        )

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_all_elements_located(
                self.NOTE_TITLES
            )
        )

        titles = self.driver.find_elements(
            *self.NOTE_TITLES
        )

        return [
            title.text.strip()
            for title in titles
        ]

    def get_note_card_data(
        self,
        title
    ):

        self.logger.info(
            f"Getting note card data for: {title}"
        )

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_all_elements_located(
                self.NOTE_CARDS
            )
        )

        cards = self.driver.find_elements(
            *self.NOTE_CARDS
        )

        for card in cards:

            try:

                card_text = card.text

                if title in card_text:

                    self.logger.info(
                        f"Card found for: {title}"
                    )

                    return card_text

            except StaleElementReferenceException:

                self.logger.warning(
                    "Stale card detected. Skipping..."
                )

                continue

        self.logger.warning(
            f"No card found for: {title}"
        )

        return None

    def get_validation_errors(self):

        self.logger.info(
            "Fetching validation errors"
        )

        elements = self.driver.find_elements(
            *self.VALIDATION_ERRORS
        )

        return [
            element.text.strip().lower()
            for element in elements
            if element.text.strip()
        ]

    def refresh_page(self):

        self.logger.info(
            "Refreshing browser page"
        )

        self.driver.refresh()

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_all_elements_located(
                self.NOTE_TITLES
            )
        )