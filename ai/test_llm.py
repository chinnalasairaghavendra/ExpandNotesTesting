from llm_client import LLMClient

llm = LLMClient()

response = llm.ask(
    "Say hello"
)

print(response)