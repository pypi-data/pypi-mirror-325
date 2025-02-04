import pytest
from multi_swarm import Agent
from unittest.mock import patch
import os

@pytest.fixture
def mock_env_vars():
    """Fixture to set up mock environment variables."""
    with patch.dict('os.environ', {
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

def test_automatic_provider_selection(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test automatic provider selection based on agent description."""
    test_cases = [
        # Code Generation & Development (Claude)
        ("An agent for Python code generation and review", "claude"),
        ("Expert in debugging and refactoring code", "claude"),
        ("API design and documentation specialist", "claude"),
        
        # Research & Analysis (Claude)
        ("Research assistant for complex analysis", "claude"),
        ("Strategic planning and architecture expert", "claude"),
        ("Security analysis specialist", "claude"),
        
        # Writing & Documentation (Claude)
        ("Technical writing and documentation expert", "claude"),
        ("Content creation specialist", "claude"),
        
        # Data Processing & Analysis (Gemini)
        ("Data processing and transformation expert", "gemini"),
        ("Statistical analysis specialist", "gemini"),
        ("Data pipeline operations manager", "gemini"),
        
        # Real-time Operations (Gemini)
        ("System monitoring and alerting specialist", "gemini"),
        ("Metrics processing and logging expert", "gemini"),
        
        # System Operations (Gemini)
        ("Deployment and integration specialist", "gemini"),
        ("Process automation expert", "gemini"),
        ("Performance optimization specialist", "gemini"),
        
        # Machine Learning Operations (Gemini)
        ("ML training and inference specialist", "gemini"),
        ("Machine learning pipeline expert", "gemini"),
        ("Model monitoring specialist", "gemini"),
        
        # Default cases (Claude)
        ("Generic assistant", "claude"),
        ("Custom task handler", "claude")
    ]
    
    for description, expected_provider in test_cases:
        agent = Agent(
            name="TestAgent",
            description=description,
            instructions=mock_instructions,
            tools_folder=mock_tools_dir
        )
        assert agent.config.llm_provider == expected_provider, \
            f"Expected {expected_provider} for description: {description}"

def test_manual_provider_override(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test that manual provider selection overrides automatic selection."""
    # Description suggests Claude, but manually set to Gemini
    agent = Agent(
        name="TestAgent",
        description="Code review and documentation specialist",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="gemini"
    )
    assert agent.config.llm_provider == "gemini"
    
    # Description suggests Gemini, but manually set to Claude
    agent = Agent(
        name="TestAgent",
        description="Data processing and analysis expert",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="claude"
    )
    assert agent.config.llm_provider == "claude"

def test_provider_config_selection(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test that correct provider config is selected based on task type."""
    # Test code task config
    code_agent = Agent(
        name="CodeAgent",
        description="Python code generation specialist",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert code_agent.config.provider_config["temperature"] == 0.1
    assert code_agent.config.provider_config["model"] == "claude-3-5-sonnet-latest"
    
    # Test research task config
    research_agent = Agent(
        name="ResearchAgent",
        description="Research and analysis specialist",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert research_agent.config.provider_config["temperature"] == 0.7
    assert research_agent.config.provider_config["model"] == "claude-3-5-opus-latest"
    
    # Test data task config
    data_agent = Agent(
        name="DataAgent",
        description="Data processing expert",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert data_agent.config.provider_config["temperature"] == 0.3
    assert data_agent.config.provider_config["model"] == "gemini-2.0-flash-exp"
    
    # Test realtime task config
    realtime_agent = Agent(
        name="MonitoringAgent",
        description="System monitoring specialist",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert realtime_agent.config.provider_config["temperature"] == 0.5
    assert realtime_agent.config.provider_config["model"] == "gemini-2.0-flash-exp"
    assert realtime_agent.config.provider_config["max_tokens"] == 2048

def test_config_override(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test that user-provided config overrides task-specific config."""
    custom_config = {
        "model": "custom-model",
        "temperature": 0.9,
        "max_tokens": 1024
    }
    
    agent = Agent(
        name="TestAgent",
        description="Code generation specialist",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        provider_config=custom_config
    )
    
    assert agent.config.provider_config["model"] == "custom-model"
    assert agent.config.provider_config["temperature"] == 0.9
    assert agent.config.provider_config["max_tokens"] == 1024

def test_provider_config_defaults(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test default provider configurations."""
    # Test Claude defaults
    claude_agent = Agent(
        name="ClaudeAgent",
        description="Code review agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert claude_agent.config.provider_config["model"] == "claude-3-5-sonnet-latest"
    assert claude_agent.config.provider_config["max_tokens"] == 4096
    assert claude_agent.config.provider_config["api_version"] == "2024-03"
    
    # Test Gemini defaults
    gemini_agent = Agent(
        name="GeminiAgent",
        description="Data processing agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    assert gemini_agent.config.provider_config["model"] == "gemini-2.0-flash-exp"
    assert gemini_agent.config.provider_config["max_tokens"] == 4096
    assert gemini_agent.config.provider_config["api_version"] == "2024-01"

def test_provider_config_override(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test overriding default provider configurations."""
    custom_config = {
        "model": "custom-model",
        "max_tokens": 2048,
        "api_version": "custom-version",
        "extra_param": "custom-value"
    }
    
    # Test with Claude
    claude_agent = Agent(
        name="CustomClaudeAgent",
        description="Code agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        provider_config=custom_config
    )
    assert claude_agent.config.provider_config == custom_config
    
    # Test with Gemini
    gemini_agent = Agent(
        name="CustomGeminiAgent",
        description="Data agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="gemini",
        provider_config=custom_config
    )
    assert gemini_agent.config.provider_config == custom_config

def test_provider_config_partial_override(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test partial override of provider configurations."""
    partial_config = {
        "max_tokens": 2048,
        "extra_param": "custom-value"
    }
    
    # Test with Claude
    claude_agent = Agent(
        name="PartialClaudeAgent",
        description="Code agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        provider_config=partial_config
    )
    assert claude_agent.config.provider_config["model"] == "claude-3-5-sonnet-latest"
    assert claude_agent.config.provider_config["max_tokens"] == 2048
    assert claude_agent.config.provider_config["api_version"] == "2024-03"
    assert claude_agent.config.provider_config["extra_param"] == "custom-value"
    
    # Test with Gemini
    gemini_agent = Agent(
        name="PartialGeminiAgent",
        description="Data agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="gemini",
        provider_config=partial_config
    )
    assert gemini_agent.config.provider_config["model"] == "gemini-2.0-flash-exp"
    assert gemini_agent.config.provider_config["max_tokens"] == 2048
    assert gemini_agent.config.provider_config["api_version"] == "2024-01"
    assert gemini_agent.config.provider_config["extra_param"] == "custom-value"

def test_explicit_provider_override_description(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test that explicit provider selection overrides description-based selection."""
    # Description suggests Claude, but explicitly set to Gemini
    agent = Agent(
        name="TestAgent",
        description="Code review and documentation",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="gemini"
    )
    assert agent.config.llm_provider == "gemini"
    
    # Description suggests Gemini, but explicitly set to Claude
    agent = Agent(
        name="TestAgent",
        description="Data processing and analysis",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir,
        llm_provider="claude"
    )
    assert agent.config.llm_provider == "claude" 