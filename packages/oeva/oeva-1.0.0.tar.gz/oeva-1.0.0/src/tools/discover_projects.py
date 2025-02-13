from pydantic import BaseModel
import json
import subprocess
from typing import List

class Project(BaseModel):
    path: str
    hasGit: bool
    hasGenomeConfig: bool
    depth: int

class DiscoverResult(BaseModel):
    success: bool
    projects: List[Project]
    total: int

def discover_projects() -> DiscoverResult:
    """Discover projects using genome discover command."""
    try:
        result = subprocess.run(
            ["genome", "discover", "--json", "--use-defaults"],
            capture_output=True,
            text=True,
            check=True
        )
        return DiscoverResult.model_validate_json(result.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to discover projects: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"Error discovering projects: {str(e)}") 