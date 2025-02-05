from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from .base import BaseModel
from ..config import MODEL_CONFIG

class GPTNeo2_7B(BaseModel):
    def __init__(self):
        super().__init__(MODEL_CONFIG["large"])
        if not self.is_model_cached():
            self.install_model()
        self.load_model()

    def install_model(self):
        self._run_subprocess("pip install transformers")
        # Download and cache model
        model = AutoModelForCausalLM.from_pretrained(self.config["model_name"])
        tokenizer = AutoTokenizer.from_pretrained(self.config["model_name"])
        model_path = self.cache_dir / self.config["model_name"].replace("/", "_")
        model.save_pretrained(str(model_path))
        tokenizer.save_pretrained(str(model_path))

    def load_model(self):
        if not self.model:
            model_path = self.cache_dir / self.config["model_name"].replace("/", "_")
            self.model = pipeline("text-generation", model=str(model_path), device=-1)

    def generate_answer(self, prompt: str) -> str:
        return self.model(prompt, max_length=50)[0]["generated_text"]