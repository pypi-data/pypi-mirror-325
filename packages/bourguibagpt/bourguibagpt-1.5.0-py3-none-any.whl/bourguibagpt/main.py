import platform
import re
import sys
import os
import logging
import argparse
import time
import signal
import json
from pathlib import Path
from typing import Optional, List, Dict, Union, Any
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress
from rich.text import Text
from rich.layout import Layout
from rich import box
import requests
import subprocess
from datetime import datetime

# Mock classes for GPTNeo models (replace these with actual imports/definitions)
class GPTNeo125M:
    def install_model(self):
        pass

class GPTNeo1_3B:
    def install_model(self):
        pass

class GPTNeo2_7B:
    def install_model(self):
        pass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

console = Console()

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║  ____                            _ _           ____ ____ _____ ║
║ | __ ) ___  _   _ _ __ __ _ _  (_) |__   __ / ___|  _ \\_   _|║
║ |  _ \\/ _ \\| | | | '__/ _` | | | | '_ \\ / _` | |  | |_) || |  ║
║ | |_) | (_) | |_| | | | (_| | |_| | |_) | (_| | |__| __/ | |  ║
║ |____/\\___/ \\__,_|_|  \\__, |\\__,_|_.__/ \\__,_|\\____|_|   |_|  ║
║                          |_|                                    ║
║              Your Tunisian Shell Command Assistant             
╚══════════════════════════════════════════════════════════════╝
"""

VERSION = "3.0.0"

# Example configurations for each model
MODEL_CONFIG = {
    "tiny": {
        "model_name": "gpt-neo-125M",
        "description": "Lightweight model for systems with ≤8 GB RAM"
    },
    "medium": {
        "model_name": "gpt-neo-1.3B",
        "description": "Balanced model for systems with 8–16 GB RAM"
    },
    "large": {
        "model_name": "gpt-neo-2.7B",
        "description": "Powerful model for systems with ≥16 GB RAM"
    }
}

def get_system_memory() -> float:
    """Example function to get system memory in GB."""
    import psutil
    mem = psutil.virtual_memory()
    return mem.total / (1024 ** 3)

def get_os_info() -> str:
    """Detect the operating system and, if Linux, the distribution."""
    os_name = platform.system()
    if os_name == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME"):
                        return line.split("=")[1].strip().strip('"')
        except Exception as e:
            logging.warning(f"Could not detect Linux distribution: {e}")
    return os_name

def recommend_model(system_ram: float) -> str:
    """Recommend a model key based on RAM."""
    if system_ram <= 8:
        return "tiny"
    elif system_ram <= 16:
        return "medium"
    else:
        return "large"

class ShellCommandGenerator:
    """Shell command generator with enhanced safety and reliability."""
    
    def __init__(
        self,
        model_name: str,
        temperature: float = 0.7,
        history_file: Optional[Path] = None,
        output_command_only: bool = False,
    ) -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.history_file = history_file or Path.home() / ".shell_command_history.json"
        self.command_history: List[Dict[str, Any]] = []
        self.output_command_only = output_command_only
        self.ollama_api = "http://localhost:11434/api/generate"
        self._load_history()

    def _load_history(self) -> None:
        """Load command history from file."""
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r') as f:
                    self.command_history = json.load(f)
        except Exception as e:
            logging.warning(f"Failed to load history: {e}")
            self.command_history = []

    def _save_history(self) -> None:
        """Save command history to file."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.command_history, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to save history: {e}")

    def run(self) -> None:
        """Dummy runner to simulate command generation loop."""
        console.print(f"[bold cyan]{BANNER}[/bold cyan]")
        console.print(f"[bold blue]BourguibaGPT[/bold blue] [cyan]v{VERSION}[/cyan]")
        console.print(f"[dim]Powered by Ollama - Model: {self.model_name}[/dim]")
        console.print("\n[italic]Type 'help' for available commands or 'exit' to quit[/italic]\n")

        while True:
            user_input = Prompt.ask("\n[bold magenta]🇹🇳 BourguibaGPT[/bold magenta] [bold blue]→[/bold blue]")
            if user_input.lower() in ['exit', 'quit']:
                break
            generated_command = self._generate_mock_command(user_input)
            if self.output_command_only:
                print(generated_command)
            else:
                console.print(f"\n[green]Generated command:[/green]")
                console.print(Panel(generated_command, style="bold white"))

    def _generate_mock_command(self, user_input: str) -> str:
        """Simulated command generation."""
        return f"mkdir {user_input.replace('create a folder called ', '')}"

    def install_model(self) -> None:
        """Placeholder for any model installation steps."""
        pass

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Enhanced Shell Command Generator")
    parser.add_argument("--model", default="mistral-openorca", help="Ollama model name")
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Generation temperature (0.0-1.0)",
        choices=[x/10 for x in range(11)]
    )
    parser.add_argument("--history-file", type=Path, help="Custom history file location")
    return parser.parse_args()

def main() -> None:
    """Main entry point."""
    try:
        args = parse_arguments()
        system_ram = get_system_memory()
        os_info = get_os_info()
        recommended = recommend_model(system_ram)

        console.print(f"[bold cyan]System Information:[/bold cyan]")
        console.print(f"• OS: {os_info}")
        console.print(f"• RAM: {system_ram:.1f} GB")
        console.print(f"• Recommended Model: {MODEL_CONFIG[recommended]['description']}")

        console.print("\n[bold]Available Models:[/bold]")
        for key, config in MODEL_CONFIG.items():
            console.print(f"• {key.capitalize()}: {config['description']}")

        selected_model_key = Prompt.ask(
            "\n[bold]Select a model[/bold] (t=Tiny / m=Medium / l=Large)",
            choices=["t","m","l"],
            default="m"
        )

        if selected_model_key == "t":
            selected_model = "tiny"
        elif selected_model_key == "m":
            selected_model = "medium"
        elif selected_model_key == "l":
            selected_model = "large"
        else:
            raise ValueError("Invalid model selection")

        # Instantiate the correct GPTNeo model
        if selected_model == "tiny":
            model = GPTNeo125M()
        elif selected_model == "medium":
            model = GPTNeo1_3B()
        else:
            model = GPTNeo2_7B()

        # Install/unpack the chosen model
        model.install_model()

        shell_generator = ShellCommandGenerator(
            model_name=MODEL_CONFIG[selected_model]["model_name"],
            temperature=args.temperature,
            history_file=args.history_file,
            output_command_only=False
        )
        shell_generator.run()

    except Exception as e:
        console.print(f"[red]Initialization error: {e}[/red]")
        logging.error("Initialization error", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()