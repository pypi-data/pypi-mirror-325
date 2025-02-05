import psutil

def get_system_memory() -> float:
    """Return total system memory in GB."""
    return psutil.virtual_memory().total / (1024 ** 3)

def recommend_model(ram_gb: float) -> str:
    """Recommend the best model based on system RAM."""
    if ram_gb <= 8:
        return "tiny"
    elif 8 < ram_gb <= 16:
        return "medium"
    else:
        return "large"