import pytest
from typing import Dict, Any
from unittest.mock import patch
import os

@pytest.fixture
def mock_env_vars():
    """Fixture to set up mock environment variables."""
    env_vars = {
        'ANTHROPIC_API_KEY': 'mock-anthropic-key',
        'GOOGLE_API_KEY': 'mock-google-key'
    }
    with patch.dict('os.environ', env_vars):
        yield env_vars

@pytest.fixture
def mock_instructions(tmp_path):
    """Fixture to create a temporary instructions file."""
    instructions = tmp_path / "instructions.md"
    instructions.write_text("Test agent instructions")
    return str(instructions)

@pytest.fixture
def mock_tools_dir(tmp_path):
    """Fixture to create a temporary tools directory."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    return str(tools_dir)

@pytest.fixture(autouse=True)
def mock_providers(monkeypatch, mock_env_vars):
    """Automatically mock LLM providers for all tests."""
    # Mock Anthropic client
    class MockAnthropicClient:
        def messages(self):
            return self
        
        def create(self, *args, **kwargs):
            return type('Response', (), {
                'content': [type('Content', (), {'text': 'Mock Claude response'})()]
            })
    
    # Mock Gemini client
    class MockGeminiClient:
        def chat(self):
            return self
            
        def completions(self):
            return self
            
        def create(self, *args, **kwargs):
            return type('Response', (), {
                'choices': [type('Choice', (), {'message': {'content': 'Mock Gemini response'}})()]
            })
    
    # Patch the clients
    monkeypatch.setattr('anthropic.Anthropic', lambda *args, **kwargs: MockAnthropicClient())
    monkeypatch.setattr('google.generativeai.GenerativeModel', lambda *args, **kwargs: MockGeminiClient())

