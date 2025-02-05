from transformers import pipeline
from .base import BaseModel
from ..config import MODEL_CONFIG

class BourguibaM(BaseModel):
    def __init__(self):
        super().__init__(MODEL_CONFIG["medium"])
        self.pipeline = None

    def install_model(self):
        self._run_subprocess("pip install git+https://github.com/huggingface/transformers.git")

    def generate_answer(self, prompt: str):
        if not self.pipeline:
            self.pipeline = pipeline("text-generation", model=self.config["model_name"])
        return self.pipeline(prompt, max_length=self.config["max_length"])[0]["generated_text"]