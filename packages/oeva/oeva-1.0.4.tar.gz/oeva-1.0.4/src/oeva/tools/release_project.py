"""Tool for releasing projects with structured commit messages."""

import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
from ..views import ViewManager, LogLevel
import openai
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

# Load environment variables
load_dotenv()

class CommitMessage(BaseModel):
    commitTitle: str
    commitBody: str

def validate_git_repo(project_path: str, view_manager: ViewManager) -> Tuple[bool, Optional[str]]:
    """Validate that the path is a git repository and has proper setup."""
    try:
        path = Path(project_path).resolve()
        
        view_manager.debug_view.log(LogLevel.INFO, "Validating project path...")
        # Check if path exists
        if not path.exists():
            return False, f"Project path does not exist: {path}"
            
        # Check if it's a directory
        if not path.is_dir():
            return False, f"Project path is not a directory: {path}"
            
        view_manager.debug_view.log(LogLevel.INFO, "Checking git repository...")
        # Check if it's a git repository
        git_dir = path / ".git"
        if not git_dir.exists() or not git_dir.is_dir():
            return False, f"Not a git repository: {path}"
            
        # Check if git is initialized properly
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=str(path),
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return False, f"Invalid git repository: {result.stderr}"
            
        view_manager.debug_view.log(LogLevel.INFO, "Checking git configuration...")
        # Check if user.name and user.email are configured
        for config in ["user.name", "user.email"]:
            result = subprocess.run(
                ["git", "config", "--get", config],
                cwd=str(path),
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                return False, f"Git {config} not configured. Please run:\ngit config --global {config} \"Your {config.split('.')[1]}\""
        
        view_manager.debug_view.log(LogLevel.SUCCESS, "Git repository validation successful")
        return True, None
        
    except Exception as e:
        return False, f"Error validating git repository: {str(e)}"

def run_git_command(cmd: List[str], cwd: str, view_manager: ViewManager, check_output: bool = True) -> Tuple[bool, str, str]:
    """Run a git command in the specified directory."""
    try:
        view_manager.debug_view.log(LogLevel.DEBUG, f"Running git command: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        
        if result.stdout.strip():
            view_manager.debug_view.log(LogLevel.DEBUG, f"Command output:\n{result.stdout.strip()}")
        
        if result.stderr.strip():
            view_manager.debug_view.log(LogLevel.WARNING if not check_output else LogLevel.ERROR, f"Command error:\n{result.stderr.strip()}")
        
        if check_output and result.returncode != 0:
            return False, "", result.stderr
            
        return True, result.stdout, result.stderr
        
    except Exception as e:
        view_manager.debug_view.log(LogLevel.ERROR, f"Command failed: {str(e)}")
        return False, "", str(e)

def _parse_git_status_line(line: str) -> Optional[str]:
    """Parse a single line of git status output.
    
    Args:
        line: The git status line to parse
        
    Returns:
        Optional[str]: Formatted change description or None if line is empty
    """
    if not line.strip():
        return None
        
    status_code = line[:2]
    file_path = line[3:]
    
    status_map = {
        "??": lambda p: f"Added new file: {p}",
        " M": lambda p: f"Modified: {p}",
        "M ": lambda p: f"Modified: {p}",
        " D": lambda p: f"Deleted: {p}",
        "D ": lambda p: f"Deleted: {p}",
        "R ": lambda p: f"Renamed: {p.split(' -> ')[0]} -> {p.split(' -> ')[1]}"
    }
    
    return status_map.get(status_code, lambda p: f"Changed: {p}")(file_path)

def _get_git_status_output(project_path: str, view_manager: ViewManager) -> Tuple[str, str]:
    """Get git status output.
    
    Args:
        project_path: Path to the git repository
        view_manager: View manager instance
        
    Returns:
        Tuple[str, str]: Status output and diff output
        
    Raises:
        RuntimeError: If git commands fail
    """
    # Get status summary
    success, status_out, status_err = run_git_command(
        ["git", "status", "--porcelain"],
        project_path,
        view_manager
    )
    if not success:
        raise RuntimeError(f"Failed to get git status: {status_err}")
        
    # Get detailed diff
    success, diff_out, diff_err = run_git_command(
        ["git", "diff", "HEAD"],
        project_path,
        view_manager
    )
    if not success:
        raise RuntimeError(f"Failed to get git diff: {diff_err}")
        
    return status_out, diff_out

def get_git_status(project_path: str, view_manager: ViewManager) -> Tuple[bool, List[str], str]:
    """Get git status and determine if there are changes.
    
    Args:
        project_path: Path to the git repository
        view_manager: View manager instance
        
    Returns:
        Tuple[bool, List[str], str]: (has_changes, change_descriptions, diff)
        
    Raises:
        RuntimeError: If git commands fail
    """
    view_manager.debug_view.log(LogLevel.INFO, "Checking git status...")
    
    # Get git status and diff output
    status_out, diff_out = _get_git_status_output(project_path, view_manager)
    
    # If no output from git status, there are no changes
    if not status_out.strip():
        view_manager.debug_view.log(LogLevel.INFO, "No changes detected in working directory")
        return False, [], ""
        
    view_manager.debug_view.log(LogLevel.INFO, "Getting detailed diff...")
    
    # Parse status into readable changes
    changes = []
    for line in status_out.splitlines():
        if change := _parse_git_status_line(line):
            changes.append(change)
            
    return True, changes, diff_out

def get_commit_message(project_path: str, changes: List[str], diff: str, view_manager: ViewManager) -> CommitMessage:
    """Get structured commit message from OpenAI based on git changes."""
    view_manager.debug_view.log(LogLevel.INFO, "Generating commit message using OpenAI...")
    client = openai.OpenAI()
    
    try:
        # Prepare a summary of changes for the model
        changes_summary = "\n".join(changes)
        diff_preview = diff[:1000] if len(diff) > 1000 else diff  # Limit diff size
        
        view_manager.debug_view.log(LogLevel.DEBUG, "Sending request to OpenAI...")
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a commit message generator. Generate a concise and descriptive commit message based on the git changes. The commit title should be under 50 characters."
                },
                {
                    "role": "user",
                    "content": f"Generate a commit message for these changes:\n\nChanged files:\n{changes_summary}\n\nDiff preview:\n{diff_preview}"
                }
            ],
            response_format={
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "commitTitle": {
                            "type": "string",
                            "description": "The commit title (under 50 characters)"
                        },
                        "commitBody": {
                            "type": "string",
                            "description": "The detailed commit message body"
                        }
                    },
                    "required": ["commitTitle", "commitBody"],
                    "additionalProperties": false
                }
            }
        )
        
        response_content = json.loads(completion.choices[0].message.content)
        commit_msg = CommitMessage(**response_content)
        view_manager.debug_view.log(LogLevel.SUCCESS, f"Generated commit message:\nTitle: {commit_msg.commitTitle}\nBody: {commit_msg.commitBody}")
        return commit_msg
        
    except Exception as e:
        view_manager.debug_view.log(LogLevel.ERROR, f"Failed to generate commit message: {str(e)}")
        raise RuntimeError(f"Failed to generate commit message: {str(e)}")

