"""
JIYA Benchmarking Script
Measures model invocation latency and response throughput.
"""
import time
from pprint import pprint
import ollama

start = time.perf_counter()

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Reply with only one word: Hello"
        }
    ],
    options={
        "temperature": 0.3,
        "num_predict": 100,
        "think": False
    }
)

end = time.perf_counter()

pprint(response)
print(f"\nTime: {end-start:.2f} sec")

