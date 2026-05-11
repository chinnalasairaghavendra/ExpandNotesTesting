from ai.llm_client import LLMClient


class FailureAnalyzer:

    @staticmethod
    def analyze(error):
        llm = LLMClient()
        prompt = f"""
        Analyze this Selenium/Pytest automation failure.

        Give:
        1. Root cause
        2. Why it happened
        3. Possible fix
        4. Stability improvement suggestions

        Error:
        {error}
        """
        return llm.ask(prompt)