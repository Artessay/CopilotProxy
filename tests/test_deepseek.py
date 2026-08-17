import time
from openai import OpenAI

client = OpenAI(
    api_key="sk-api-key",
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
    model="deepseek-v4-flash",
    # model="deepseek-v4-pro",
    input=messages,
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.output_text}")