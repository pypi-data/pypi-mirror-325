import platform
import subprocess

def get_os_info() -> str:
    """Detect OS and Linux distribution"""
    os_name = platform.system()
    if os_name == "Linux":
        try:
            result = subprocess.run(
                ["lsb_release", "-ds"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip().strip('"')
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    return os_name

def system_has_gpu() -> bool:
    """Check if NVIDIA GPU is available"""
    try:
        subprocess.run(["nvidia-smi"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False