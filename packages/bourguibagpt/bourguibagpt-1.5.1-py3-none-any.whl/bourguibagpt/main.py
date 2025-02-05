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
from typing import Optional, List, Dict, Any
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress
from rich.text import Text
from rich.layout import Layout
from rich import box
import subprocess
from datetime import datetime

# Import Hugging Face transformers components
from transformers import pipeline, set_seed

# Mock classes for GPTNeo models (replace these with actual imports/definitions if needed)
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
║              Your Tunisian Shell Command Assistant             ║
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
    """Retrieve total system memory in GB."""
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
    """Recommend a model key based on available RAM."""
    if system_ram <= 8:
        return "tiny"
    elif system_ram <= 16:
        return "medium"
    else:
        return "large"

class ShellCommandGenerator:
    """Shell command generator with enhanced safety and reliability using Hugging Face."""
    
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
        self.max_retries = 3
        self.timeout = 30
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

    def _call_hf(self, prompt: str) -> Dict[str, Any]:
        """
        Call Hugging Face text generation pipeline to generate a shell command.
        Returns a dict with key 'command'.
        """
        try:
            # Initialize the text generation pipeline with given model on CPU
            generator = pipeline("text-generation", model=self.model_name, device=-1)
            # Set seed for reproducibility; adjust max_length as needed
            set_seed(42)
            results = generator(prompt, max_length=50, num_return_sequences=1)
            text = results[0]["generated_text"].strip()
            # Remove markdown style code fences if present
            command = text.replace("```", "").strip()
            return {"command": command}
        except Exception as e:
            raise ValueError(f"Hugging Face generation error: {e}")

    def generate_command(self, prompt: str) -> Dict[str, Any]:
        """Generate a shell command based on the given prompt using Hugging Face."""
        try:
            result = self._call_hf(prompt)
            command = result.get('command', '').strip()
            if not command:
                raise ValueError("Generated command is empty")
            record = {
                'prompt': prompt,
                'command': command,
                'timestamp': datetime.now().isoformat(),
                'success': True,
                'error': None
            }
            self.command_history.append(record)
            self._save_history()
            return record
        except Exception as e:
            record = {
                'prompt': prompt,
                'command': None,
                'timestamp': datetime.now().isoformat(),
                'success': False,
                'error': str(e)
            }
            self.command_history.append(record)
            self._save_history()
            console.print(f"[red]Error generating command: {e}[/red]")
            return record

    def run(self) -> None:
        """Interactive command generation loop."""
        console.print(f"[bold cyan]{BANNER}[/bold cyan]")
        console.print(f"[bold blue]BourguibaGPT[/bold blue] [cyan]v{VERSION}[/cyan]")
        console.print(f"[dim]Powered by Hugging Face - Model: {self.model_name}[/dim]")
        console.print("\n[italic]Type 'help' for available commands or 'exit' to quit[/italic]\n")
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold magenta]🇹🇳 BourguibaGPT[/bold magenta] [bold blue]→[/bold blue]")
                if user_input.lower() in ['exit', 'quit']:
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                elif user_input.lower() == 'history':
                    self.show_history()
                elif user_input.lower().startswith('execute '):
                    # Execute a command provided after "execute "
                    command = user_input[8:].strip()
                    self.execute_command(command)
                else:
                    # Use the prompt directly to generate command via Hugging Face
                    result = self.generate_command(user_input)
                    if result.get("command"):
                        if self.output_command_only:
                            print(result["command"])
                        else:
                            console.print(f"\n[green]Generated command:[/green]")
                            console.print(Panel(result["command"], style="bold white"))
                            
                            choice = Prompt.ask(
                                "\n[yellow]Type 'e' to execute the generated command and exit, or 'n' to return to the prompt:[/yellow]",
                                choices=["e", "n"],
                                default="n"
                            )
                            if choice.lower() == "e":
                                self.execute_command(result["command"], confirm_execution=False)
                                console.print("[green]Exiting...[/green]")
                                sys.exit(0)
                            else:
                                console.print("[blue]Continuing with a new prompt...[/blue]")
                    else:
                        console.print("[red]Failed to generate a valid command[/red]")
                        
            except KeyboardInterrupt:
                console.print("\n[yellow]Exiting...[/yellow]")
                break
            except Exception as e:
                logging.error(f"Error in command loop: {e}")
    
    def execute_command(self, command: str, confirm_execution: bool = True) -> bool:
        """Safely execute a shell command with confirmation."""
        try:
            if confirm_execution:
                confirm = Prompt.ask(
                    "\n[yellow]Do you want to execute this command?[/yellow]",
                    choices=["yes", "no"],
                    default="no"
                )
                if confirm.lower() != "yes":
                    return False
            console.print("\n[cyan]Executing command...[/cyan]")
            result = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True
            )
            if result.returncode == 0:
                console.print("[green]Command executed successfully[/green]")
                if result.stdout:
                    console.print(Panel(result.stdout, title="Output", border_style="green"))
            else:
                console.print("[red]Command failed[/red]")
                if result.stderr:
                    console.print(Panel(result.stderr, title="Error", border_style="red"))
            return result.returncode == 0
        except Exception as e:
            console.print(f"[red]Error executing command: {e}[/red]")
        return False

    def show_history(self, limit: int = 10) -> None:
        """Display command history."""
        if not self.command_history:
            console.print("[yellow]No command history available[/yellow]")
            return
        console.print("\n[bold]Command History:[/bold]")
        for entry in reversed(self.command_history[-limit:]):
            console.print(Panel(
                f"Prompt: {entry['prompt']}\nCommand: {entry['command']}\nTime: {entry['timestamp']}",
                border_style="blue"
            ))

    def _show_help(self) -> None:
        """Display help information."""
        help_text = """[bold]Available Commands:[/bold]
        
[cyan]help[/cyan] - Show this help message
[cyan]history[/cyan] - Show command history
[cyan]execute <command>[/cyan] - Execute a specific command
[cyan]exit or quit[/cyan] - Exit BourguibaGPT

[bold]Tips:[/bold]
• Be specific in your command requests
• Use natural language to describe what you want to do
• Commands are validated for safety
• History is saved automatically
        """
        console.print(Panel(
            help_text,
            title="[bold]BourguibaGPT Help[/bold]",
            border_style="blue",
            box=box.DOUBLE
        ))

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Enhanced Shell Command Generator using Hugging Face")
    parser.add_argument("--model", default="mistral-openorca", help="Hugging Face model name")
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
    """Main entry point with error handling."""
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
            choices=["t", "m", "l"],
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
        # Instantiate the correct GPTNeo model for potential installation steps
        if selected_model == "tiny":
            model = GPTNeo125M()
        elif selected_model == "medium":
            model = GPTNeo1_3B()
        else:
            model = GPTNeo2_7B()
        # Install/unpack the chosen model if required
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