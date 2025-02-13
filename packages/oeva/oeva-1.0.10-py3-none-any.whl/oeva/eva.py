"""Eva CLI - A friendly AI assistant for managing your projects.

This module implements the main CLI interface and chat functionality for Eva,
using OpenAI's function calling capabilities to handle various project management tasks.
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from openai import OpenAI, OpenAIError, APIError, APIConnectionError, BadRequestError

import typer

from .config import OPENAI_MODEL, TOOLS
from .system_instructions import SystemInstructions
from .tools.tool_handler import ToolHandler
from .views import ViewManager

app = typer.Typer()
client = OpenAI()
system = SystemInstructions()
view_manager = ViewManager()
tool_handler = ToolHandler(view_manager)

class Eva:
    """Main Eva class for programmatic usage."""
    
    def __init__(self):
        """Initialize Eva with default configuration."""
        self.version = "1.0.9"  # Match version from pyproject.toml
        self.client = OpenAI()
        self.system = SystemInstructions()
        self.view_manager = ViewManager()
        self.tool_handler = ToolHandler(self.view_manager)
        
    def run(self):
        """Start an interactive chat session."""
        show_welcome_message()
        start_chat()

def format_tool_result(tool_call: Dict[str, Any], _result: Any, logs: str) -> str:
    """Format tool call result for chat display.
    
    Args:
        tool_call: The tool call information
        _result: The result from the tool execution (unused)
        logs: Execution logs
        
    Returns:
        str: Formatted result message for display
    """
    try:
        args = json.loads(tool_call.function.arguments)
        formatted_args = json.dumps(args, indent=2)
    except json.JSONDecodeError as e:
        formatted_args = f"Failed to parse arguments: {str(e)}"
        
    return f"""Tool Execution Summary
Tool: {tool_call.function.name}

Arguments:
```json
{formatted_args}
```

Result: ✅ Success

Logs:
```
{logs}
```"""

def format_tool_error(tool_call: Dict[str, Any], error: str, logs: str) -> str:
    """Format tool error for chat display.
    
    Args:
        tool_call: The tool call information
        error: The error message
        logs: Execution logs
        
    Returns:
        str: Formatted error message for display
    """
    try:
        args = json.loads(tool_call.function.arguments)
        formatted_args = json.dumps(args, indent=2)
    except json.JSONDecodeError as e:
        formatted_args = f"Failed to parse arguments: {str(e)}"
    
    return f"""❌ Tool Execution Failed

Tool: {tool_call.function.name}

Arguments:
```json
{formatted_args}
```

Error Message:
{error}

Logs:
```
{logs}
```"""

def handle_tool_calls(tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Handle tool calls from the OpenAI API.
    
    Args:
        tool_calls: List of tool calls to execute
        
    Returns:
        List[Dict[str, Any]]: List of tool results
    """
    results = []
    
    for tool_call in tool_calls:
        # Switch to debug view
        try:
            args = json.loads(tool_call.function.arguments)
        except json.JSONDecodeError as e:
            args = {"error": f"Failed to parse arguments: {str(e)}"}
            
        view_manager.start_tool(tool_call.function.name, args)
        
        try:
            # Handle tool call using tool handler
            result, error_msg = tool_handler.handle_tool(tool_call)
            
            # Get logs before switching back to chat view
            logs = view_manager.end_tool()
            
            if error_msg:
                # Format and show error in chat
                formatted_error = format_tool_error(tool_call, error_msg, logs)
                view_manager.add_chat_message("system", formatted_error)
                
                # Always append a response for the tool call, even if it failed
                results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": json.dumps({
                        "success": False,
                        "error": error_msg,
                        "logs": logs
                    })
                })
            else:
                # Format and show success in chat
                formatted_result = format_tool_result(tool_call, result, logs)
                view_manager.add_chat_message("system", formatted_result)
                
                # Add successful tool result
                results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": json.dumps({
                        "success": True,
                        "result": result,
                        "logs": logs
                    })
                })
            
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            # Handle expected errors
            logs = view_manager.end_tool()
            formatted_error = format_tool_error(tool_call, f"Data error: {str(e)}", logs)
            view_manager.add_chat_message("system", formatted_error)
            results.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": json.dumps({
                    "success": False,
                    "error": str(e),
                    "logs": logs
                })
            })
        except (APIError, APIConnectionError) as e:
            # Handle OpenAI API errors
            logs = view_manager.end_tool()
            formatted_error = format_tool_error(tool_call, f"API error: {str(e)}", logs)
            view_manager.add_chat_message("system", formatted_error)
            results.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": json.dumps({
                    "success": False,
                    "error": str(e),
                    "logs": logs
                })
            })
        except (OSError, IOError) as e:
            # Handle system/IO errors
            logs = view_manager.end_tool()
            formatted_error = format_tool_error(tool_call, f"System error: {str(e)}", logs)
            view_manager.add_chat_message("system", formatted_error)
            results.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": json.dumps({
                    "success": False,
                    "error": str(e),
                    "logs": logs
                })
            })
            
    return results

