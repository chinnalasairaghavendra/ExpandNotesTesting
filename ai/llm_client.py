import os
import time

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


class LLMClient:

    def __init__(self):

        self.client = OpenAI(

            api_key=os.getenv(
                "LONGCAT_API_KEY"
            ),

            base_url="https://api.longcat.chat/openai/v1",

            timeout=60
        )

    def ask(self, prompt):

        retries = 3

        for attempt in range(retries):

            try:

                response = (
                    self.client.chat.completions.create(

                        model="longcat-flash-chat",

                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],

                        temperature=0.3
                    )
                )

                return (
                    response
                    .choices[0]
                    .message
                    .content
                )

            except Exception as e:

                print(
                    f"LLM Retry {attempt + 1}: {e}"
                )

                time.sleep(2)

        raise Exception(
            "LongCat API failed after retries"
        )