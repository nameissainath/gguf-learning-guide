import subprocess
import sys

"""
This script downloads a GGUF model using Ollama CLI.
For local Llama.cpp-based apps, you may wish to export the .gguf file from Ollama after download (see Ollama docs).
"""

MODEL_NAME = "llama3"  # Change to your preferred Ollama-supported model

def check_ollama_installed():
    try:
        subprocess.run(["ollama", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ERROR] Ollama not found. Get it from https://ollama.com/download")
        sys.exit(1)

def download_gguf_with_ollama(model_name):
    print(f"[INFO] Downloading '{model_name}' with Ollama CLI...")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"[SUCCESS] Model '{model_name}' downloaded. The GGUF file is managed by Ollama.")
        print("See https://github.com/ollama/ollama/blob/main/docs/models.md for info on exporting .gguf files.")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Download failed for '{model_name}'.")
        sys.exit(1)

def main():
    check_ollama_installed()
    download_gguf_with_ollama(MODEL_NAME)

if __name__ == "__main__":
    main()
