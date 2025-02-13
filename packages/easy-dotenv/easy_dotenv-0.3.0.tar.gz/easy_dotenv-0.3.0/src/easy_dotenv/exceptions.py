class EnvError(Exception):
    """Base exception for easy-dotenv errors"""
    pass

class EnvMissingError(EnvError):
    """Raised when required environment variables are missing"""
    pass

class EnvTypeError(EnvError):
    """Raised when environment variable has invalid type"""
    pass

class EnvFileNotFoundError(EnvError):
    """Raised when .env file cannot be found at specified path or project root"""
    pass 