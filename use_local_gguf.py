"""
How to Use a GGUF Model in Python with llama-cpp-python

Steps:
1. Make sure you have downloaded a GGUF file (see download_and_use_gguf.py) from Hugging Face, TheBloke repos, or elsewhere.
2. Place the GGUF file in a known folder (e.g. models/ or your working directory).
3. Install llama-cpp-python:
   pip install llama-cpp-python
4. Update the MODEL_PATH below to the correct location/filename.
5. Run this script to chat with your local model!
"""

import os
from llama_cpp import Llama

# === Change this to your GGUF model's actual location ===
MODEL_PATH = "models/mistral-7b-v0.1.Q2_K.gguf"  # Example

assert os.path.isfile(MODEL_PATH), f"[ERROR] GGUF file not found at: {MODEL_PATH}\nPlace your model in this path or update MODEL_PATH."

llm = Llama(model_path=MODEL_PATH)

# Your prompt goes here
prompt = "Explain what GGUF is in one sentence."

response = llm(prompt)
print("\n[Model Response]:\n" + response["choices"][0]["text"].strip())
