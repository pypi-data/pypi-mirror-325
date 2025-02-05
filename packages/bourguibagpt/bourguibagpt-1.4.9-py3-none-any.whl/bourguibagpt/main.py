import sys
from pathlib import Path
import platform
import re
import logging
import argparse
import json
from datetime import datetime
from typing import Optional, List, Dict, Any
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
import subprocess

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Import custom modules
from bourguibagpt.models.tiny import GPTNeo125M
from bourguibagpt.models.medium import GPTNeo1_3B
from bourguibagpt.models.large import GPTNeo2_7B
from bourguibagpt.utils.memory import get_system_memory, recommend_model
from bourguibagpt.utils.system import get_os_info
from bourguibagpt.config import MODEL_CONFIG

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Initialize console for rich output
console = Console()

# Banner
BANNER = """
╔══════════════════════════════════════════════════════════════╗
║  ____                            _ _           ____ ____ _____ ║
║ | __ ) ___  _   _ _ __ __ _ _  (_) |__   __ / ___|  _ \_   _|║
║ |  _ \/ _ \| | | | '__/ _` | | | | '_ \ / _` | |  | |_) || |  ║
║ | |_) | (_) | |_| | | | (_| | |_| | |_) | (_| | |__| __/ | |  ║
║ |____/\___/ \__,_|_|  \__, |\__,_|_.__/ \__,_|\\____|_|   |_|  ║
║                          |_|                                    ║
║              Your Tunisian Shell Command Assistant             ╚══════════════════════════════════════════════════════════════╝
"""

VERSION = "3.0.0"

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

    def generate_command(self, prompt: str) -> str:
        """Generate shell command from user prompt."""
        os_info = get_os_info()
        os_specific_prompt = (
            f"Generate a shell command to {prompt} on {os_info}. "
            "Return ONLY the command itself without any explanations, comments, or code blocks. "
            "The response should be a single line executable command."
        )
        
        model = self._get_model()
        response = model.generate_answer(os_specific_prompt)
        
        # Post-processing pipeline
        command = response.strip()
        # Remove code blocks
        command = re.sub(r'^\s*```(?:shell|bash)?\s*', '', command, flags=re.IGNORECASE)
        command = re.sub(r'\s*```\s*$', '', command, flags=re.IGNORECASE)
        # Remove any remaining line breaks and shell prompts
        command = re.sub(r'\n\s*', ' ', command).strip()
        # Remove dangerous characters (defense in depth)
        command = re.sub(r'[;&|]', '', command).strip()
        
        # Split into lines and validate
        lines = [line.strip() for line in command.splitlines() if line.strip()]
        valid_lines = [
            line for line in lines
            if not line.lower().startswith(('bash', 'sh', 'zsh', 'echo'))
        ]
        
        command = valid_lines[0] if valid_lines else ''
        
        self.command_history.append({
            "prompt": prompt,
            "command": command,
            "timestamp": datetime.now().isoformat(),
            "os": os_info
        })
        self._save_history()
        return command

    def _get_model(self):
        """Get the appropriate model based on configuration."""
        if "125M" in self.model_name:
            return GPTNeo125M()
        elif "1.3B" in self.model_name:
            return GPTNeo1_3B()
        elif "2.7B" in self.model_name:
            return GPTNeo2_7B()
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")

    def run(self) -> None:
        """Interactive command generation loop."""
        console.print(f"[bold cyan]{BANNER}[/bold cyan]")
        console.print(f"[bold blue]BourguibaGPT[/bold blue] [cyan]v{VERSION}[/cyan]")
        console.print(f"[dim]Powered by EleutherAI - Model: {self.model_name}[/dim]")
        console.print("\n[italic]Type 'help' for available commands or 'exit' to quit[/italic]\n")
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold magenta]🇹🇳 BourguibaGPT[/bold magenta] [bold blue]→[/bold blue]")
                
                if user_input.lower() in ['exit', 'quit']:
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                else:
                    command = self.generate_command(user_input)
                    if self.output_command_only:
                        console.print(command)
                    else:
                        console.print(f"\n[green]Generated command:[/green]")
                        console.print(Panel(command, style="bold white"))
                        
            except KeyboardInterrupt:
                console.print("\n[yellow]Exiting...[/yellow]")
                break
            except Exception as e:
                logging.error(f"Error in command loop: {e}")

    def _show_help(self) -> None:
        """Display help information."""
        help_text = """[bold]Available Commands:[/bold]
        
        [cyan]help[/cyan] - Show this help message
        [cyan]exit/quit[/cyan] - Exit BourguibaGPT
        
        [bold]Tips:[/bold]
        
        • Be specific in your command requests
        • Use natural language to describe what you want to do
        • Commands are validated for safety
        • History is saved automatically
        """
        console.print(Panel(help_text, title="[bold]BourguibaGPT Help[/bold]", border_style="blue", box=box.DOUBLE))

def main() -> None:
    """Main entry point for BourguibaGPT."""
    console = Console()
    try:
        # Detect system specs
        system_ram = get_system_memory()
        os_info = get_os_info()
        recommended_model = recommend_model(system_ram)

        console.print(f"[bold cyan]System Information:[/bold cyan]")
        console.print(f"• OS: {os_info}")
        console.print(f"• RAM: {system_ram:.1f} GB")
        console.print(f"• Recommended Model: {MODEL_CONFIG[recommended_model]['description']}")

        # Let user select configuration
        console.print("\n[bold]Available Models:[/bold]")
        for key, config in MODEL_CONFIG.items():
            console.print(f"• {key.capitalize()}: {config['description']}")

        selected_model = Prompt.ask(
            "\n[bold]Select a model[/bold]",
            choices=list(MODEL_CONFIG.keys()),
            default=recommended_model
        )

        # Initialize model
        if selected_model == "tiny":
            model = GPTNeo125M()
        elif selected_model == "medium":
            model = GPTNeo1_3B()
        elif selected_model == "large":
            model = GPTNeo2_7B()
        else:
            raise ValueError("Invalid model selection")

        model.install_model()

        # Initialize command generator
        generator = ShellCommandGenerator(model_name=MODEL_CONFIG[selected_model]["model_name"], output_command_only=True)
        generator.run()

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()