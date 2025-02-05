from abc import ABC, abstractmethod
import subprocess
import logging

logger = logging.getLogger(__name__)

class BaseModel(ABC):
    @abstractmethod
    def __init__(self, config: dict):
        self.config = config
        self.model = None
    
    @abstractmethod
    def install_model(self):
        """Install model dependencies and download weights"""
        pass
    
    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        """Generate response from model"""
        pass

    def _run_subprocess(self, command: str):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Subprocess error: {e}")
            raise