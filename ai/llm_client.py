import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


class LLMClient:

    def __init__(self):

        self.client = OpenAI(

            api_key=os.getenv(
                "LONGCAT_API_KEY"
            ),

            base_url="https://api.longcat.chat/openai/v1"
        )

    def ask(self, prompt):

        response = self.client.chat.completions.create(

            model="longcat-flash-chat",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3
        )

        return (
            response
            .choices[0]
            .message
            .content
        )