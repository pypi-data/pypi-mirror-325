# Model configuration constants
MODEL_CONFIG = {
    "tiny": {
        "model_name": "bartowski/Phi-3.5-mini-instruct-GGUF",
        "model_file": "Phi-3.5-mini-instruct.Q4_K_M.gguf",
        "max_length": 50,
        "ram_threshold": 8  # GB
    },
    "medium": {
        "model_name": "mistralai/Mistral-7B-Instruct-v0.3",
        "ram_threshold": 16,  # GB
        "vram_threshold": 6  # GB
    },
    "big": {
        "model_name": "bigcode/starcoder2-7b",
        "vram_threshold": 6  # GB
    }
}