import pytest
from multi_swarm import Agent
from multi_swarm.tools import BaseTool
from pathlib import Path
from unittest.mock import patch, MagicMock
import os

class MockTool(BaseTool):
    """Mock tool for testing."""
    def run(self):
        return "Mock tool result"

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
    """Fixture to create a temporary tools directory with mock tools."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    
    # Create a mock tool file
    tool_file = tools_dir / "mock_tool.py"
    tool_file.write_text("""
from multi_swarm.tools import BaseTool

class MockTool(BaseTool):
    def run(self):
        return "Mock tool result"
    """)
    
    return str(tools_dir)

def test_tool_loading(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test loading tools from directory."""
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    
    # Verify tools were loaded
    assert len(agent.tools) > 0
    assert "MockTool" in agent.tools
    assert isinstance(agent.tools["MockTool"], BaseTool)

def test_tool_loading_empty_dir(mock_env_vars, mock_instructions, tmp_path):
    """Test loading tools from empty directory."""
    empty_dir = tmp_path / "empty_tools"
    empty_dir.mkdir()
    
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=str(empty_dir)
    )
    
    assert agent.tools == {}

def test_tool_loading_nonexistent_dir(mock_env_vars, mock_instructions):
    """Test loading tools from nonexistent directory."""
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder="nonexistent_tools"
    )
    
    assert agent.tools == {}

def test_tool_loading_invalid_tool(mock_env_vars, mock_instructions, tmp_path):
    """Test loading invalid tool files."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    
    # Create an invalid tool file
    invalid_tool = tools_dir / "invalid_tool.py"
    invalid_tool.write_text("""
class InvalidTool:  # Not inheriting from BaseTool
    def run(self):
        return "Invalid tool"
    """)
    
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=str(tools_dir)
    )
    
    assert "InvalidTool" not in agent.tools

def test_tool_loading_syntax_error(mock_env_vars, mock_instructions, tmp_path):
    """Test handling of syntax errors in tool files."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    
    # Create a file with syntax error
    invalid_tool = tools_dir / "syntax_error.py"
    invalid_tool.write_text("""
this is not valid python code
    """)
    
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=str(tools_dir)
    )
    
    assert agent.tools == {}

def test_tool_access_methods(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test tool access methods."""
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=mock_tools_dir
    )
    
    # Test get_tool
    tool = agent.get_tool("MockTool")
    assert tool is not None
    assert isinstance(tool, BaseTool)
    
    # Test list_tools
    tools = agent.list_tools()
    assert "MockTool" in tools
    
    # Test getting nonexistent tool
    assert agent.get_tool("NonexistentTool") is None

def test_tool_reloading(mock_env_vars, mock_instructions, tmp_path):
    """Test reloading tools after changes."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=str(tools_dir)
    )
    
    # Initially no tools
    assert len(agent.tools) == 0
    
    # Add a new tool file
    tool_file = tools_dir / "new_tool.py"
    tool_file.write_text("""
from multi_swarm.tools import BaseTool

class NewTool(BaseTool):
    def run(self):
        return "New tool result"
    """)
    
    # Reload tools
    agent.tools = agent._load_tools()
    
    # Verify new tool was loaded
    assert "NewTool" in agent.tools

def test_multiple_tools_same_file(mock_env_vars, mock_instructions, tmp_path):
    """Test loading multiple tools from the same file."""
    tools_dir = tmp_path / "tools"
    tools_dir.mkdir()
    
    # Create a file with multiple tools
    tool_file = tools_dir / "multiple_tools.py"
    tool_file.write_text("""
from multi_swarm.tools import BaseTool

class Tool1(BaseTool):
    def run(self):
        return "Tool 1 result"

class Tool2(BaseTool):
    def run(self):
        return "Tool 2 result"
    """)
    
    agent = Agent(
        name="TestAgent",
        description="Test agent",
        instructions=mock_instructions,
        tools_folder=str(tools_dir)
    )
    
    assert "Tool1" in agent.tools
    assert "Tool2" in agent.tools 