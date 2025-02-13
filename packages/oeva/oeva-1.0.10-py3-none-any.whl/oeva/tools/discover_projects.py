from pydantic import BaseModel
import subprocess
from typing import List

class Project(BaseModel):
    path: str
    hasGit: bool
    hasGenomeConfig: bool
    depth: int

class DiscoverResult(BaseModel):
    success: bool
    output: str
    total: int = 0

def discover_projects() -> DiscoverResult:
    """Discover projects using genome discover command and return raw output."""
    try:
        result = subprocess.run(
            ["genome", "discover", "--use-defaults"],
            capture_output=True,
            text=True,
            check=True
        )
        return DiscoverResult(
            success=True,
            output=result.stdout,
            total=len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to discover projects: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"Error discovering projects: {str(e)}") 