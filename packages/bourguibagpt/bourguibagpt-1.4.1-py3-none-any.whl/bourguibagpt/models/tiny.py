from pathlib import Path
from llama_cpp import Llama
from .base import BaseModel
from ..config import MODEL_CONFIG

class BourguibaT(BaseModel):
    def __init__(self):
        super().__init__(MODEL_CONFIG["tiny"])
        self.model_file = self.config["model_file"]
        self.llm = None

    def install_model(self):
        self._run_subprocess("pip install llama-cpp-python")
        if not Path(self.model_file).exists():
            self._run_subprocess(
                f"huggingface-cli download {self.config['model_name']} {self.model_file}"
            )

    def generate_answer(self, prompt: str):
        if not self.llm:
            self.llm = Llama(
                model_path=self.model_file,
                n_ctx=2048,
                n_threads=4,
                n_gpu_layers=0
            )
        output = self.llm(
            f"<|user|>\n{prompt}<|assistant|>",
            max_tokens=self.config["max_length"],
            temperature=0.7
        )
        return output['choices'][0]['text']