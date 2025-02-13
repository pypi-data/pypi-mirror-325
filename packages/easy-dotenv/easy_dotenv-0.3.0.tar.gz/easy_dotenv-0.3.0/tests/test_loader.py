import os
import pytest
from easy_dotenv import EnvLoader, EnvMissingError, EnvTypeError

@pytest.fixture
def clean_env():
    """Clean environment variables before each test"""
    # Save original environment
    original_env = dict(os.environ)
    
    # Clean environment variables
    for key in list(os.environ.keys()):
        if key not in ('PATH', 'PYTHONPATH'):  # Keep essential variables
            del os.environ[key]
    
    yield
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)

def test_required_vars(clean_env):
    """Test loading required environment variables"""
    os.environ['DATABASE_URL'] = 'postgresql://localhost:5432/db'
    os.environ['PORT'] = '5000'

    env = EnvLoader.load(
        database_url=str,
        port=int
    )

    assert env.database_url == 'postgresql://localhost:5432/db'
    assert env.port == 5000

def test_optional_vars(clean_env):
    """Test loading optional environment variables with defaults"""
    env = EnvLoader.load(
        debug=(bool, False),
        workers=(int, 4)
    )

    assert env.debug is False
    assert env.workers == 4

def test_missing_required_var(clean_env):
    """Test error when required variable is missing"""
    with pytest.raises(EnvMissingError) as exc_info:
        EnvLoader.load(
            missing_var=str
        )
    assert "MISSING_VAR" in str(exc_info.value)

def test_invalid_type(clean_env):
    """Test error when variable has invalid type"""
    os.environ['PORT'] = 'not_a_number'

    with pytest.raises(EnvTypeError) as exc_info:
        EnvLoader.load(
            port=int
        )
    assert "PORT" in str(exc_info.value)
    assert "int" in str(exc_info.value)

def test_bool_conversion(clean_env):
    """Test boolean value conversion"""
    os.environ['DEBUG'] = 'true'
    os.environ['VERBOSE'] = '1'
    os.environ['QUIET'] = 'false'
    os.environ['TESTING'] = '0'

    env = EnvLoader.load(
        debug=bool,
        verbose=bool,
        quiet=bool,
        testing=bool
    )

    assert env.debug is True
    assert env.verbose is True
    assert env.quiet is False
    assert env.testing is False

def test_mixed_vars(clean_env):
    """Test mix of required and optional variables"""
    os.environ['API_KEY'] = 'secret'
    os.environ['DEBUG'] = 'true'

    env = EnvLoader.load(
        api_key=str,
        port=(int, 8000),
        debug=(bool, False)
    )

    assert env.api_key == 'secret'
    assert env.port == 8000  # Default value
    assert env.debug is True  # From environment