def show_welcome_message():
    """Show welcome message and available information."""
    view_manager.clear_chat_history()
    view_manager.chat_view.console.print("\n[bold blue]Welcome to Eva Chat! Type 'exit' to end the conversation.[/bold blue]\n")
    
    # Show discovered projects
    view_manager.chat_view.console.print("[bold cyan]Discovered Projects:[/bold cyan]")
    for name, path in system.available_projects.items():
        view_manager.chat_view.console.print(f"[green]•[/green] [bold]{name}[/bold]: {path}")
    view_manager.chat_view.console.print()
    
    # Show available project locations
    parent_dirs = {str(Path(path).parent) for path in system.available_projects.values()}
    view_manager.chat_view.console.print("[bold cyan]Available Project Locations:[/bold cyan]")
    for path in sorted(parent_dirs):
        view_manager.chat_view.console.print(f"[green]•[/green] {path}")
    view_manager.chat_view.console.print()

    # Show available tools
    view_manager.chat_view.console.print("[bold cyan]Available Tools:[/bold cyan]")
    for tool in TOOLS:
        name = tool["function"]["name"]
        description = tool["function"]["description"]
        view_manager.chat_view.console.print(f"[green]•[/green] [bold]{name}[/bold]: {description}")
    view_manager.chat_view.console.print()

def get_assistant_response(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Get response from OpenAI API.
    
    Args:
        messages: The conversation history
        
    Returns:
        Dict[str, Any]: The assistant's response message
        
    Raises:
        ValueError: If response format is invalid
        TypeError: If response data types are incorrect
        APIError: If OpenAI API returns an error
        APIConnectionError: If connection to OpenAI fails
    """
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            tools=TOOLS,
            stream=False
        )
        return response.choices[0].message
    except (APIError, APIConnectionError) as e:
        raise BadRequestError(message=f"OpenAI API error: {str(e)}", response=None, body=str(e)) from e

def handle_assistant_message(messages: List[Dict[str, Any]], assistant_message: Dict[str, Any]) -> None:
    """Handle the assistant's message and any tool calls.
    
    Args:
        messages: The conversation history
        assistant_message: The assistant's response message
    """
    # Add assistant's message to conversation history first
    messages.append(assistant_message)
    
    # Show content if it exists
    if assistant_message.content:
        view_manager.add_chat_message("assistant", assistant_message.content)
    
    # Handle any tool calls
    if assistant_message.tool_calls:
        # Handle tool calls and get results
        tool_results = handle_tool_calls(assistant_message.tool_calls)
        
        # Add tool results to conversation history
        messages.extend(tool_results)
        
        # Get final response after tool calls
        view_manager.chat_view.show_processing()
        try:
            final_message = get_assistant_response(messages)
            messages.append(final_message)
            if final_message.content:
                view_manager.add_chat_message("assistant", final_message.content)
        except (ValueError, TypeError) as e:
            error_msg = f"Failed to process final response: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")
        except (APIError, APIConnectionError) as e:
            error_msg = f"OpenAI API error in final response: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")
        except (OSError, IOError) as e:
            error_msg = f"System error in final response: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")

def process_user_input(messages: List[Dict[str, Any]], user_input: str) -> bool:
    """Process user input and get assistant response.
    
    Args:
        messages: The conversation history
        user_input: The user's input
        
    Returns:
        bool: True if chat should continue, False if it should end
    """
    if user_input.lower() == "exit":
        view_manager.chat_view.console.print("\n[bold blue]Goodbye! Have a great day![/bold blue]\n")
        return False
        
    # Add user message to conversation
    messages.append({"role": "user", "content": user_input})
    view_manager.add_chat_message("user", user_input)
    
    # Show thinking indicator
    view_manager.chat_view.show_thinking()
    
    try:
        # Get and handle assistant response
        assistant_message = get_assistant_response(messages)
        handle_assistant_message(messages, assistant_message)
    except (ValueError, TypeError) as e:
        error_msg = f"Failed to process OpenAI response: {str(e)}"
        view_manager.add_chat_message("system", f"❌ {error_msg}")
    except (APIError, APIConnectionError) as e:
        error_msg = f"OpenAI API error: {str(e)}"
        view_manager.add_chat_message("system", f"❌ {error_msg}")
    except (OSError, IOError) as e:
        error_msg = f"System error: {str(e)}"
        view_manager.add_chat_message("system", f"❌ {error_msg}")
    
    return True

def start_chat():
    """Start a chat session with Eva."""
    messages = [{
        "role": "system",
        "content": system.get_instructions()
    }]
    
    show_welcome_message()
    
    while True:
        try:
            # Get user input
            user_input = view_manager.chat_view.get_input()
            
            # Process input and get response
            if not process_user_input(messages, user_input):
                break
                
        except KeyboardInterrupt:
            view_manager.chat_view.console.print("\n[bold blue]Chat interrupted. Goodbye![/bold blue]\n")
            break
        except (OSError, IOError) as e:
            error_msg = f"System error in chat loop: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")
        except (APIError, APIConnectionError) as e:
            error_msg = f"API error in chat loop: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")
        except (ValueError, TypeError) as e:
            error_msg = f"Data error in chat loop: {str(e)}"
            view_manager.add_chat_message("system", f"❌ {error_msg}")
            # Don't break the chat loop on errors

@app.callback()
def callback():
    """Eva - A friendly AI assistant for managing your projects."""

@app.command()
def chat():
    """Start an interactive chat session with Eva."""
    show_welcome_message()
    start_chat()

def main():
    """Main entry point for the CLI."""
    app()

if __name__ == "__main__":
    main() 