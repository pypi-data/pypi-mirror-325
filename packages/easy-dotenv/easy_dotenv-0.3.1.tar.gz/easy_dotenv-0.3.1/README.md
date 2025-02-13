# easy-dotenv

[![PyPI version](https://badge.fury.io/py/easy-dotenv.svg)](https://badge.fury.io/py/easy-dotenv)
[![Python Versions](https://img.shields.io/pypi/pyversions/easy-dotenv.svg)](https://pypi.org/project/easy-dotenv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple and type-safe environment variables management for Python.

## Installation

```bash
pip install easy-dotenv
```

## Usage

You can organize your environment variables by modules. For example:

```python
# env_loader.py
from easy_dotenv import EnvConfig

class BaseEnv(EnvConfig):
    # Base application settings
    port: int
    api_key: str
    debug: bool = False     # Optional with default value
    workers: int = 4        # Optional with default value
    
class TelegramEnv(EnvConfig):
    # Telegram-specific settings
    bot_token: str
    chat_id: str
    channel_id: str = ''    # Optional with default empty string

# Both classes will look for .env in project root
base = BaseEnv('..')
telegram = TelegramEnv('..')

__all__ = ['base', 'telegram']
```

Then use it in your code:
```python
from env_loader import base, telegram

# Access base configuration
print(f"Port: {base.port}")
print(f"API Key: {base.api_key}")
print(f"Debug mode: {base.debug}")    # False if not set
print(f"Workers: {base.workers}")     # 4 if not set

# Access Telegram configuration
print(f"Bot Token: {telegram.bot_token}")
print(f"Chat ID: {telegram.chat_id}")
print(f"Channel ID: {telegram.channel_id}")  # Empty string if not set
```

Your `.env` file:
```env
# Base
PORT=8000
API_KEY=your_api_key_here
DEBUG=true

# Telegram
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
CHANNEL_ID=optional_channel_id
```

## Features

- Type validation with automatic conversion
- Required and optional variables
- Default values
- .env file support with flexible path resolution
- Clean and simple API
- Full type hints support
- No code duplication

## .env File Location

The path to the `.env` file can be specified in several ways:

- `'.env'` - Look for `.env` in the same directory as the config file
- `'..'` - Look for `.env` in the project root (where pyproject.toml/setup.py is located)
- `'config/.env'` - Look in a subdirectory
- `'../.env'` - Look in the parent directory
- `None` - Use python-dotenv's default behavior

## Type Conversion

The library automatically converts environment variables to the specified types:

```python
class Env(EnvConfig):
    # String values (no conversion needed)
    api_key: str
    database_url: str
    
    # Integer values
    port: int                # "8000" -> 8000
    workers: int = 4         # Default: 4
    
    # Boolean values
    debug: bool = False      # Default: False
    verbose: bool            # "true"/"1" -> True, "false"/"0" -> False
```

## Error Handling

The environment validation happens when you initialize the configuration:
```python
from easy_dotenv import EnvConfig, EnvMissingError, EnvTypeError, EnvFileNotFoundError

try:
    class Env(EnvConfig):
        api_key: str         # Required
        port: int           # Required
        debug: bool = False  # Optional
    
    env = Env('..')  # Look for .env in project root
except EnvMissingError as e:
    print("Missing environment variables:", e)
except EnvTypeError as e:
    print("Invalid environment variable type:", e)
except EnvFileNotFoundError as e:
    print("Could not find .env file:", e)  # Wrong path or no project root found
```

## Development

### Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/MacOS
# or
# venv\Scripts\activate  # Windows

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=easy_dotenv
```

The test suite includes:
- Required variables validation
- Optional variables with defaults
- Type conversion (including boolean values)
- Error handling for missing variables
- Error handling for invalid types
- Mixed required and optional variables

## License

MIT

## Requirements

- Python 3.7 or higher
- python-dotenv>=0.19.0