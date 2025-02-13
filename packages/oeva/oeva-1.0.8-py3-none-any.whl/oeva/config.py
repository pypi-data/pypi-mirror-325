"""Configuration module for Eva."""

import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load YAML config
config_path = Path(__file__).parent / "config" / "settings.yaml"
with open(config_path) as f:
    config = yaml.safe_load(f)

# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = config["openai"]["model"]
OPENAI_STREAM = config["openai"]["stream"]

# Eva personality settings
EVA_PERSONALITY = config["eva"]["personality"]

# Tool settings
TOOLS = config["tools"] 