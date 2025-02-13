"""Tool for analyzing projects using genome."""

import subprocess
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from ..views import ViewManager

def _validate_project_path(project_path: Path) -> Optional[Dict[str, str]]:
    """Validate that the project path exists.
    
    Args:
        project_path: The path to validate
        
    Returns:
        Optional error dict if validation fails
    """
    if not project_path.exists():
        return {"error": f"Project path does not exist: {project_path}"}
    return None

def _run_genome_analyze(project_path: Path, view_manager: ViewManager) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, str]]]:
    """Run the genome analyze command.
    
    Args:
        project_path: The project path to analyze
        view_manager: The view manager instance
        
    Returns:
        Tuple of (analysis_results, error_dict)
    """
    view_manager.debug_view.show_command(f"Analyzing project: {project_path}")
    
    result = subprocess.run(
        ["genome", "analyze", "--json"],
        cwd=str(project_path),
        capture_output=True,
        text=True,
        check=False
    )
    
    if result.returncode != 0:
        return None, {"error": f"Failed to analyze project: {result.stderr}"}
        
    try:
        analysis = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        return None, {"error": f"Failed to parse analysis results: {str(e)}"}
        
    if not analysis.get("success"):
        return None, {"error": "Genome analysis failed"}
        
    return analysis, None

def _extract_findings(analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract findings from analysis results.
    
    Args:
        analysis: The genome analysis results
        
    Returns:
        List of findings
    """
    findings = []
    for genome_results in analysis["results"].values():
        for result in genome_results:
            if result.get("issues"):
                findings.extend(result["issues"])
    return findings

def _extract_git_info(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Extract git information from analysis results.
    
    Args:
        analysis: The genome analysis results
        
    Returns:
        Dict containing git information
    """
    git_info = {
        "has_git": False,
        "has_changes": False,
        "total_changes": 0,
        "lines_changed": 0
    }
    
    if "github-workflow" in analysis["results"]:
        for result in analysis["results"]["github-workflow"]:
            if result["gene"]["name"] == "git-repo":
                git_info["has_git"] = result["protein"]["isGitRepo"]
            elif result["gene"]["name"] == "git-changes" and result["protein"]["hasChanges"]:
                git_info["has_changes"] = True
                git_info["total_changes"] = result["protein"]["totalChanges"]
                git_info["lines_changed"] = result["protein"]["totalLinesChanged"]
                
    return git_info

def _determine_project_type(analysis: Dict[str, Any]) -> str:
    """Determine the project type from analysis results.
    
    Args:
        analysis: The genome analysis results
        
    Returns:
        Project type string
    """
    if "python-process" in analysis["results"]:
        return "python"
    elif "next-v1" in analysis["results"]:
        return "nextjs"
    return "unknown"

def _display_findings(findings: List[Dict[str, Any]], view_manager: ViewManager) -> None:
    """Display findings in the debug view.
    
    Args:
        findings: List of findings to display
        view_manager: The view manager instance
    """
    if findings:
        view_manager.debug_view.console.print("\n[bold cyan]Analysis Findings:[/bold cyan]")
        for finding in findings:
            view_manager.debug_view.console.print(f"[yellow]•[/yellow] {finding.get('message', 'No message')}")

def analyze_project(project_path: str) -> Dict[str, Any]:
    """Analyze a project using genome analyze command.
    
    Args:
        project_path: The path to the project to analyze
        
    Returns:
        Dict containing the analysis results or error information:
        - On success: {
            "success": true,
            "findings": [{"message": "...", "suggestions": [...]}],
            "stats": {
                "total_issues": int,
                "git_changes": int,
                "lines_changed": int
            },
            "project_info": {
                "path": str,
                "type": str,
                "has_git": bool,
                "has_changes": bool
            }
        }
        - On error: {"error": "error message"}
    """
    view_manager = ViewManager()
    
    try:
        # Resolve and validate path
        project_path = Path(project_path).resolve()
        if error := _validate_project_path(project_path):
            return error
            
        # Run genome analyze
        analysis, error = _run_genome_analyze(project_path, view_manager)
        if error:
            return error
            
        # Extract information
        findings = _extract_findings(analysis)
        git_info = _extract_git_info(analysis)
        project_type = _determine_project_type(analysis)
        
        # Display results
        view_manager.debug_view.show_success("Project analysis completed successfully")
        _display_findings(findings, view_manager)
        
        # Return analysis results
        return {
            "success": True,
            "findings": findings,
            "stats": {
                "total_issues": len(findings),
                "git_changes": git_info["total_changes"],
                "lines_changed": git_info["lines_changed"]
            },
            "project_info": {
                "path": str(project_path),
                "type": project_type,
                "has_git": git_info["has_git"],
                "has_changes": git_info["has_changes"]
            }
        }
        
    except (OSError, IOError) as e:
        view_manager.debug_view.show_error(f"System error analyzing project: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        view_manager.debug_view.show_error(f"Error analyzing project: {str(e)}")
        return {"error": str(e)} 