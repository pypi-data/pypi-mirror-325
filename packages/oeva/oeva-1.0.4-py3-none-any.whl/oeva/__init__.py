"""Eva - AI Assistant and Project Management Tool."""

from .eva import main, Eva, app, start_chat, show_welcome_message
from .config import OPENAI_MODEL, TOOLS
from .system_instructions import SystemInstructions
from .views import ViewManager
from .tools.tool_handler import ToolHandler

__version__ = "1.0.4"
__all__ = [
    "main",
    "Eva",
    "app",
    "start_chat",
    "show_welcome_message",
    "OPENAI_MODEL",
    "TOOLS",
    "SystemInstructions",
    "ViewManager",
    "ToolHandler"
] 