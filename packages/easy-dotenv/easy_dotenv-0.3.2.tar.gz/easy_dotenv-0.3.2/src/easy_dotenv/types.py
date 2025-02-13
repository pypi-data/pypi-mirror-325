from typing import Protocol, TypeVar, Any, Dict, Type, Union, Optional, get_type_hints
from pathlib import Path
import inspect
import os
from .exceptions import EnvFileNotFoundError

class RuntimeEnvironment(Protocol):
    """Runtime environment protocol for type checking"""
    def __getattr__(self, name: str) -> Any: ...

EnvVarType = Union[Type, tuple[Type, Optional[Any]]]
EnvVarsDict = Dict[str, EnvVarType]

T = TypeVar('T')

class EnvConfig:
    """Base class for environment configuration"""
    def __init_subclass__(cls) -> None:
        from .loader import EnvLoader
        
        hints = get_type_hints(cls)
        env_vars = {}
        
        # Get type hints and default values
        for name, type_hint in hints.items():
            if name.startswith('_'):
                continue
            
            # Check if there's a default value
            default = getattr(cls, name, None)
            if default is not None:
                env_vars[name] = (type_hint, default)
            else:
                env_vars[name] = type_hint
        
        def __new__(cls_, env_file: Union[str, Path, None] = None):
            if env_file:
                frame = inspect.currentframe()
                while frame:
                    if frame.f_code.co_name == '<module>':
                        caller_path = Path(frame.f_code.co_filename)
                        break
                    frame = frame.f_back

                if str(env_file).startswith('..'):  # Search from project root
                    # Find project root
                    current_dir = caller_path.parent
                    root_found = False
                    while current_dir.parent != current_dir:
                        if any((current_dir / marker).exists() for marker in ['pyproject.toml', 'setup.py', '.git']):
                            env_path = current_dir / '.env'
                            root_found = True
                            break
                        current_dir = current_dir.parent
                    if not root_found:
                        raise EnvFileNotFoundError("Could not find project root (no pyproject.toml, setup.py or .git found)")
                else:
                    # Relative to current file
                    env_path = caller_path.parent / str(env_file)
                
                if not env_path.exists():
                    raise EnvFileNotFoundError(f"Could not find .env file at {env_path}")
                
                instance = EnvLoader.load(env_file=env_path, **env_vars)
            else:
                instance = EnvLoader.load(**env_vars)
            return instance
            
        cls.__new__ = __new__ 