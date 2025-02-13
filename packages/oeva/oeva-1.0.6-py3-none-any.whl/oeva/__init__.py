"""Eva - A friendly AI assistant for managing your projects."""

__version__ = "1.0.6"

from .eva import Eva, app, start_chat, show_welcome_message
from .config import OPENAI_MODEL, TOOLS
from .system_instructions import SystemInstructions
from .views import ViewManager
from .tools.tool_handler import ToolHandler

__all__ = [
    "Eva",
    "app",
    "start_chat",
    "show_welcome_message",
    "OPENAI_MODEL",
    "TOOLS",
    "SystemInstructions",
    "ViewManager",
    "ToolHandler",
] 