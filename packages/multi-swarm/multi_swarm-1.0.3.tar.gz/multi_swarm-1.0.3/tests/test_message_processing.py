import pytest
from multi_swarm import Agent
from multi_swarm.core.thread import Thread
from unittest.mock import patch, MagicMock
import anthropic
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

@pytest.fixture
def mock_claude_response():
    """Fixture to create a mock Claude response."""
    response = MagicMock()
    response.content = [MagicMock(text="Mock Claude response")]
    return response

@pytest.fixture
def mock_gemini_response():
    """Fixture to create a mock Gemini response."""
    response = MagicMock()
    response.choices = [MagicMock(message=MagicMock(content="Mock Gemini response"))]
    return response

def test_claude_message_processing(mock_env_vars, mock_instructions, mock_tools_dir, mock_claude_response):
    """Test message processing with Claude provider."""
    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_claude_response
        mock_anthropic.return_value = mock_client
        
        agent = Agent(
            name="ClaudeAgent",
            description="Code review agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir,
            llm_provider="claude"
        )
        
        # Create a thread
        thread = Thread(id="test-thread")
        thread.add_message(role="user", content="Test message")
        
        # Process the message
        response = agent._process_with_llm(thread)
        
        # Verify the response
        assert response == "Mock Claude response"
        
        # Verify the API call
        mock_client.messages.create.assert_called_once()
        call_args = mock_client.messages.create.call_args[1]
        assert call_args["model"] == "claude-3-5-sonnet-latest"
        assert call_args["max_tokens"] == 4096
        assert call_args["system"] == "Test agent instructions"
        assert len(call_args["messages"]) == 1
        assert call_args["messages"][0]["role"] == "user"
        assert call_args["messages"][0]["content"] == "Test message"

def test_gemini_message_processing(mock_env_vars, mock_instructions, mock_tools_dir, mock_gemini_response):
    """Test message processing with Gemini provider."""
    with patch('openai.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_gemini_response
        mock_openai.return_value = mock_client
        
        agent = Agent(
            name="GeminiAgent",
            description="Data processing agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir,
            llm_provider="gemini"
        )
        
        # Create a thread
        thread = Thread(id="test-thread")
        thread.add_message(role="user", content="Test message")
        
        # Process the message
        response = agent._process_with_llm(thread)
        
        # Verify the response
        assert response == "Mock Gemini response"
        
        # Verify the API call
        mock_client.chat.completions.create.assert_called_once()
        call_args = mock_client.chat.completions.create.call_args[1]
        assert call_args["model"] == "gemini-pro"
        assert len(call_args["messages"]) == 2
        assert call_args["messages"][0]["role"] == "system"
        assert call_args["messages"][0]["content"] == "Test agent instructions"
        assert call_args["messages"][1]["role"] == "user"
        assert call_args["messages"][1]["content"] == "Test message"

def test_message_processing_with_history(mock_env_vars, mock_instructions, mock_tools_dir, mock_claude_response):
    """Test message processing with conversation history."""
    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_claude_response
        mock_anthropic.return_value = mock_client
        
        agent = Agent(
            name="TestAgent",
            description="Test agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir
        )
        
        # Create a thread with history
        thread = Thread(id="test-thread")
        thread.add_message(role="user", content="First message")
        thread.add_message(role="assistant", content="First response")
        thread.add_message(role="user", content="Second message")
        
        # Process the message
        response = agent._process_with_llm(thread)
        
        # Verify the API call includes history
        call_args = mock_client.messages.create.call_args[1]
        messages = call_args["messages"]
        assert len(messages) == 3
        assert messages[0]["role"] == "user"
        assert messages[0]["content"] == "First message"
        assert messages[1]["role"] == "assistant"
        assert messages[1]["content"] == "First response"
        assert messages[2]["role"] == "user"
        assert messages[2]["content"] == "Second message"

def test_message_processing_errors(mock_env_vars, mock_instructions, mock_tools_dir):
    """Test error handling in message processing."""
    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("API Error")
        mock_anthropic.return_value = mock_client
        
        agent = Agent(
            name="TestAgent",
            description="Test agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir
        )
        
        # Create a thread
        thread = Thread(id="test-thread")
        thread.add_message(role="user", content="Test message")
        
        # Process the message and expect error handling
        with pytest.raises(ValueError, match="Error processing message"):
            agent._process_with_llm(thread)

def test_message_routing(mock_env_vars, mock_instructions, mock_tools_dir, mock_claude_response):
    """Test message routing between providers."""
    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_claude_response
        mock_anthropic.return_value = mock_client
        
        agent = Agent(
            name="TestAgent",
            description="Test agent",
            instructions=mock_instructions,
            tools_folder=mock_tools_dir
        )
        
        # Create a thread with a message containing routing
        thread = Thread(id="test-thread")
        thread.add_message(role="user", content="Analysis task @Gemini optimize this")
        
        # Process the message
        response = agent._process_with_llm(thread)
        
        # Verify the response includes routing information
        assert "Forwarding to Gemini" in response 