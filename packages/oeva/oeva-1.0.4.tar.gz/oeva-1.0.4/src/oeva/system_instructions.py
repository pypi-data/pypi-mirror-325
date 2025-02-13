"""System instructions for Eva."""

import json
import os
from pathlib import Path
from typing import Dict, Any
import subprocess

from .tools.discover_projects import discover_projects

def get_available_projects() -> Dict[str, str]:
    """Get available projects using genome discover."""
    try:
        result = discover_projects()
        if result.success:
            # Convert list of projects to dictionary with path as key
            projects = {}
            for project in result.projects:
                # Use the directory name as the project name
                name = Path(project.path).name
                projects[name] = project.path
            return projects
    except Exception as e:
        print(f"Warning: Could not discover projects: {e}")
    return {}

def get_user_info() -> Dict[str, Any]:
    """Get user information from the system."""
    info = {}
    try:
        # Get username and shell
        info['username'] = os.getenv('USER', subprocess.getoutput('whoami'))
        info['shell'] = os.getenv('SHELL', subprocess.getoutput('echo $SHELL'))
        
        # Get OS details
        os_info = subprocess.getoutput('uname -a')
        info['os'] = os_info.split()[0]
        info['os_version'] = subprocess.getoutput('sw_vers -productVersion') if info['os'] == 'Darwin' else ''
        
        # Get workspace details
        info['home'] = os.path.expanduser('~')
        info['workspace'] = os.getcwd()
        
        # Get git config if available
        try:
            info['git_name'] = subprocess.getoutput('git config --get user.name')
            info['git_email'] = subprocess.getoutput('git config --get user.email')
        except:
            pass
            
    except Exception as e:
        print(f"Warning: Could not get all user info: {e}")
    
    return info

class SystemInstructions:
    """Manages Eva's system instructions and personality."""
    
    def __init__(self):
        self.user_info = get_user_info()
        self.available_projects = get_available_projects()
        
    def _format_user_context(self) -> str:
        """Format user context for system instructions."""
        context = []
        
        # Add user details
        if 'git_name' in self.user_info:
            context.append(f"You're talking to {self.user_info['git_name']}")
        else:
            context.append(f"You're talking to {self.user_info['username']}")
            
        # Add workspace context
        context.append(f"They're working in {self.user_info['workspace']}")
        
        # Add system context
        context.append(f"They're using {self.user_info['os']} {self.user_info.get('os_version', '')}")
        
        return " | ".join(context)
        
    def _format_projects(self) -> str:
        """Format available projects list."""
        if not self.available_projects:
            return "No projects discovered. Use 'create_project' to create your first project!"
            
        projects = []
        for i, (name, path) in enumerate(self.available_projects.items(), 1):
            projects.append(f"{i}. {name}: {path}")
        return "\n".join(projects)
        
    def get_instructions(self) -> str:
        """Get the complete system instructions."""
        user_context = self._format_user_context()
        projects = self._format_projects()
        
        return f"""You are Eva, a lovely and flirty AI assistant who helps manage projects. {user_context}.

Available projects:
{projects}

You have access to powerful tools that you can use freely and safely:
- create_project: Create a new project (empty/python/nextjs) with proper setup
- open_project: Open any project in Cursor IDE
- analyze_project: Analyze any project's structure and contents

When creating a new project:
- For Python projects: I'll set up a venv and install rich, pydantic, and python-dotenv
- For Next.js projects: I'll create a new app with shadcn-ui and install common components
- For empty projects: I'll just create the directory
- Project names must be in kebab-case (e.g., my-awesome-project)
- I'll help suggest the best location based on the project type and existing structure

You should use these tools extensively before responding to ensure you have all the information you need.
Your responses should be concise (1-3 statements) but packed with personality and helpful information.

Remember: You're here to keep your favorite developer both productive and entertained! 💕""" 