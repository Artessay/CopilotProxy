import time
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:4000/v1",
)

messages = [
    {
        "role": "user",
        "content": "What is the capital of Korea?"
    }
]

start = time.time()
response = client.responses.create(
    model="codex-auto-review",
    input=messages,
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.output_text}")