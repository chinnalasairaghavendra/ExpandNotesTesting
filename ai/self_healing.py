import json

from selenium.webdriver.common.by import By

from ai.llm_client import LLMClient


class AILocatorHealer:

    @staticmethod
    def heal_locator(
        failed_locator,
        interactable_elements
    ):

        llm = LLMClient()

        prompt = f"""
        A Selenium locator failed during UI automation.

        Failed locator:
        {failed_locator}

        Visible interactable elements on the page:
        {interactable_elements}

        Your task:
        Suggest the best replacement locator for the intended element.

        Return ONLY valid JSON in this exact format:

        {{
            "strategy": "xpath",
            "locator": "//button[@type='submit']"
        }}

        OR:

        {{
            "strategy": "css",
            "locator": "button[type='submit']"
        }}

        Rules:
        - Return only JSON.
        - Do not include markdown.
        - Do not include explanation.
        - strategy must be either "xpath" or "css".
        - Prefer stable attributes in this order:
          1. data-testid
          2. id
          3. name
          4. aria-label
          5. placeholder
          6. type
          7. visible text
        - Avoid absolute XPath.
        - Avoid dynamic class names if possible.
        - Choose only one locator.
        """

        response = llm.ask(prompt).strip()

        try:

            locator_data = json.loads(response)

            strategy = (
                locator_data
                .get("strategy", "")
                .lower()
            )

            locator = locator_data.get(
                "locator",
                ""
            )

            if strategy == "xpath":

                return (
                    By.XPATH,
                    locator
                )

            if strategy == "css":

                return (
                    By.CSS_SELECTOR,
                    locator
                )

            raise ValueError(
                f"Unsupported locator strategy: {strategy}"
            )

        except Exception as e:

            raise Exception(
                f"AI locator healing failed. "
                f"Response was: {response}. "
                f"Error: {e}"
            )