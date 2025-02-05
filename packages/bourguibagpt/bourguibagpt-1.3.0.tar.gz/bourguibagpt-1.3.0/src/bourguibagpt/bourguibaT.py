# Uses bartowski/Phi-3.5-mini-instruct-GGUF for systems with <=8GB RAM and no CPU/GPU
import sys
import subprocess
from transformers import pipeline

class BourguibaT:
    def __init__(self):
        self.model_name = "bartowski/Phi-3.5-mini-instruct-GGUF"

    def install_model(self):
        try:
            subprocess.run(
                f"pip install git+https://github.com/huggingface/transformers.git",
                shell=True, check=True
            )
            # Additional installations if needed for GGUF
        except Exception as e:
            print(f"Failed to install model dependencies: {e}")

    def generate_answer(self, prompt: str):
        # Minimal pipeline usage
        gen = pipeline("text-generation", model=self.model_name)
        return gen(prompt, max_length=50)[0]["generated_text"]