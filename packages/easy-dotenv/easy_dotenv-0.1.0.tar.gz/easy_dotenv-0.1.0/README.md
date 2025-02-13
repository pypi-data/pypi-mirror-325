# easy-dotenv

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

## License

MIT