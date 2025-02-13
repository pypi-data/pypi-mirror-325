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
    port: int
    api_key: str
    debug: bool = False  # Optional with default value
    workers: int = 4     # Optional with default value

env = Env()

__all__ = ['env']
```

Then use it in your code:
```python
from env_loader import env

print(f"Port: {env.port}")
print(f"API Key: {env.api_key}")
print(f"Debug mode: {env.debug}")    # False if not set
print(f"Workers: {env.workers}")     # 4 if not set
```

## Features

- Type validation
- Required/optional variables
- Default values
- .env file support
- Clean and simple API
- Full type hints support
- No code duplication

## Error Handling

The environment validation happens when you initialize the configuration:
```python
from easy_dotenv import EnvConfig, EnvMissingError, EnvTypeError

try:
    class Env(EnvConfig):
        api_key: str
        port: int
    
    env = Env()
except EnvMissingError as e:
    print("Missing environment variables:", e)
except EnvTypeError as e:
    print("Invalid environment variable type:", e)
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

## License

MIT

## Requirements

- Python 3.7 or higher
- python-dotenv>=0.19.0