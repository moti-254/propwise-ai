import os
import requests
import json

# Set these to match your environment
API_KEY = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")  # or "openrouter/llama-3-70b"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Say hello!"}
    ],
    "temperature": 0.2,
    "max_tokens": 100,
}

print("POST to:", BASE_URL)
print("Model:", MODEL)
response = requests.post(BASE_URL, headers=headers, json=payload)
print("Status code:", response.status_code)
print("Raw response:", response.text)

try:
    data = response.json()
    print("Parsed JSON:", json.dumps(data, indent=2))
except Exception as e:
    print("Failed to parse JSON:", e)
