from transformers import pipeline
from .base import BaseModel
from ..config import MODEL_CONFIG

class GPTNeo125M(BaseModel):
    def __init__(self):
        super().__init__(MODEL_CONFIG["tiny"])

    def install_model(self):
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        self._run_subprocess("pip install transformers")
        
        # Download model using Hugging Face
        from transformers import AutoModelForCausalLM, AutoTokenizer
        
        model = AutoModelForCausalLM.from_pretrained(self.config["model_name"])
        tokenizer = AutoTokenizer.from_pretrained(self.config["model_name"])
        
        # Save model and tokenizer
        model.save_pretrained(self.model_path)
        tokenizer.save_pretrained(self.model_path)

    def generate_answer(self, prompt: str) -> str:
        if not self.model:
            self.model = pipeline("text-generation", model=str(self.model_path), device=-1)
        return self.model(prompt, max_length=50)[0]["generated_text"]