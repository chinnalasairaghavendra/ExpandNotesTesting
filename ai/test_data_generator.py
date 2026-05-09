import json

from ai.llm_client import LLMClient


class TestDataGenerator:

    @staticmethod
    def generate_note():

        llm = LLMClient()

        prompt = """
        Generate realistic test note data.

        Return ONLY valid JSON in this format:

        {
            "title": "...",
            "description": "...",
            "category": "Home"
        }

        Category must be one of:
        Home, Work, Personal
        """

        response = llm.ask(prompt)

        return json.loads(response)