def check_git_origin(project_path: str, view_manager: ViewManager) -> Optional[str]:
    """Check if git origin is set and return setup command if not."""
    view_manager.debug_view.log(LogLevel.INFO, "Checking git remote origin...")
    success, output, error = run_git_command(
        ["git", "remote", "get-url", "origin"],
        project_path,
        view_manager,
        check_output=False
    )
    if not success or not output.strip():
        view_manager.debug_view.log(LogLevel.WARNING, "Git remote origin not configured")
        return "git remote add origin <repository-url>"
    
    view_manager.debug_view.log(LogLevel.SUCCESS, f"Found git remote origin: {output.strip()}")
    return None

def release_project(project_path: str) -> str:
    """Release a project by committing and pushing changes."""
    view_manager = ViewManager()
    
    try:
        view_manager.debug_view.log(LogLevel.INFO, f"Starting project release for: {project_path}")
        
        # Validate git repository
        is_valid, error_msg = validate_git_repo(project_path, view_manager)
        if not is_valid:
            view_manager.debug_view.log(LogLevel.ERROR, f"Validation failed: {error_msg}")
            raise ValueError(error_msg)
            
        # Check for changes before proceeding
        has_changes, changes, diff = get_git_status(project_path, view_manager)
        
        if not has_changes:
            msg = "No changes to commit - working tree clean"
            view_manager.debug_view.log(LogLevel.INFO, msg)
            return msg
            
        # Show detected changes
        view_manager.debug_view.log(LogLevel.INFO, "Changes to be committed:")
        for change in changes:
            view_manager.debug_view.log(LogLevel.INFO, f"  {change}")
            
        # Stage all changes
        view_manager.debug_view.log(LogLevel.INFO, "Staging changes...")
        success, _, error = run_git_command(
            ["git", "add", "--all"],
            project_path,
            view_manager
        )
        if not success:
            raise RuntimeError(f"Failed to stage changes: {error}")
            
        # Get structured commit message
        commit_data = get_commit_message(project_path, changes, diff, view_manager)
        
        # Commit changes
        view_manager.debug_view.log(LogLevel.INFO, "Creating commit...")
        commit_message = f"{commit_data.commitTitle}\n\n{commit_data.commitBody}"
        success, _, error = run_git_command(
            ["git", "commit", "-m", commit_message],
            project_path,
            view_manager
        )
        if not success:
            raise RuntimeError(f"Failed to commit changes: {error}")
            
        # Check if origin is set
        if origin_setup := check_git_origin(project_path, view_manager):
            msg = f"Changes committed successfully. To push changes, first set up git origin:\n{origin_setup}"
            view_manager.debug_view.log(LogLevel.WARNING, msg)
            return msg
            
        # Push changes
        view_manager.debug_view.log(LogLevel.INFO, "Pushing changes to origin...")
        success, _, error = run_git_command(
            ["git", "push", "origin", "HEAD"],
            project_path,
            view_manager
        )
        if not success:
            raise RuntimeError(f"Failed to push changes: {error}")
            
        msg = f"Project released successfully:\n- Commit: {commit_data.commitTitle}\n- Changes pushed to origin\n\nChanged files:\n" + "\n".join(f"- {change}" for change in changes)
        view_manager.debug_view.log(LogLevel.SUCCESS, msg)
        return msg
        
    except Exception as e:
        error_msg = f"Error releasing project: {str(e)}"
        view_manager.debug_view.log(LogLevel.ERROR, error_msg)
        return error_msg 