from ai.llm_client import LLMClient


class AILocatorHealer:

    @staticmethod
    def heal_locator(

        failed_locator,

        page_source
    ):

        llm = LLMClient()

        prompt = f"""
        A Selenium locator failed.

        Failed locator:
        {failed_locator}

        HTML:
        {page_source[:5000]}

        Suggest ONLY ONE valid XPath locator.
        Return ONLY the XPath string.
        """

        response = llm.ask(prompt)

        return response.strip()