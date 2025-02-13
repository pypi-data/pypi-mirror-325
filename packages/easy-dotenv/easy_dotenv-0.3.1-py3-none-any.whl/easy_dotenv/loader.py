import os
from typing import TypeVar, Any, cast, Type, Optional, Union
from dataclasses import make_dataclass
from dotenv import load_dotenv
from pathlib import Path
from .types import RuntimeEnvironment, EnvVarsDict, T
from .exceptions import EnvError, EnvTypeError, EnvMissingError, EnvFileNotFoundError

def create_env_class(**env_vars: EnvVarsDict) -> Type[Any]:
    """Create a dataclass based on environment variables"""
    fields = [
        (name, var_type if not isinstance(var_type, tuple) else var_type[0])
        for name, var_type in env_vars.items()
    ]
    return make_dataclass('GeneratedEnv', fields)

class Environment(RuntimeEnvironment):
    """Runtime environment container with type information"""
    def __init__(self, **kwargs: Any):
        self.__dict__.update(kwargs)

    def __getattr__(self, name: str) -> Any:
        raise AttributeError(f"Environment variable '{name}' is not defined")

class EnvLoader:
    @staticmethod
    def _convert_to_bool(value: str) -> bool:
        """Convert string value to boolean"""
        value = value.lower()
        if value in ('true', '1'):
            return True
        if value in ('false', '0'):
            return False
        raise ValueError(f"Cannot convert '{value}' to bool")

    @classmethod
    def load(cls, env_file: Union[str, Path, None] = None, **env_vars: EnvVarsDict) -> T:
        """Load and validate environment variables from .env file"""
        values = {}
        missing_vars = []
        env_class = create_env_class(**env_vars)
        
        # First check environment variables
        for var_name, var_type in env_vars.items():
            required = True
            default = None
            
            # Handle optional variables with default values
            if isinstance(var_type, tuple):
                var_type, default = var_type
                required = False
            
            value = os.getenv(var_name.upper())
            
            if value is None:
                # If not found in environment, try loading from .env file
                if env_file and load_dotenv(dotenv_path=env_file, override=False):
                    value = os.getenv(var_name.upper())
                
                if value is None:
                    if required:
                        missing_vars.append(var_name.upper())
                        continue
                    value = default
                    # Skip type conversion for default values as they already have correct type
                    values[var_name] = value
                    continue
            
            # Convert string values from env to proper type
            try:
                if var_type == bool:
                    value = cls._convert_to_bool(value)
                else:
                    value = var_type(value)
            except ValueError:
                raise EnvTypeError(f"Environment variable {var_name.upper()} must be of type {var_type.__name__}")
            
            values[var_name] = value

        if missing_vars:
            raise EnvMissingError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        return cast(T, env_class(**values))
