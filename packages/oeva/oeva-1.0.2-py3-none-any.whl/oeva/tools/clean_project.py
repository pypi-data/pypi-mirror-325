"""Tool for cleaning/deleting projects."""

import shutil
from pathlib import Path
from views import ViewManager, LogLevel

def clean_project(project_path: str) -> tuple[bool, str]:
    """Clean (delete) a project directory after user confirmation.
    
    Args:
        project_path: The path to the project to delete
        
    Returns:
        tuple[bool, str]: (success, message)
        - success: True if successful, False otherwise
        - message: Description of what happened
    """
    view_manager = ViewManager()
    
    try:
        # Resolve and validate path
        project_path = Path(project_path).resolve()
        if not project_path.exists():
            return False, f"Project path does not exist: {project_path}"
            
        view_manager.debug_view.log(LogLevel.WARNING, f"About to delete project directory: {project_path}")
        view_manager.debug_view.log(LogLevel.WARNING, "This action cannot be undone!")
        
        # Get user confirmation
        confirmation = view_manager.shell.get_input("Are you sure you want to delete this directory? [y/N] ")
        if confirmation.lower() != 'y':
            view_manager.debug_view.log(LogLevel.INFO, "Operation cancelled by user")
            return True, "Operation cancelled by user"
            
        # Delete directory
        view_manager.debug_view.log(LogLevel.INFO, "Deleting project directory...")
        if project_path.is_file():
            project_path.unlink()
        else:
            shutil.rmtree(project_path)
            
        view_manager.debug_view.log(LogLevel.SUCCESS, "Project directory deleted successfully")
        return True, f"Project directory deleted successfully: {project_path}"
        
    except Exception as e:
        error_msg = f"Error deleting project: {str(e)}"
        view_manager.debug_view.log(LogLevel.ERROR, error_msg)
        return False, error_msg 