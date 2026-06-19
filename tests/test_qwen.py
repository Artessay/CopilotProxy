import time
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
    timeout=3600
)

messages = [
    {
        "role": "user",
        "content": "What is the capital of Korea?"
    }
]

start = time.time()
response = client.chat.completions.create(
    model="qwen3.5-9b",
    messages=messages,
    max_tokens=32768,
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")