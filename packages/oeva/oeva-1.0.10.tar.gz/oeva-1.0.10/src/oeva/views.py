"""Views module for Eva CLI."""

import json
import os
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

class LogLevel(Enum):
    """Log levels for the debug view."""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"

@dataclass
class LogEntry:
    """A log entry in the debug view."""
    timestamp: datetime
    level: LogLevel
    message: str
    details: Optional[Dict] = None

class ViewType(Enum):
    """Types of views available."""
    CHAT = "chat"
    DEBUG = "debug"

class View(ABC):
    """Base class for views in Eva CLI."""
    
    def __init__(self):
        """Initialize the view with a console instance."""
        self.console = Console()
    
    def clear(self):
        """Clear the console screen."""
        self.console.clear()
    
    @abstractmethod
    def show(self):
        """Display the view's content."""
        pass

class ChatView(View):
    """Chat view for interactive conversations."""
    
    def show(self):
        """Display the chat view's content."""
        self.console.clear()
        self.console.print(Panel("Eva Chat", style="bold blue"))
    
    def show_message(self, role: str, content: str):
        """Show a chat message."""
        if not content:  # Skip empty messages
            return
            
        if role == "user":
            self.console.print("\n[bold]You:[/bold]")
        elif role == "system":
            self.console.print("\n[bold yellow]System:[/bold yellow]")
        else:
            self.console.print("\n[bold green]Eva:[/bold green]")
            
        # Strip rich formatting tags for cleaner display
        content = content.replace("[bold]", "").replace("[/bold]", "")
        content = content.replace("[bold red]", "").replace("[/bold red]", "")
        content = content.replace("[bold yellow]", "").replace("[/bold yellow]", "")
        content = content.replace("[bold cyan]", "").replace("[/bold cyan]", "")
        
        self.console.print(Markdown(content))
        
    def show_thinking(self):
        """Show thinking indicator."""
        self.console.print("\n[bold magenta]Eva is thinking...[/bold magenta]")
        
    def show_processing(self):
        """Show processing indicator."""
        self.console.print("\n[bold magenta]Eva is processing the results...[/bold magenta]")
        
    def get_input(self, prompt: str = "You") -> str:
        """Get user input."""
        return Prompt.ask(f"[bold]{prompt}[/bold]")

class DebugView(View):
    """Debug view for displaying logs and tool execution details."""
    
    def __init__(self):
        """Initialize the debug view with console and log storage."""
        super().__init__()
        self.logs: List[LogEntry] = []
        self._log_level_formats = {
            LogLevel.ERROR: ("[bold red]ERROR[/bold red]", "red"),
            LogLevel.WARNING: ("[bold yellow]WARN[/bold yellow]", "yellow"),
            LogLevel.SUCCESS: ("[bold green]SUCCESS[/bold green]", "green"),
            LogLevel.INFO: ("[bold blue]INFO[/bold blue]", "blue"),
            LogLevel.DEBUG: ("[bold]DEBUG[/bold]", "white"),
        }
        
    def log(self, level: LogLevel, message: str, details: Optional[Dict] = None):
        """Add a log entry."""
        try:
            entry = LogEntry(
                timestamp=datetime.now(),
                level=level,
                message=message,
                details=details
            )
            self.logs.append(entry)
            self._display_log_entry(entry)
        except Exception as e:
            # Fallback to simple error display if logging fails
            self.console.print(f"[bold red]ERROR[/bold red] Failed to log message: {str(e)}")
            self.console.print(f"Original message: {message}")
        
    def _display_log_entry(self, entry: LogEntry):
        """Display a log entry with appropriate formatting based on log level."""
        try:
            timestamp = entry.timestamp.strftime("%H:%M:%S")
            level_format = self._log_level_formats.get(entry.level, ("[bold]DEBUG[/bold]", "white"))
            self.console.print(f"[dim]{timestamp}[/dim] {level_format[0]} {entry.message}")
            
            if entry.details:
                if "code" in entry.details:
                    try:
                        self.console.print(Syntax(
                            entry.details["code"],
                            entry.details.get("language", "bash"),
                            theme="monokai"
                        ))
                    except Exception as e:
                        self.console.print(f"[dim]Failed to format code: {str(e)}[/dim]")
                        self.console.print(entry.details["code"])
                        
                if "output" in entry.details:
                    try:
                        self.console.print(Panel(
                            entry.details["output"],
                            border_style="dim"
                        ))
                    except Exception as e:
                        self.console.print(f"[dim]Failed to format output: {str(e)}[/dim]")
                        self.console.print(entry.details["output"])
                        
        except Exception as e:
            # Fallback to simple error display if formatting fails
            self.console.print(f"[bold red]ERROR[/bold red] Failed to display log entry: {str(e)}")
            self.console.print(f"Original entry: {entry}")
        
    def start_tool(self, name: str, args: Optional[dict] = None):
        """Start tool execution view."""
        self.logs = []  # Clear logs for new tool execution
        self.log(LogLevel.INFO, f"Starting tool execution: {name}")
        if args:
            try:
                formatted_args = json.dumps(args, indent=2)
                self.log(LogLevel.DEBUG, "Tool arguments:", {"code": formatted_args, "language": "json"})
            except Exception as e:
                self.log(LogLevel.ERROR, f"Failed to format tool arguments: {str(e)}")
                self.log(LogLevel.DEBUG, "Raw arguments:", {"output": str(args)})
        
    def show_command(self, cmd: str):
        """Show command being executed."""
        self.log(LogLevel.INFO, f"Executing command:", {"code": cmd})
        
    def show_output(self, output: str):
        """Show command output."""
        self.log(LogLevel.DEBUG, "Command output:", {"output": output})
        
    def show_error(self, error: str):
        """Show error message."""
        self.log(LogLevel.ERROR, error)
        
    def show_success(self, message: str):
        """Show success message."""
        self.log(LogLevel.SUCCESS, message)
        
    def get_logs_summary(self) -> str:
        """Get a summary of all logs for the current tool execution."""
        try:
            summary = []
            for entry in self.logs:
                timestamp = entry.timestamp.strftime("%H:%M:%S")
                summary.append(f"{timestamp} [{entry.level.value.upper()}] {entry.message}")
                if entry.details:
                    if "code" in entry.details:
                        summary.append(f"Code:\n{entry.details['code']}")
                    if "output" in entry.details:
                        summary.append(f"Output:\n{entry.details['output']}")
            return "\n".join(summary)
        except Exception as e:
            return f"Error generating logs summary: {str(e)}\nRaw logs: {str(self.logs)}"

    def show(self):
        """Display the debug view's content."""
        self.console.clear()
        self.console.print(Panel("Debug View", style="bold yellow"))
        for log in self.logs[-10:]:  # Show last 10 logs
            self._display_log_entry(log)

