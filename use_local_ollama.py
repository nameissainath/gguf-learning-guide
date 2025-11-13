"""
How to Use a GGUF Model with Ollama via Python

Ollama must be installed and running as a local service:
1. Install Ollama: https://ollama.com/download
2. Launch Ollama (it runs a local server at http://localhost:11434 by default)
3. Make sure your desired model (e.g. llama3, mistral) is pulled via `ollama pull llama3`.

This script sends a prompt to Ollama's REST API and prints the reply.

Requirements: pip install requests
"""
import json
try:
    import requests
except ImportError:
    requests = None
import sys

OLLAMA_SERVER = "http://localhost:11434"
MODEL_NAME = "llama3"  # change as needed (must be available via `ollama pull`)

PROMPT = "Explain what GGUF is in one sentence."

# Compose payload for /api/generate (Ollama HTTP API)
payload = {
    "model": MODEL_NAME,
    "prompt": PROMPT,
}

print(f"Sending prompt to Ollama: {PROMPT}")

if requests:
    try:
        r = requests.post(f"{OLLAMA_SERVER}/api/generate", json=payload, stream=True)
        if r.status_code != 200:
            print(f"Error {r.status_code}: {r.text}")
            sys.exit(1)
        # Ollama streams results - print as received
        response_text = ""
        for line in r.iter_lines():
            if line:
                chunk = json.loads(line)
                response_text += chunk.get("response", "")
        print("\n[Ollama Response]:\n" + response_text.strip())
    except Exception as e:
        print("Could not connect to Ollama server. Is it running?")
        print(e)
else:
    print("\nPlease install the 'requests' library with:")
    print("   pip install requests")
