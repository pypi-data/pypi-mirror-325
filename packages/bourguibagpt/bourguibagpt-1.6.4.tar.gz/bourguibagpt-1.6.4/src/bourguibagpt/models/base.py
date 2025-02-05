from abc import ABC, abstractmethod
import subprocess
import logging
import signal
from pathlib import Path
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class TimeoutError(Exception):
    pass

@contextmanager
def timeout_handler(seconds):
    def handler(signum, frame):
        raise TimeoutError()
    
    # Set handler for SIGALRM
    original_handler = signal.signal(signal.SIGALRM, handler)
    
    try:
        signal.alarm(seconds)
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_handler)

class BaseModel(ABC):
    TIMEOUT = 30  # seconds

    @abstractmethod
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