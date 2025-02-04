# Testing Guide

This guide covers best practices for testing Multi-Swarm agencies, agents, and tools based on our testing experience.

## Core Testing Areas

### 1. Message Handling
- Test `agent_name` field inclusion
- Verify message routing
- Check thread management
- Test message persistence

### 2. State Management
- Test state persistence
- Verify state recovery
- Check concurrent access
- Test state cleanup

### 3. Agent Communication
- Test communication flows
- Verify message delivery
- Check response handling
- Test error scenarios

### 4. Tool Integration
- Test tool initialization
- Verify tool execution
- Check error handling
- Test resource cleanup

## Test Plan Structure

### 1. Unit Tests

```python
import pytest
from multi_swarm import Agent, Thread, Message

def test_message_handling():
    # Test message creation
    message = Message(
        content="Test message",
        role="user",
        agent_name="test_agent"
    )
    assert message.agent_name == "test_agent"
    
    # Test thread management
    thread = Thread()
    thread.add_message(message)
    assert len(thread.messages) == 1
    assert thread.messages[0].agent_name == "test_agent"

def test_state_persistence():
    # Test state saving
    agent = Agent("TestAgent")
    thread = agent.thread_manager.create_thread()
    thread.add_message(
        content="Test state",
        role="user",
        agent_name="user"
    )
    agent.save_state()
    
    # Test state loading
    new_agent = Agent("TestAgent")
    new_agent.load_state()
    loaded_thread = new_agent.thread_manager.get_thread(thread.id)
    assert loaded_thread.messages[0].content == "Test state"
```

### 2. Integration Tests

```python
def test_agent_communication():
    # Create agents
    agent1 = Agent("Agent1")
    agent2 = Agent("Agent2")
    
    # Test communication flow
    thread = agent1.thread_manager.create_thread()
    thread.add_message(
        content="Message for Agent2",
        role="user",
        agent_name="Agent1"
    )
    
    response = agent2._process_with_llm(thread)
    assert response is not None
    assert response.agent_name == "Agent2"

def test_tool_integration():
    # Create agent with tool
    agent = Agent("TestAgent")
    tool = TestTool()
    agent.add_tool(tool)
    
    # Test tool usage
    thread = agent.thread_manager.create_thread()
    thread.add_message(
        content="Use test tool",
        role="user",
        agent_name="user"
    )
    
    response = agent._process_with_llm(thread)
    assert "Tool executed successfully" in response.content
```

### 3. System Tests

```python
def test_agency_workflow():
    # Create agency
    agency = Agency([
        agent1,
        [agent1, agent2],
        [agent2, agent3]
    ])
    
    # Test complete workflow
    response = agency.process_message(
        "Start workflow",
        thread_id=None
    )
    
    assert response is not None
    assert len(agency.thread_manager.get_all_threads()) > 0
```

## Test Categories

### 1. Message Tests
- Message creation and validation
- Thread management
- Message routing
- State persistence

### 2. Agent Tests
- Agent initialization
- Tool management
- Communication flows
- Error handling

### 3. Agency Tests
- Agency configuration
- Inter-agent communication
- Workflow execution
- State management

### 4. Tool Tests
- Tool initialization
- Input validation
- Error handling
- Resource management

## Best Practices

### 1. Test Setup
- Use fixtures for common objects
- Clean up resources after tests
- Mock external services
- Use appropriate test data

### 2. Test Organization
- Group related tests
- Use descriptive names
- Document test purposes
- Maintain test independence

### 3. Error Testing
- Test error scenarios
- Verify error messages
- Check error recovery
- Test cleanup on errors

### 4. State Testing
- Test state persistence
- Verify state recovery
- Check concurrent access
- Test state cleanup

## Common Issues and Solutions

### 1. Message Handling
**Problem**: Missing agent_name in messages
**Solution**:
```python
def test_message_validation():
    # Test message creation with missing agent_name
    with pytest.raises(ValueError) as exc:
        Message(
            content="Test",
            role="user"
        )
    assert "agent_name is required" in str(exc.value)
    
    # Test correct message creation
    message = Message(
        content="Test",
        role="user",
        agent_name="test_agent"
    )
    assert message.agent_name == "test_agent"
```

### 2. State Management
**Problem**: State not persisting correctly
**Solution**:
```python
def test_state_persistence():
    agent = Agent("TestAgent")
    
    # Create and save state
    thread = agent.thread_manager.create_thread()
    thread.add_message(
        content="Test",
        role="user",
        agent_name="user"
    )
    agent.save_state()
    
    # Verify state persistence
    new_agent = Agent("TestAgent")
    new_agent.load_state()
    loaded_thread = new_agent.thread_manager.get_thread(thread.id)
    assert loaded_thread.messages[0].content == "Test"
```

### 3. Resource Management
**Problem**: Resources not cleaned up
**Solution**:
```python
def test_resource_cleanup():
    agent = Agent("TestAgent")
    tool = ResourceTool()
    
    try:
        # Use tool
        result = tool.run()
        assert result is not None
        
    finally:
        # Verify cleanup
        assert tool.resources_cleaned_up()
```

## Test Execution

### 1. Running Tests
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_messages.py

# Run tests with coverage
pytest --cov=multi_swarm tests/
```

### 2. Test Configuration
```python
# conftest.py
import pytest

@pytest.fixture
def test_agent():
    agent = Agent("TestAgent")
    yield agent
    agent.cleanup()

@pytest.fixture
def test_thread(test_agent):
    thread = test_agent.thread_manager.create_thread()
    yield thread
```

### 3. Test Environment
```bash
# .env.test
TEST_API_KEY=test_key
TEST_ENDPOINT=http://test-api.example.com
```

## Continuous Integration

### 1. GitHub Actions
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest tests/
```

### 2. Test Coverage
```yaml
      - name: Run coverage
        run: |
          pytest --cov=multi_swarm tests/
          coverage report
```

## Learn More

- [Creating Tools](creating-tools.md)
- [Creating Agents](creating-agents.md)
- [API Reference](../api/testing.md) 