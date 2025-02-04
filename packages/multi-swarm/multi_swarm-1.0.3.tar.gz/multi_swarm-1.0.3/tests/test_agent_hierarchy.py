import pytest
from multi_swarm import Agent, BaseAgent
from multi_swarm.core.agent import Agent as CoreAgent
from multi_swarm.core.base_agent import BaseAgent as CoreBaseAgent

def test_agent_imports():
    """Test that agent classes can be imported from both root and core packages."""
    # Test imports from root package
    assert Agent is not None
    assert BaseAgent is not None
    
    # Test imports from core package
    assert CoreAgent is not None
    assert CoreBaseAgent is not None
    
    # Verify they are the same classes
    assert Agent is CoreAgent
    assert BaseAgent is CoreBaseAgent

def test_agent_inheritance():
    """Test that Agent properly inherits from BaseAgent."""
    assert issubclass(Agent, BaseAgent)
    
    # Test that Agent implements all abstract methods
    required_methods = [
        '_determine_provider',
        '_get_provider_config',
        '_load_tools',
        '_validate_environment',
        '_process_with_llm'
    ]
    
    for method in required_methods:
        assert hasattr(Agent, method), f"Agent missing required method: {method}"
        assert Agent.__dict__[method] != BaseAgent.__dict__[method], \
            f"Agent.{method} not implemented (still using BaseAgent's implementation)"

def test_agent_initialization():
    """Test that Agent can be properly initialized with various configurations."""
    # Test with minimal required parameters
    agent = Agent(
        name="TestAgent",
        description="A test agent",
        instructions="test_instructions.txt",
        tools_folder="test_tools"
    )
    assert agent.name == "TestAgent"
    assert agent.description == "A test agent"
    
    # Test with custom provider
    agent_claude = Agent(
        name="ClaudeAgent",
        description="A Claude agent for code tasks",
        instructions="test_instructions.txt",
        tools_folder="test_tools",
        llm_provider="claude"
    )
    assert agent_claude.config.llm_provider == "claude"
    
    # Test with custom config
    custom_config = {"model": "custom-model", "max_tokens": 2048}
    agent_custom = Agent(
        name="CustomAgent",
        description="A custom agent",
        instructions="test_instructions.txt",
        tools_folder="test_tools",
        provider_config=custom_config
    )
    assert agent_custom.config.provider_config["model"] == "custom-model"
    
def test_automatic_provider_selection():
    """Test that Agent correctly selects providers based on description."""
    # Test Claude selection for code tasks
    code_agent = Agent(
        name="CodeAgent",
        description="An agent for code review and documentation",
        instructions="test_instructions.txt",
        tools_folder="test_tools"
    )
    assert code_agent.config.llm_provider == "claude"
    
    # Test Gemini selection for data tasks
    data_agent = Agent(
        name="DataAgent",
        description="An agent for data processing and analysis",
        instructions="test_instructions.txt",
        tools_folder="test_tools"
    )
    assert data_agent.config.llm_provider == "gemini"
    
def test_circular_imports():
    """Test that there are no circular import issues."""
    from multi_swarm.core import Agency, Agent, BaseAgent
    from multi_swarm import Agency as RootAgency, Agent as RootAgent, BaseAgent as RootBaseAgent
    
    # Verify imports work from both locations
    assert Agency is RootAgency
    assert Agent is RootAgent
    assert BaseAgent is RootBaseAgent 