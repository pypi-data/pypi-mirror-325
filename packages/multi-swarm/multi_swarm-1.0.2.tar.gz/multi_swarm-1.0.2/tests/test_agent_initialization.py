import pytest
import os
from pathlib import Path
from multi_swarm import Agent, BaseAgent
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_env_vars():
    """Fixture to set up mock environment variables."""
    with patch.dict(os.environ, {
        'ANTHROPIC_API_KEY': 'mock-anthropic-key',
        'GOOGLE_API_KEY': 'mock-google-key'
    }):
        yield

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

def test_base_agent_initialization(mock_env_vars, mock_instructions):
    """Test BaseAgent initialization with minimal parameters."""
    agent = BaseAgent(
        name="TestBaseAgent",
        description="Test description",
        instructions=mock_instructions,
        llm_provider="claude",
        provider_config={"model": "test-model"},
        temperature=0.7
    )
    
    assert agent.config.name == "TestBaseAgent"
    assert agent.config.description == "Test description"
    assert agent.config.llm_provider == "claude"
    assert agent.config.temperature == 0.7
    assert agent.instructions == "Test agent instructions"

def test_agent_initialization_with_defaults(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test Agent initialization with default values."""
    agent = Agent(
        name="TestAgent",
        description="Test agent for code tasks",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    
    assert agent.config.name == "TestAgent"
    assert agent.config.description == "Test agent for code tasks"
    assert agent.config.llm_provider == "claude"  # Default for code tasks
    assert agent.tools_folder == mock_tools_dir
    assert agent.storage_path == "./storage"
    assert not agent.use_file_storage
    assert not agent.use_rag
    assert not agent.use_code_interpreter

def test_agent_initialization_with_custom_config(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test Agent initialization with custom configuration."""
    custom_config = {
        "model": "custom-model",
        "max_tokens": 2048,
        "api_version": "2024-custom"
    }
    
    agent = Agent(
        name="CustomAgent",
        description="Custom agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="gemini",
        provider_config=custom_config,
        temperature=0.9,
        storage_path="/custom/storage",
        use_file_storage=True,
        use_rag=True,
        use_code_interpreter=True
    )
    
    assert agent.config.llm_provider == "gemini"
    assert agent.config.provider_config == custom_config
    assert agent.config.temperature == 0.9
    assert agent.storage_path == "/custom/storage"
    assert agent.use_file_storage
    assert agent.use_rag
    assert agent.use_code_interpreter

def test_agent_initialization_missing_instructions():
    """Test Agent initialization with missing instructions file."""
    with pytest.raises(FileNotFoundError):
        Agent(
            name="TestAgent",
            description="Test agent",
            instructions="nonexistent.md",
            tools_folder="tools"
        )

def test_agent_initialization_invalid_provider(mock_instructions, mock_tools_dir):
    """Test Agent initialization with invalid provider."""
    with pytest.raises(ValueError, match="Unsupported LLM provider"):
        Agent(
            name="TestAgent",
            description="Test agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir,
            llm_provider="invalid_provider"
        )

def test_agent_initialization_missing_api_keys(mock_instructions, mock_tools_dir):
    """Test Agent initialization with missing API keys."""
    # Test Claude without API key
    with pytest.raises(ValueError, match="ANTHROPIC_API_KEY.*required"):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': '', 'GOOGLE_API_KEY': 'mock-key'}):
            Agent(
                name="TestAgent",
                description="Test agent",
                instructions=mock_instructions,
                tools_folder=mock_tools_dir,
                llm_provider="claude"
            )
    
    # Test Gemini without API key
    with pytest.raises(ValueError, match="GOOGLE_API_KEY.*required"):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'mock-key', 'GOOGLE_API_KEY': ''}):
            Agent(
                name="TestAgent",
                description="Test agent",
                instructions=mock_instructions,
                tools_folder=mock_tools_dir,
                llm_provider="gemini"
            )

def test_agent_initialization_with_nonexistent_tools_dir(mock_instructions):
    """Test Agent initialization with nonexistent tools directory."""
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder="nonexistent_tools"
    )
    
    assert agent.tools == {} 