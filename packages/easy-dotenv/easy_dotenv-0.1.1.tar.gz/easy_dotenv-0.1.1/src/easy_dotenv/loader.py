import os
from typing import Dict, Type, Union, Optional
from dotenv import load_dotenv

class EnvError(Exception):
    """Base exception for easy-dotenv errors"""
    pass

class EnvMissingError(EnvError):
    """Raised when required environment variables are missing"""
    pass

class EnvTypeError(EnvError):
    """Raised when environment variable has invalid type"""
    pass

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
    def load(cls, **env_vars: Dict[str, Union[Type, tuple[Type, Optional[any]]]]):
        load_dotenv()
        
        instance = type('Environment', (), {})()
        missing_vars = []
        
        for var_name, var_type in env_vars.items():
            required = True
            default = None
            
            if isinstance(var_type, tuple):
                var_type, default = var_type
                required = False
            
            value = os.getenv(var_name.upper())
            
            if value is None:
                if required:
                    missing_vars.append(var_name.upper())
                    continue
                value = default
            else:
                try:
                    if var_type == bool:
                        value = cls._convert_to_bool(value)
                    else:
                        value = var_type(value)
                except ValueError:
                    raise EnvTypeError(f"Environment variable {var_name.upper()} must be of type {var_type.__name__}")
            
            setattr(instance, var_name, value)

        if missing_vars:
            raise EnvMissingError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        return instance
