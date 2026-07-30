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
response = client.chat.completions.create(
    model="claude-opus-5",
    messages=messages,
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")