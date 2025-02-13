"""Tool for creating new projects."""

import os
import subprocess
import re
from pathlib import Path
from typing import Literal, Optional, Tuple
from rich.console import Console

from ..views import (
    ViewManager,
    ViewType,
    LogLevel,
    get_project_inputs
)

# Common shadcn components to install
SHADCN_COMPONENTS = [
    "accordion",
    "alert",
    "alert-dialog",
    "aspect-ratio",
    "avatar",
    "badge",
    "breadcrumb",
    "button",
    "calendar",
    "card",
    "carousel",
    "chart",
    "checkbox",
    "collapsible",
    "command",
    "context-menu",
    "dialog",
    "drawer",
    "dropdown-menu",
    "form",
    "hover-card",
    "input",
    "input-otp",
    "label",
    "menubar",
    "navigation-menu",
    "pagination",
    "popover",
    "progress",
    "radio-group",
    "resizable",
    "scroll-area",
    "select",
    "separator",
    "sheet",
    "sidebar",
    "skeleton",
    "slider",
    "sonner",
    "switch",
    "table",
    "tabs",
    "textarea",
    "toast",
    "toggle",
    "toggle-group",
    "tooltip"
]

def validate_project_name(name: str) -> bool:
    """Validate project name is in kebab-case."""
    return bool(re.match(r'^[a-z][a-z0-9-]*[a-z0-9]$', name))

def is_git_repo(path: str) -> bool:
    """Check if path is inside a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=path,
            capture_output=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def setup_python_project(project_path: Path, view_manager: ViewManager) -> tuple[bool, str]:
    """Set up a new Python project.
    
    Returns:
        tuple[bool, str]: (success, message)
        - success: True if successful, False otherwise
        - message: Description of what happened
    """
    try:
        # Create requirements.txt
        view_manager.debug_view.log(LogLevel.INFO, "Creating requirements.txt")
        requirements = """rich>=13.7.0
