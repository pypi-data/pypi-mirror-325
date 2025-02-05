from transformers import pipeline
from .base import BaseModel
from ..config import MODEL_CONFIG

class GPTNeo125M(BaseModel):
    def __init__(self):
        super().__init__(MODEL_CONFIG["tiny"])

    def install_model(self):
        self._run_subprocess("pip install transformers")

    def generate_answer(self, prompt: str) -> str:
        if not self.model:
            self.model = pipeline("text-generation", model=self.config["model_name"], device=-1)  # Force CPU
        return self.model(prompt, max_length=50)[0]["generated_text"]