class InteractiveShell:
    """Interactive shell for running commands."""
    def __init__(self, debug_view: DebugView):
        self.debug_view = debug_view
        self.console = Console()
        
    def run_command(
        self, 
        cmd: List[str], 
        cwd: Optional[str] = None, 
        env: Optional[Dict[str, str]] = None,
        capture_output: bool = True
    ) -> Tuple[bool, str]:
        """Run a shell command and return success status and output.
        
        Args:
            cmd: Command to run as list of strings
            cwd: Working directory for command
            env: Environment variables
            capture_output: Whether to capture output or show it directly to user
        """
        try:
            self.debug_view.log(LogLevel.DEBUG, f"Running command: {' '.join(cmd)}")
            
            if capture_output:
                # Run with captured output for logging
                result = subprocess.run(
                    cmd,
                    cwd=cwd,
                    env=env,
                    capture_output=True,
                    text=True
                )
                
                # Log output
                if result.stdout:
                    self.debug_view.log(LogLevel.DEBUG, "Command output:", {"output": result.stdout})
                if result.stderr:
                    self.debug_view.log(LogLevel.WARNING if result.returncode == 0 else LogLevel.ERROR, 
                                      "Command error:", {"output": result.stderr})
                    
                return result.returncode == 0, result.stdout if result.returncode == 0 else result.stderr
            else:
                # Run with direct output to user terminal
                result = subprocess.run(
                    cmd,
                    cwd=cwd,
                    env=env,
                    text=True
                )
                return result.returncode == 0, ""
                
        except Exception as e:
            error_msg = str(e)
            self.debug_view.log(LogLevel.ERROR, f"Command failed: {error_msg}")
            return False, error_msg
            
    def get_input(self, prompt: str = "") -> str:
        """Get input from the user with an optional prompt."""
        self.debug_view.log(LogLevel.INFO, f"Waiting for user input: {prompt}")
        response = self.console.input(prompt)
        self.debug_view.log(LogLevel.INFO, f"User input received: {response}")
        return response

class ViewManager:
    """Manages transitions between different views."""
    def __init__(self):
        self.chat_view = ChatView()
        self.debug_view = DebugView()
        self.current_view = ViewType.CHAT
        self.shell = InteractiveShell(self.debug_view)
        self.chat_history: List[Tuple[str, str]] = []
        
    def switch_to(self, view_type: ViewType):
        """Switch to a different view."""
        if view_type != self.current_view:
            if view_type == ViewType.CHAT:
                self.chat_view.clear()
                # Restore chat history
                for role, content in self.chat_history:
                    self.chat_view.show_message(role, content)
            else:
                self.debug_view.clear()
            self.current_view = view_type
            
    def start_tool(self, name: str, args: Optional[dict] = None):
        """Start tool execution and switch to debug view."""
        self.switch_to(ViewType.DEBUG)
        self.debug_view.start_tool(name, args)
        
    def end_tool(self) -> str:
        """End tool execution and switch back to chat view.
        
        Returns:
            str: Summary of all logs for the tool execution
        """
        logs_summary = self.debug_view.get_logs_summary()
        self.switch_to(ViewType.CHAT)
        return logs_summary
        
    def add_chat_message(self, role: str, content: str):
        """Add a message to chat history and display if in chat view."""
        self.chat_history.append((role, content))
        if self.current_view == ViewType.CHAT:
            self.chat_view.show_message(role, content)
            
    def clear_chat_history(self):
        """Clear chat history."""
        self.chat_history = []
        if self.current_view == ViewType.CHAT:
            self.chat_view.clear()
            
    def get_current_view(self) -> Union[ChatView, DebugView]:
        """Get the current active view."""
        return self.chat_view if self.current_view == ViewType.CHAT else self.debug_view

def get_project_inputs() -> tuple[str, str, str]:
    """Get project creation inputs interactively."""
    console = Console()
    
    # Get project type
    project_type = Prompt.ask(
        "[bold]Project Type[/bold]",
        choices=["empty", "python", "nextjs"],
        default="python"
    )
    
    # Get project name
    while True:
        project_name = Prompt.ask(
            "[bold]Project Name[/bold] (kebab-case)",
            default="my-awesome-project"
        )
        if project_name.replace("-", "").isalnum() and "-" in project_name:
            break
        console.print("[red]Project name must be in kebab-case (e.g., my-awesome-project)[/red]")
    
    # Get base location
    while True:
        base_location = Prompt.ask(
            "[bold]Base Location[/bold] (absolute path)",
            default=os.path.expanduser("~/projects")
        )
        if os.path.isabs(base_location):
            break
        console.print("[red]Base location must be an absolute path[/red]")
    
    return base_location, project_name, project_type 