pydantic>=2.0.0
python-dotenv>=1.0.0"""
        
        with open(project_path / "requirements.txt", "w") as f:
            f.write(requirements)
            
        # Create and activate venv
        view_manager.debug_view.log(LogLevel.INFO, "Creating virtual environment")
        success, msg = view_manager.shell.run_command(
            ["python", "-m", "venv", "venv"], 
            cwd=str(project_path),
            capture_output=False  # Show output to user
        )
        if not success:
            return False, f"Failed to create virtual environment: {msg}"
            
        # Install requirements
        view_manager.debug_view.log(LogLevel.INFO, "Installing requirements")
        env = os.environ.copy()
        env["PATH"] = str(project_path / "venv" / "bin") + os.pathsep + env["PATH"]
        success, msg = view_manager.shell.run_command(
            ["pip", "install", "-r", "requirements.txt"], 
            cwd=str(project_path), 
            env=env,
            capture_output=False  # Show output to user
        )
        if not success:
            return False, f"Failed to install requirements: {msg}"
            
        return True, "Python project setup completed successfully"
        
    except Exception as e:
        return False, f"Error setting up Python project: {str(e)}"

def setup_nextjs_project(project_path: Path, view_manager: ViewManager) -> tuple[bool, str]:
    """Set up a new Next.js project.
    
    Returns:
        tuple[bool, str]: (success, message)
        - success: True if successful, False otherwise
        - message: Description of what happened
    """
    try:
        # Create Next.js project with interactive prompts
        view_manager.debug_view.log(LogLevel.INFO, "Creating Next.js project...")
        success, msg = view_manager.shell.run_command(
            ["npx", "create-next-app@latest", str(project_path)],
            capture_output=False  # Show output to user and allow interaction
        )
        if not success:
            return False, f"Failed to create Next.js project: {msg}"
            
        # Initialize shadcn-ui
        view_manager.debug_view.log(LogLevel.INFO, "Initializing shadcn...")
        success, msg = view_manager.shell.run_command(
            ["npx", "shadcn@latest", "init"], 
            cwd=str(project_path),
            capture_output=False  # Show output to user and allow interaction
        )
        if not success:
            return False, f"Failed to initialize shadcn: {msg}"
            
        # Install shadcn components
        view_manager.debug_view.log(LogLevel.INFO, "Installing shadcn components...")
        success, msg = view_manager.shell.run_command(
            ["npx", "shadcn@latest", "add", "-y"] + SHADCN_COMPONENTS, 
            cwd=str(project_path),
            capture_output=False  # Show output to user
        )
        if not success:
            view_manager.debug_view.log(LogLevel.WARNING, f"Failed to install components: {msg}")
                
        return True, "Next.js project setup completed successfully"
    except Exception as e:
        return False, f"Error setting up Next.js project: {str(e)}"

def _validate_inputs(
    base_location: str,
    project_name: str,
    project_type: str,
    view_manager: ViewManager
) -> Optional[str]:
    """Validate project creation inputs.
    
    Args:
        base_location: Base directory for the project
        project_name: Name of the project
        project_type: Type of project to create
        view_manager: View manager instance
        
    Returns:
        Optional[str]: Error message if validation fails, None if successful
    """
    # Validate base location is absolute
    if not os.path.isabs(base_location):
        return "Base location must be an absolute path"
        
    # Validate base location exists
    base_path = Path(base_location).resolve()
    if not base_path.exists():
        return f"Base location does not exist: {base_location}"
        
    # Validate project name
    if not validate_project_name(project_name):
        return "Project name must be in kebab-case (e.g., my-awesome-project)"
        
    # Check if project already exists
    project_path = base_path / project_name
    if project_path.exists():
        return f"Project directory already exists: {project_path}"
        
    # Check if inside git repo
    if is_git_repo(str(base_path)):
        return f"Base location is inside a git repository: {base_location}"
        
    return None

def _setup_project_by_type(
    project_path: Path,
    project_type: str,
    view_manager: ViewManager
) -> Optional[str]:
    """Set up project based on its type.
    
    Args:
        project_path: Path to the project directory
        project_type: Type of project to create
        view_manager: View manager instance
        
    Returns:
        Optional[str]: Error message if setup fails, None if successful
    """
    if project_type == "python":
        success, msg = setup_python_project(project_path, view_manager)
        if not success:
            return msg
    elif project_type == "nextjs":
        success, msg = setup_nextjs_project(project_path, view_manager)
        if not success:
            return msg
    return None

def _run_post_creation_tasks(
    project_path: Path,
    view_manager: ViewManager
) -> None:
    """Run tasks after project creation.
    
    Args:
        project_path: Path to the project directory
        view_manager: View manager instance
    """
    # Run genome validate
    view_manager.debug_view.log(LogLevel.INFO, "Running genome validate")
    success, msg = view_manager.shell.run_command(
        ["genome", "validate"], 
        cwd=str(project_path),
        capture_output=False  # Show output to user
    )
    if not success:
        view_manager.debug_view.log(LogLevel.WARNING, f"genome validate failed: {msg}")
        
    # Open in Cursor
    view_manager.debug_view.log(LogLevel.INFO, "Opening project in Cursor")
    success, msg = view_manager.shell.run_command(
        ["cursor", "--new-window", str(project_path)],
        capture_output=False  # Show output to user
    )
    if not success:
        view_manager.debug_view.log(LogLevel.WARNING, f"Failed to open project in Cursor: {msg}")

def create_project(
    base_location: Optional[str] = None,
    project_name: Optional[str] = None,
    project_type: Optional[Literal["empty", "python", "nextjs"]] = None
) -> Tuple[bool, str]:
    """Create a new project.
    
    Args:
        base_location: Base directory for the project (must be absolute path)
        project_name: Name of the project (in kebab-case)
        project_type: Type of project to create
        
    Returns:
        Tuple[bool, str]: (success, message)
        - success: True if successful, False otherwise
        - message: Description of what happened
    """
    view_manager = ViewManager()
    
    try:
        # Get inputs interactively if not provided
        if not all([base_location, project_name, project_type]):
            base_location, project_name, project_type = get_project_inputs()
            
        # Validate inputs
        if error := _validate_inputs(base_location, project_name, project_type, view_manager):
            return False, error
            
        # Create project directory
        project_path = Path(base_location).resolve() / project_name
        view_manager.debug_view.log(LogLevel.INFO, f"Creating project directory: {project_path}")
        project_path.mkdir(parents=True)
        
        # Set up project based on type
        if error := _setup_project_by_type(project_path, project_type, view_manager):
            return False, error
            
        # Run post-creation tasks
        _run_post_creation_tasks(project_path, view_manager)
        
        return True, f"Project {project_name} created successfully"
        
    except (OSError, IOError) as e:
        return False, f"System error creating project: {str(e)}"
    except Exception as e:
        return False, f"Error creating project: {str(e)}" 