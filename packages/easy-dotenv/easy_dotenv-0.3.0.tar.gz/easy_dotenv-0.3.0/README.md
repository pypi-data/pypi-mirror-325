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

Create an environment configuration file (e.g., `env_loader.py`):
```python
from easy_dotenv import EnvConfig

class Env(EnvConfig):
    # Required variables (will raise EnvMissingError if not set)
    port: int
    api_key: str
    
    # Optional variables with default values
    debug: bool = False
    workers: int = 4

env = Env('..')  # Look for .env file in project root (see .env File Location below)

__all__ = ['env']
```

Then use it in your code:
```python
from env_loader import env

print(f"Port: {env.port}")           # Required, must be set in environment or .env
print(f"API Key: {env.api_key}")     # Required, must be set in environment or .env
print(f"Debug mode: {env.debug}")    # Optional, False if not set
print(f"Workers: {env.workers}")     # Optional, 4 if not set
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