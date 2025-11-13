import os
import requests

"""
This script helps you get GGUF models from Hugging Face for use with llama.cpp or llama-cpp-python.

Methods:
 1. Manual Download: Instructions included
 2. Scripted Download: Provide a direct Hugging Face .gguf link
 3. Interactive download (choose quantization, autograb from Hugging Face)
After download, use your GGUF in llama-cpp-python (see: use_local_gguf.py) or llama.cpp.
"""

HUGGINGFACE_URL = ""  # Set this to a direct link to a .gguf model file
OUTPUT_DIR = "models"  # Folder to save GGUF files

# Quantization choices for Mistral-7B-v0.1 GGUF
MISTRAL_7B_QUANTS = [
    ("FP16",   "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.FP16.gguf"),
    ("Q8_0",   "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q8_0.gguf"),
    ("Q6_K",   "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q6_K.gguf"),
    ("Q5_K_M", "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q5_K_M.gguf"),
    ("Q4_K_M", "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf"),
    ("Q3_K",   "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q3_K.gguf"),
    ("Q2_K",   "https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q2_K.gguf"),
]


def explain_huggingface_download():
    help_text = '''\nManual Download Steps:\n1. Go to https://huggingface.co/models?search=gguf\n2. Search for a model (e.g. "TheBloke/Mistral-7B-v0.1-GGUF")\n3. Click on your desired .gguf file, then click "Download"\n4. Save the file to your 'models' folder (create it if needed)\n\nScripted Download steps below if you have a direct .gguf link.\n'''
    print(help_text)


def download_gguf_hf_script(hf_url, output_dir):
    if not hf_url:
        print("[ERROR] Please provide a Hugging Face direct .gguf link!")
        return
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, os.path.basename(hf_url))
    print(f"[INFO] Downloading: {hf_url}\nSaving to: {filename}")
    r = requests.get(hf_url, stream=True)
    if r.status_code != 200:
        print(f"[ERROR] Download failed with status {r.status_code}.")
        return
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"[SUCCESS] GGUF file saved as: {filename}")
    print("You can now use this GGUF file in your Python app or llama.cpp.")


def interactive_quantized_download():
    print("\nMISTRAL-7B GGUF MODEL AUTO-DOWNLOAD MENU:\nPick a quantization level for your hardware:")
    for idx, (quant, _) in enumerate(MISTRAL_7B_QUANTS, 1):
        if quant == "FP16":
            note = "(highest RAM, highest quality)"
        elif quant == "Q8_0":
            note = "(large, almost full quality)"
        elif quant == "Q4_K_M":
            note = "(recommended for most users)"
        elif quant == "Q3_K":
            note = "(tiny, lowest memory, least accurate)"
        else:
            note = ""
        print(f"  {idx}. {quant} {note}")
    pick = input("Enter the number of your choice: ").strip()
    if not pick.isdigit() or int(pick) < 1 or int(pick) > len(MISTRAL_7B_QUANTS):
        print("[ERROR] Invalid choice.")
        return
    quant, url = MISTRAL_7B_QUANTS[int(pick)-1]
    print(f"\nYou chose: {quant}")
    download_gguf_hf_script(url, OUTPUT_DIR)


def main():
    intro = '''\n######## GGUF Model Downloader for llama.cpp/llama-cpp-python ########\nChoose your method:\n1. Manual Hugging Face download (follow printed instructions)\n2. Scripted Hugging Face download (if you have a direct download link)\n3. Download Mistral-7B GGUF file (pick quantization, auto-download)\n'''
    print(intro)
    option = input("Download method? (1=Manual HF, 2=Scripted HF, 3=Menu-download): ").strip()
    if option == "1":
        explain_huggingface_download()
    elif option == "2":
        url = input("Paste your Hugging Face direct .gguf file link here: ").strip()
        if not url.endswith(".gguf"):
            print("[ERROR] Must be a .gguf link. Look for 'resolve/main/*.gguf'.")
            return
        download_gguf_hf_script(url, OUTPUT_DIR)
    elif option == "3":
        interactive_quantized_download()
    else:
        print("[ERROR] Invalid option.")

    print("\nNext step: Use your GGUF file with llama-cpp-python (see use_local_gguf.py) or llama.cpp.")

if __name__ == "__main__":
    main()
