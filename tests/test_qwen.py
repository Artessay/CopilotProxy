import time
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

# model_name = "qwen3.5-9b"
model_name = "qwen3.5-122b-a10b"
# model_name = "qwen3.5-397b-a17b-int4"

messages = [
    {
        "role": "user",
        "content": "What is the capital of Korea?"
    }
]

start = time.time()
response = client.chat.completions.create(
    model=model_name,
    messages=messages,
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")