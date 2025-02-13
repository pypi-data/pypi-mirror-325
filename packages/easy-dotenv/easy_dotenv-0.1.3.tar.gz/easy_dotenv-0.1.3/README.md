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

```python
from easy_dotenv import EnvLoader

env = EnvLoader.load(
    # Required variables
    database_url=str,
    port=int,
    
    # Optional variables with defaults
    debug=(bool, False),
    workers=(int, 4)
)

# Access your environment variables
print(env.database_url)
print(env.port)
print(env.debug)  # False if not set
print(env.workers)  # 4 if not set
```

## Features

- Type validation
- Required/optional variables
- Default values
- .env file support
- Clean and simple API
- Type hints support

## Error Handling

```python
from easy_dotenv import EnvLoader, EnvMissingError, EnvTypeError

try:
    env = EnvLoader.load(
        api_key=str,
        port=int
    )
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