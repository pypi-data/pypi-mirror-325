import pytest
import os
from typing import Dict, Any
from pathlib import Path
from tests.utils.mocks import patch_providers

@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    # Use test-specific environment variables
    test_env = {
        "ANTHROPIC_API_KEY": "test-claude-key",
        "GOOGLE_API_KEY": "test-gemini-key",
        "TEST_MODE": "true"
    }
    
    # Apply environment variables
    for key, value in test_env.items():
        monkeypatch.setenv(key, value)
    
    return test_env

@pytest.fixture
def test_storage_path(tmp_path) -> Path:
    """Create and return a temporary storage path."""
    storage = tmp_path / "test_storage"
    storage.mkdir(exist_ok=True)
    return storage

@pytest.fixture
def mock_responses():
    """Mock API responses for testing."""
    # Implementation will depend on the mocking library used
    pass

@pytest.fixture
def test_instructions() -> str:
    """Return test instructions for agents."""
    return """
    # Test Agent Instructions
    You are a test agent. Your role is to:
    1. Process test messages
    2. Return predefined responses
    3. Validate functionality
    """

@pytest.fixture
def test_config() -> Dict[str, Any]:
    """Return test configuration."""
    return {
        "name": "Test Agent",
        "description": "Agent for testing",
        "llm_provider": "claude",
        "provider_config": {
            "model": "claude-3-5-sonnet-latest",
            "max_tokens": 100
        },
        "temperature": 0.7
    }

def pytest_configure(config):
    """Configure pytest for the test suite."""
    # Add custom markers
    config.addinivalue_line(
        "markers",
        "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers",
        "api: mark test as requiring API access"
    )

def pytest_collection_modifyitems(config, items):
    """Modify test collection based on environment."""
    skip_integration = pytest.mark.skip(reason="Integration tests disabled")
    skip_api = pytest.mark.skip(reason="API tests disabled")
    
    # Skip integration tests unless explicitly enabled
    run_integration = config.getoption("--integration", default=False)
    # Skip API tests unless explicitly enabled
    run_api = config.getoption("--api", default=False)
    
    for item in items:
        # Skip integration tests
        if "integration" in item.keywords and not run_integration:
            item.add_marker(skip_integration)
        # Skip API tests
        if "api" in item.keywords and not run_api:
            item.add_marker(skip_api)

def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="run integration tests"
    )
    parser.addoption(
        "--api",
        action="store_true",
        default=False,
        help="run API tests"
    )

@pytest.fixture
def mock_provider_config() -> Dict[str, Dict[str, Any]]:
    """Provide mock provider configurations for testing."""
    return {
        "claude": {
            "model": "claude-3-sonnet",
            "api_version": "2024-03",
            "max_tokens": 4096
        },
        "gemini": {
            "model": "gemini-2.0-pro",
            "api_version": "2024-01",
            "max_tokens": 4096
        }
    }

@pytest.fixture
def mock_agent_config() -> Dict[str, Any]:
    """Mock agent configuration for testing."""
    return {
        "name": "TestAgent",
        "description": "Test Agent Description",
        "instructions": "Test instructions",
        "tools_folder": "./tools",
        "temperature": 0.7
    }

@pytest.fixture
def mock_agency_config() -> Dict[str, Any]:
    """Mock agency configuration for testing."""
    return {
        "shared_instructions": "Test shared instructions",
        "temperature": 0.7,
        "max_prompt_tokens": 4096
    }

@pytest.fixture
def mock_tool_config() -> Dict[str, Any]:
    """Mock tool configuration for testing."""
    return {
        "name": "TestTool",
        "description": "Test Tool Description",
        "parameters": {
            "param1": "value1",
            "param2": "value2"
        }
    }

@pytest.fixture(autouse=True)
def mock_providers(monkeypatch, mock_env_vars):
    """Automatically mock LLM providers for all tests."""
    patch_providers(monkeypatch, mock_env_vars)
    return None 