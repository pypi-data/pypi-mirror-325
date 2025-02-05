from transformers import pipeline
from .base import BaseModel
from ..config import MODEL_CONFIG

class BourguibaB(BaseModel):
    def __init__(self, vram_gb: int):
        super().__init__(MODEL_CONFIG["big"])
        self.vram_gb = vram_gb
        self.pipeline = None

    def install_model(self):
        self._run_subprocess("pip install git+https://github.com/huggingface/transformers.git")

    def generate_answer(self, prompt: str):
        if not self.pipeline:
            model_name = ("mistralai/Mistral-7B-Instruct-v0.3" 
                          if 4 <= self.vram_gb <= 6 
                          else self.config["model_name"])
            self.pipeline = pipeline("text-generation", model=model_name)
        return self.pipeline(prompt, max_length=self.config["max_length"])[0]["generated_text"]