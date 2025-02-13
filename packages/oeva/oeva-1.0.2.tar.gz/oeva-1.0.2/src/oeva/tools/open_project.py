"""Tool for opening projects in Cursor."""

import subprocess
from pathlib import Path
from views import ViewManager

def open_project(project_path: str) -> tuple[bool, str]:
    """Open a project in Cursor.
    
    Args:
        project_path: The path to the project to open
        
    Returns:
        tuple[bool, str]: (success, message)
    """
    view_manager = ViewManager()
    
    try:
        # Resolve and validate path
        project_path = str(Path(project_path).resolve())
        if not Path(project_path).exists():
            raise ValueError(f"Project path does not exist: {project_path}")
            
        view_manager.debug_view.show_command(f"Opening project: {project_path}")
        
        # Open in Cursor
        if not view_manager.shell.run_command(["cursor", "--new-window", project_path]):
            raise RuntimeError("Failed to open project in Cursor")
            
        view_manager.debug_view.show_success(f"Project opened successfully: {project_path}")
        return True, f"Project opened successfully: {project_path}"
        
    except Exception as e:
        view_manager.debug_view.show_error(f"Error opening project: {str(e)}")
        return False, str(e) 