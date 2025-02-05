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
from transformers import pipeline



# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Initialize console for rich output
console = Console()

# Fix banner alignment
BANNER = """
╔══════════════════════════════════════════════════════════════╗
║  ____                            _ _           ____ ____ _____ ║
║ | __ ) ___  _   _ _ __ __ _ _  (_) |__   __ / ___|  _ \\_   _|║
║ |  _ \\/ _ \\| | | | '__/ _` | | | | '_ \\ / _` | |  | |_) || |  ║
║ | |_) | (_) | |_| | | | (_| | |_| | |_) | (_| | |__| __/ | |  ║
║ |____/\\___/ \\__,_|_|  \\__, |\\__,_|_.__/ \\__,_|\\____|_|   |_|  ║
║                          |_|                                    ║
║              Your Tunisian Shell Command Assistant             ╚══════════════════════════════════════════════════════════════╝
"""

VERSION = "2.0.0"

class ShellCommandGenerator:
    """Shell command generator with enhanced safety and reliability"""
    
    def __init__(
        self,
        model_name: str = "microsoft/Phi-3.5-mini-instruct",
        temperature: float = 0.7,
        auto_execute: bool = False,
        history_file: Optional[Path] = None,
        max_retries: int = 3,
        timeout: int = 30,
        hf_api_key: Optional[str] = "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"  # Your key here
    ) -> None:
        # Validate parameters
        if not isinstance(temperature, float) or not 0 <= temperature <= 1:
            raise ValueError("Temperature must be a float between 0 and 1")
        if not isinstance(max_retries, int) or max_retries < 1:
            raise ValueError("max_retries must be a positive integer")
            
        self.model_name = model_name
        self.temperature = temperature
        self.auto_execute = auto_execute
        self.max_retries = max_retries
        self.timeout = timeout
        self.command_history: List[Dict[str, Any]] = []

        # Use Hugging Face Inference API with the provided key.
        self.hf_api_key = hf_api_key
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.history_file = history_file or Path.home() / ".shell_command_history.json"
        
        # Load command history
        self._load_history()
        
        # Initialize the Hugging Face pipeline
        self.generator = pipeline("text-generation", model=self.model_name, use_auth_token=self.hf_api_key)
        
    def get_os_info(self) -> str:
        """Detect the operating system and, if Linux, the distribution."""
        os_name = platform.system()
        if (os_name == "Linux"):
            try:
                with open("/etc/os-release", "r") as f:
                    for line in f:
                        if (line.startswith("PRETTY_NAME")):
                            # Format: PRETTY_NAME="Ubuntu 20.04.2 LTS"
                            return line.split("=")[1].strip().strip('"')
            except Exception as e:
                logging.warning(f"Could not detect Linux distribution: {e}")
        return os_name

    def _load_history(self) -> None:
        """Load command history from file"""
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r') as f:
                    self.command_history = json.load(f)
        except Exception as e:
            logging.warning(f"Failed to load history: {e}")
            self.command_history = []

    def _save_history(self) -> None:
        """Save command history to file"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.command_history, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to save history: {e}")

    def generate_command(self, prompt: str) -> Dict[str, Any]:
        """Generate shell command from user prompt using Hugging Face API"""
        response = self.generator(prompt, max_length=50, temperature=self.temperature)
        command = response[0]["generated_text"]

        # Add to history and return
        self.command_history.append({"prompt": prompt, "command": command, "timestamp": datetime.now().isoformat()})
        self._save_history()
        return {"command": command}

    def _extract_command(self, text: str) -> Optional[str]:
        """Extract command with improved parsing"""
        # Look for CMD: prefix
        if match := re.search(r'CMD:\s*(.+)$', text, re.MULTILINE):
            command = match.group(1).strip()
            # Basic command structure validation
            if re.match(r'^[\w.-]+(\s+[\w."\'*?/-]+)*$', command):
                return command
        return None

    def _validate_command(self, command: str) -> bool:
        """Simplified but strict command validation"""
        # Whitelist of safe commands
        SAFE_COMMANDS = {
            'ls': r'-[altrh]*',
            'mkdir': r'[\w.-]+',
            'touch': r'[\w.-]+',
            'cat': r'[\w.-]+',
            'echo': r'"[^"]*"',
            'pwd': '',
            'find': r'\. -name "[\w.*]+"',
            'grep': r'-[ivr]+ "[\w ]+"',
            'cd': r'[\w./-]*'  # Added cd command support
        }
        
        # Check command against whitelist
        parts = command.split(maxsplit=1)
        base_cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ''
        
        if base_cmd not in SAFE_COMMANDS:
            return False
            
        # Validate arguments against pattern
        if pattern := SAFE_COMMANDS[base_cmd]:
            return bool(re.match(pattern, args))
            
        return True

    def validate_command(self, command: str) -> bool:
        """Validates commands against dangerous patterns"""
        safe_pattern = r'^[\w./-]+(?:\s+(?:[\w./-]+|>>?\s*[\w./-]+))*$'
        dangerous_patterns = [
            r'rm\s+-[rf]{2}',
            r'rm\s+[/*]',
            r'>\s*/dev/',
            r'mkfs',
            r'dd',
            r'chmod\s+[0-7]{4}'
        ]
        if not command:
            return False
            
        # Allow safer patterns including redirects
        if not re.match(safe_pattern, command):
            return False

        # Check for dangerous patterns        
        return not any(re.search(p, command) for p in dangerous_patterns)

    def _add_to_history(self, prompt: str, command: str) -> None:
        """Add command to history with metadata"""
        self.command_history.append({
            "prompt": prompt,
            "command": command,
            "timestamp": datetime.now().isoformat(),
            "system": platform.system(),
            "executed": False
        })
        self._save_history()

    def execute_command(self, command: str, confirm_execution: bool = True) -> bool:
        """Safely execute a shell command"""
        try:
            if not self.validate_command(command):
                return False

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
        """Display command history"""
        if not self.command_history:
            console.print("[yellow]No command history available[/yellow]")
            return
            
        console.print("\n[bold]Command History:[/bold]")
        for entry in reversed(self.command_history[-limit:]):
            console.print(Panel(
                f"Prompt: {entry['prompt']}\nCommand: {entry['command']}\nTime: {entry['timestamp']}",
                border_style="blue"
            ))

    def run(self) -> None:
        """Interactive command generation loop with enhanced features"""
        # Display banner and welcome message
        console.print(f"[bold cyan]{BANNER}[/bold cyan]")
        console.print(f"[bold blue]BourguibaGPT[/bold blue] [cyan]v{VERSION}[/cyan]")
        console.print(f"[dim]Powered by Hugging Face - Model: {self.model_name}[/dim]")
        console.print("\n[italic]Type 'help' for available commands or 'exit' to quit[/italic]\n")
        
        while True:
            try:
                user_input = Prompt.ask(
                    "\n[bold magenta]🇹🇳 BourguibaGPT[/bold_magenta] [bold blue]→[/bold blue]"
                )
                
                if user_input.lower() in ['exit', 'quit']:
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                elif user_input.lower() == 'history':
                    self.show_history()
                elif user_input.lower().startswith('execute '):
                    command = user_input[8:].strip()
                    self.execute_command(command)
                else:
                    command = self.generate_command(user_input)
                    if command:
                        console.print(f"\n[green]Generated command:[/green]")
                        console.print(Panel(command["command"], style="bold white"))
                        
                        choice = Prompt.ask(
                            "\n[yellow]Type 'e' to execute the generated command and exit, or 'n' to return to the prompt:[/yellow]",
                            choices=["e", "n"],
                            default="n"
                        )
                        if choice.lower() == "e":
                            self.execute_command(command["command"], confirm_execution=False)
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

    def _show_help(self) -> None:
        """Display help information"""
        help_text = """[bold]Available Commands:[/bold]
        
        [cyan]help[/cyan] - Show this help message
        [cyan]history[/cyan] - Show command history
        [cyan]execute <command>[/cyan] - Execute a specific command
        [cyan]exit/quit[/cyan] - Exit BourguibaGPT
        
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

