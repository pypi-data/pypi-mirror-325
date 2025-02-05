import platform
import subprocess

def get_os_info() -> str:
    """Detect OS and Linux distribution."""
    os_name = platform.system()
    if os_name == "Linux":
        try:
            # Try to get Linux distribution info
            result = subprocess.run(
                ["lsb_release", "-ds"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip().strip('"')
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to generic Linux if lsb_release is not available
            return "Linux (Unknown Distribution)"
    return os_name

def get_os_type() -> str:
    """Get OS type (Windows, Linux, macOS)."""
    return platform.system()