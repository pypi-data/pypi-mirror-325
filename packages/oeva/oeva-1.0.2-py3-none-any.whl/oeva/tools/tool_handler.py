"""Tool handler for managing all tool executions."""

from typing import Dict, Any, List, Optional, Tuple
import json
from views import ViewManager
from .create_project import create_project
from .open_project import open_project
from .analyze_project import analyze_project
from .release_project import release_project
from .clean_project import clean_project

class ToolHandler:
    def __init__(self, view_manager: ViewManager):
        self.view_manager = view_manager
        self.tools = {
            "create_project": self._handle_create_project,
            "open_project": self._handle_open_project,
            "analyze_project": self._handle_analyze_project,
            "release_project": self._handle_release_project,
            "clean_project": self._handle_clean_project
        }
    
    def handle_tool(self, tool_call: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle a tool call and return result and error if any.
        
        Returns:
            Tuple[Dict[str, Any], Optional[str]]: (result, error_message)
        """
        function_name = tool_call.function.name
        if function_name not in self.tools:
            return {"success": False, "message": f"Unknown tool: {function_name}"}, f"Unknown tool: {function_name}"
            
        handler = self.tools[function_name]
        try:
            arguments = json.loads(tool_call.function.arguments)
            return handler(arguments)
        except Exception as e:
            return {"success": False, "message": str(e)}, str(e)
    
    def _handle_create_project(self, arguments: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle create_project tool."""
        success, msg = create_project(**arguments)
        result = {
            "success": success,
            "message": msg
        }
        return result, None if success else msg
    
    def _handle_open_project(self, arguments: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle open_project tool."""
        success, msg = open_project(**arguments)
        result = {
            "success": success,
            "message": msg
        }
        return result, None if success else msg
    
    def _handle_analyze_project(self, arguments: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle analyze_project tool."""
        result = analyze_project(**arguments)
        if isinstance(result, dict) and "error" in result:
            return {"success": False, "message": result["error"]}, result["error"]
        return {"success": True, "data": result}, None
    
    def _handle_release_project(self, arguments: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle release_project tool."""
        result = release_project(**arguments)
        # If result contains error-indicating phrases, treat as error
        error_indicators = ["failed", "error", "not a git repository", "no changes", "git config"]
        is_error = any(indicator in result.lower() for indicator in error_indicators)
        
        if is_error:
            return {"success": False, "message": result}, result
        return {"success": True, "message": result}, None
        
    def _handle_clean_project(self, arguments: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
        """Handle clean_project tool."""
        success, msg = clean_project(**arguments)
        result = {
            "success": success,
            "message": msg
        }
        return result, None if success else msg 