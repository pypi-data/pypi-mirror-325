from abc import ABC, abstractmethod
import subprocess
import logging
from pathlib import Path
from transformers import pipeline
import torch
import signal
from contextlib import contextmanager
import timeout_decorator

class TimeoutError(Exception):
    pass

@contextmanager
def timeout(seconds):
    def signal_handler(signum, frame):
        raise TimeoutError("Generation timed out")
    
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

logger = logging.getLogger(__name__)

class BaseModel(ABC):
    TIMEOUT = 30  # seconds

    def __init__(self, config: dict):
        self.config = config
        self.model = None
        self.cache_dir = Path.home() / ".cache" / "bourguibagpt" / "models"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def is_model_cached(self) -> bool:
        model_path = self.cache_dir / self.config["model_name"].replace("/", "_")
        return model_path.exists()

    @abstractmethod
    def install_model(self):
        pass

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        pass

    def _run_subprocess(self, command: str):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Subprocess error: {e}")
            raise

    def generate_with_timeout(self, prompt: str) -> str:
        try:
            with timeout(self.TIMEOUT):
                return self.model(
                    prompt,
                    max_length=50,
                    num_return_sequences=1,
                    truncation=True,
                    temperature=0.7
                )[0]["generated_text"]
        except TimeoutError:
            return "Error: Generation timed out. Please try again."
        except Exception as e:
            return f"Error during generation: {str(e)}"