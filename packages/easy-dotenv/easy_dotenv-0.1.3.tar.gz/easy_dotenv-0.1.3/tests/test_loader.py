import os
import pytest
from easy_dotenv import EnvLoader, EnvMissingError, EnvTypeError

@pytest.fixture
def clean_env():
    """Cleans environment variables before each test"""
    original_env = dict(os.environ)
    os.environ.clear()
    yield
    os.environ.clear()
    os.environ.update(original_env)

def test_required_vars(clean_env):
    os.environ['DATABASE_URL'] = 'postgresql://localhost:5432/db'
    os.environ['PORT'] = '5000'
    
    env = EnvLoader.load(
        database_url=str,
        port=int
    )
    
    assert env.database_url == 'postgresql://localhost:5432/db'
    assert env.port == 5000
    assert isinstance(env.port, int)

def test_optional_vars(clean_env):
    env = EnvLoader.load(
        debug=(bool, False),
        workers=(int, 4)
    )
    
    assert env.debug is False
    assert env.workers == 4

def test_missing_required_var(clean_env):
    with pytest.raises(EnvMissingError) as exc_info:
        EnvLoader.load(api_key=str)
    
    assert 'API_KEY' in str(exc_info.value)

def test_invalid_type(clean_env):
    os.environ['PORT'] = 'not_a_number'
    
    with pytest.raises(EnvTypeError) as exc_info:
        EnvLoader.load(port=int)
    
    assert 'PORT' in str(exc_info.value)
    assert 'int' in str(exc_info.value)

def test_bool_conversion(clean_env):
    test_cases = {
        'true': True,
        'True': True,
        '1': True,
        'false': False,
        'False': False,
        '0': False
    }
    
    for input_value, expected in test_cases.items():
        os.environ['DEBUG'] = input_value
        env = EnvLoader.load(debug=bool)
        assert env.debug == expected

def test_mixed_vars(clean_env):
    os.environ['API_KEY'] = 'secret'
    os.environ['DEBUG'] = 'true'
    
    env = EnvLoader.load(
        api_key=str,
        port=(int, 8000),
        debug=(bool, False)
    )
    
    assert env.api_key == 'secret'
    assert env.port == 8000
    assert env.debug is True
