"""
JIYA Ollama Standalone Verification Script
"""
import sys
from pprint import pprint
import ollama

# Ensure Windows PowerShell/cmd console handles UTF-8 (emojis, unicode) cleanly
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main():
    print("Testing local Ollama connection...")
    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": "Tell me about yourself in one short sentence."
            }
        ],
        options={
            "think": False
        }
    )

    print("TYPE:", type(response))
    print("\nCONTENT:", response["message"]["content"])


if __name__ == "__main__":
    main()
