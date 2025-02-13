from typing import Protocol, TypeVar, Any, Dict, Type, Union, Optional, get_type_hints
from dataclasses import dataclass

class RuntimeEnvironment(Protocol):
    """Runtime environment protocol for type checking"""
    def __getattr__(self, name: str) -> Any: ...

EnvVarType = Union[Type, tuple[Type, Optional[Any]]]
EnvVarsDict = Dict[str, EnvVarType]

T = TypeVar('T')

class EnvConfig:
    """Base class for environment configuration"""
    def __init_subclass__(cls) -> None:
        hints = get_type_hints(cls)
        env_vars = {
            name: type_hint for name, type_hint in hints.items()
            if not name.startswith('_')
        }
        
        # Create instance with loaded values
        instance = EnvLoader.load(**env_vars)
        
        # Replace class with instance
        cls.__new__ = lambda _: instance 