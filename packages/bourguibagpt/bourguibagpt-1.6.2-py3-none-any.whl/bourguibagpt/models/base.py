from abc import ABC, abstractmethod
import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class BaseModel(ABC):
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