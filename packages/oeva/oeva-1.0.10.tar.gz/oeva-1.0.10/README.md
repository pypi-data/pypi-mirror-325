# oeva

Eva - A friendly AI assistant for managing your projects through a simple CLI interface.

## Features

- 🤖 AI-powered project management
- 📁 Project discovery and organization
- 🔍 Project analysis and validation
- 🚀 Interactive project creation
- 🔄 Git integration and release management

## Prerequisites

1. Python 3.8 or higher
2. OpenAI API key (get one at https://platform.openai.com/api-keys)

## Installation

Install Eva globally using pip:

```bash
pip install oeva
```

Set up your OpenAI API key:

```bash
# Add to your shell profile (~/.zshrc, ~/.bashrc, etc.)
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Start an interactive chat session with Eva:

```bash
oeva chat
```

Eva will help you:
- Create new projects with proper setup
- Open projects in your IDE
- Analyze project structure and dependencies
- Manage git repositories and releases
- And much more!

## Example Conversation

```
> oeva chat

Welcome to Eva Chat! Type 'exit' to end the conversation.

You: Create a new Python project called my-awesome-api
Eva: I'll help you create a new Python project with all the essentials! 💫

Creating project: my-awesome-api...
✓ Created directory structure
✓ Set up virtual environment
✓ Installed base dependencies
✓ Added README.md and .gitignore
✓ Initialized git repository

Your project is ready! Would you like me to open it in your IDE?

You: Yes please!
Eva: Opening my-awesome-api in Cursor... Done! 🚀

Let me know if you need help setting up anything else!

You: exit
Goodbye! Have a great day! ✨
```

## License

MIT License 