# Add parameter validation to parse_arguments
def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Enhanced Shell Command Generator")
    parser.add_argument("--model", default="microsoft/Phi-3.5-mini-instruct", help="Hugging Face model name")
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Generation temperature (0.0-1.0)",
        choices=[x/10 for x in range(11)]  # Restrict to valid range
    )
    parser.add_argument("--auto-execute", action="store_true", help="Auto-execute generated commands")
    parser.add_argument("--history-file", type=Path, help="Custom history file location")
    return parser.parse_args()

# Enhance error handling in main
def main() -> None:
    """Main entry point with improved error handling"""
    # Ask user about system specs to decide best model
    console.print("[bold cyan]Model Selection Wizard[/bold cyan]")
    console.print("We will ask some questions to figure out the best model for your system.\n")
    mem_gb = Prompt.ask("How many GB of system RAM do you have?", default="8")
    gpu = Prompt.ask("Do you have a GPU? (yes/no)", choices=["yes","no"], default="no")
    gpu_vram = "0"
    if gpu == "yes":
        gpu_vram = Prompt.ask("Approximate GPU VRAM (in GB)?", default="4")

    # Based on answers, pick a file or class
    chosen_file = "default"
    try:
        mem_gb_val = int(mem_gb)
        gpu_vram_val = int(gpu_vram)
        if gpu == "no" and mem_gb_val <= 8:
            chosen_file = "bourguibaT"
        elif gpu == "yes" and 4 <= gpu_vram_val <= 6:
            chosen_file = "bourguibaB_4_6"
        elif gpu == "yes" and gpu_vram_val > 6:
            chosen_file = "bourguibaB_starcoder2"
        else:
            # Fallback to Mistral as default if user has CPU or any GPU
            chosen_file = "bourguibaM"
    except:
        chosen_file = "bourguibaM"

    console.print(f"You selected: {chosen_file}\n")
    console.print("[bold cyan]Installing required dependencies now...[/bold cyan]")

    # Example install step
    subprocess.run("pip install transformers rich requests", shell=True)

    # Hypothetical: we import and install the correct model class
    if chosen_file == "bourguibaT":
        from bourguibaT import BourguibaT
        t = BourguibaT()
        t.install_model()
    elif chosen_file.startswith("bourguibaB"):
        from bourguibagpt.bourguibaB import BourguibaB
        b = BourguibaB(int(gpu_vram))
        b.install_model()
    else:
        from bourguibagpt.bourguibaM import BourguibaM
        m = BourguibaM()
        m.install_model()

    # Now proceed with original logic
    try:
        args = parse_arguments()
        generator = ShellCommandGenerator(
            model_name=args.model,
            temperature=args.temperature,
            auto_execute=args.auto_execute,
            history_file=args.history_file
        )
        generator.run()
    except Exception as e:
        console.print(f"[red]Initialization error: {e}[/red]")
        sys.exit(1)

if __name__ == '__main__':
    main()
