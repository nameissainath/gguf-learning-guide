# Quantized: Local LLMs with GGUF, Quantization and Ollama — Beginner Friendly

Welcome to **Quantized** — your all-in-one mini-suite for exploring, running, and understanding modern local AI models and GGUF files. This repo is for anyone who wants to:
- Run local Large Language Models (LLMs) without cloud dependencies
- Learn about quantization, GGUF, and binary storage in simple terms
- Use Ollama or llama-cpp for offline AI

## 📂 Project Structure

### Code/
Python scripts to help you download, run, and experiment with models:

- **download_and_use_gguf.py**: Interactive downloader for GGUF files from Hugging Face, with a guided menu for quantization choice. Includes manual and scripted download methods. Great for beginners.
- **use_local_gguf.py**: Example: Load and chat with a GGUF model locally using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) in Python. Change the path to your model and run your own prompt offline!
- **download_ollama_model.py**: Download a model using the Ollama CLI. See their docs to convert/export models to GGUF for use elsewhere.
- **use_local_ollama.py**: Example: Use Ollama's local REST API from Python to send prompts to a supported model (like llama3 or mistral). Quick way to try local LLMs with one script.

### Notes/
Beginner-friendly, plain-English explanations:

- **GGUF_Beginner_Guide.md**: The ultimate intro to GGUF format, local LLMs, basic terminology, quantization, and community tooling — no prior knowledge needed.
- **Quantization_Concepts_Beginner_Guide.md**: What is quantization in ML? Visuals, analogies, and simple math to understand bits, bytes, and how neural networks are made smaller.
- **Bit_Byte_Storage_Explained_Beginner.md**: Learn what bits and bytes really mean, how computers store information, and how it all links to AI files.

## 🚀 Quick Start Guide

1. **Download a Model**
   - Use `download_and_use_gguf.py` to guide you through downloading a GGUF file (recommended for first-timers).
   - Or, try `download_ollama_model.py` to fetch a base model with Ollama (see their docs to export if needed).

2. **Run a Model in Python**
   - Install llama-cpp-python: `pip install llama-cpp-python`
   - Edit the path in `use_local_gguf.py` to your GGUF file and run for simple chat.

3. **Send Prompts with Ollama (Python)**
   - Ensure Ollama is running (`ollama serve` or via the desktop app)
   - Run `use_local_ollama.py` to test prompt/response via API

> For first-timers: Start with the GGUF_Beginner_Guide in Notes/ for a gentle intro to every concept (models, quantization, bits, and more).

## ❓ FAQ & Learning
- What is a GGUF or quantized model? See the guides in Notes/.
- How do I choose a quantization? See both the script prompt texts and guides for easy recommendations.
- Need more visuals/examples? Every Note is written for clarity, not just for coders!

---

### Attribution & Thanks
- The guides build on research and examples from open-source communities (llama.cpp, Hugging Face, Ollama, and TheBloke).
- If you found this helpful, consider starring the repo and contributing more beginner resources!

Happy experimenting — and enjoy running local LLMs the accessible way!
