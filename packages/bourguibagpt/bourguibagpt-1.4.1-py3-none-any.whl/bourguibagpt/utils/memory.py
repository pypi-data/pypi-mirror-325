import psutil
import torch

def get_system_memory() -> float:
    """Return total system memory in GB"""
    return psutil.virtual_memory().total / (1024 ** 3)

def get_gpu_memory() -> float:
    """Return available GPU memory in GB"""
    if torch.cuda.is_available():
        return torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
    return 0.0