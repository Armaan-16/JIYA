"""
JIYA Speed Test Script
Evaluates local inference roundtrip latency.
"""
import time
import ollama

start = time.perf_counter()

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Say only: Hello"
        }
    ],
    options={
        "num_predict": 5,
        "temperature": 0
    }
)

end = time.perf_counter()

print(response["message"]["content"])
print(f"\nTime: {end - start:.2f} seconds")

