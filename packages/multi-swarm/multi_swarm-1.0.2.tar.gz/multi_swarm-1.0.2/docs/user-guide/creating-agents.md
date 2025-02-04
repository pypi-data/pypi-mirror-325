# Creating Agents

Agents are the core building blocks of Multi-Swarm. Each agent has specific roles, capabilities, and tools.

## Important Naming Requirements

1. **Entry Agent Name**
   - Must match the agency name
   - Used for initial message routing
   - Case-sensitive
   - Example: If agency.name is "CEO", the entry agent's name must be "CEO"

2. **Other Agent Names**
   - Must be unique within the agency
   - Should reflect the agent's role
   - Case-sensitive
   - Used in communication flows

## Basic Agent Creation

```python
from multi_swarm import Agent

class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",  # Will be the entry agent
            description="Chief Executive Officer - Main decision maker",
            instructions="path/to/ceo_instructions.md",
            tools_folder="path/to/ceo_tools",
            temperature=0.7
        )

class Developer(Agent):
    def __init__(self):
        super().__init__(
            name="Developer",
            description="Expert in software development and implementation",
            instructions="path/to/dev_instructions.md",
            tools_folder="path/to/dev_tools",
            use_code_interpreter=True  # Enable code execution
        )
```

## Agent Parameters

- **name** (str): Unique identifier for the agent (MUST match agency name if entry agent)
- **description** (str): Detailed description of agent's role and capabilities
- **instructions** (str): Path to markdown file containing agent instructions
- **tools_folder** (str): Path to folder containing agent's tools
- **temperature** (float, optional): Model temperature (0.0-1.0)
- **use_rag** (bool, optional): Enable Retrieval-Augmented Generation
- **llm_provider** (str, optional): Manually specify LLM provider ("claude" or "gemini")
- **provider_config** (dict, optional): Provider-specific configuration

## Message Handling

Agents must handle messages correctly:

```python
# Correct way to add a message
thread.add_message(
    content="Task assigned: Implement feature X",
    role="assistant",
    agent_name=self.config.name,  # Required
    metadata={"task_id": "123"}   # Optional
)

# Wrong ways:
# ❌ Don't pass dict directly
thread.add_message({
    "content": "Message",
    "role": "user"
})

# ❌ Don't create Message instance directly
message = Message(
    content="Message",
    role="user"
)
```

## Agent Instructions

Create an `instructions.md` file to define the agent's behavior:

```markdown
# Agent Role

[Detailed description of the agent's role and responsibilities]

# Goals

- Primary Goal: [Description]
- Secondary Goals:
  - Goal 1: [Description]
  - Goal 2: [Description]

# Process Workflow

1. Message Reception
   - Validate incoming messages
   - Extract key information
   - Identify required actions

2. Task Processing
   - Select appropriate tools
   - Execute actions
   - Handle errors gracefully

3. Response Generation
   - Format response appropriately
   - Include necessary metadata
   - Ensure proper message structure

# Guidelines

- Always validate inputs
- Use appropriate error handling
- Maintain message format
- Follow security practices
```

## Advanced Features

### 1. Knowledge Base (RAG)

```python
class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Researcher",
            description="Research and analysis specialist",
            instructions="researcher_instructions.md",
            tools_folder="./tools",
            use_rag=True,
            rag_config={
                "index_name": "research_data",
                "embedding_model": "all-MiniLM-L6-v2",
                "chunk_size": 1000
            }
        )
```

### 2. Code Interpreter

```python
class DevAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Developer",
            description="Software development and testing",
            instructions="dev_instructions.md",
            tools_folder="./tools",
            use_code_interpreter=True,
            interpreter_config={
                "timeout": 30,
                "memory_limit": "1G",
                "allowed_imports": ["os", "sys", "json"]
            }
        )
```

### 3. File Storage

```python
class DataAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Data Manager",
            description="Data management and processing",
            instructions="data_instructions.md",
            tools_folder="./tools",
            use_file_storage=True,
            storage_config={
                "base_path": "./data",
                "max_size": "5G",
                "allowed_types": [".csv", ".json", ".txt"]
            }
        )
```

## Error Handling

Implement comprehensive error handling:

```python
from multi_swarm.exceptions import AgentError, ToolError

class CustomAgent(Agent):
    def _process_with_llm(self, thread: Thread) -> str:
        """Process message with proper error handling."""
        try:
            # Validate thread
            if not thread.messages:
                raise AgentError("Empty thread")
                
            # Process message
            response = super()._process_with_llm(thread)
            
            # Validate response
            if not response:
                raise AgentError("Empty response")
                
            return response
            
        except ToolError as e:
            # Handle tool execution errors
            self.logger.error(f"Tool error: {str(e)}")
            return {"error": f"Tool execution failed: {str(e)}"}
            
        except Exception as e:
            # Handle unexpected errors
            self.logger.error(f"Unexpected error: {str(e)}")
            raise AgentError(f"Processing failed: {str(e)}")
```

## Testing Agents

Create comprehensive tests:

```python
def test_agent():
    # Create test agent
    agent = TestAgent("TestAgent")
    
    # Test initialization
    assert agent.config.name == "TestAgent"
    assert agent.tools is not None
    
    # Test message processing
    thread = agent.thread_manager.create_thread()
    thread.add_message(
        content="Test message",
        role="user",
        agent_name="user"
    )
    
    response = agent._process_with_llm(thread)
    assert response is not None
    
    # Test error handling
    with pytest.raises(AgentError):
        agent._process_with_llm(Thread())  # Empty thread
```

## Best Practices

### 1. Agent Design
- Give agents focused responsibilities
- Use clear, descriptive names
- Implement proper error handling
- Enable only needed features

### 2. Message Handling
- Always use Thread.add_message
- Include required agent_name
- Validate message content
- Handle metadata properly

### 3. State Management
- Implement proper cleanup
- Handle resource limits
- Monitor performance
- Log important events

### 4. Security
- Validate inputs
- Control resource usage
- Handle sensitive data
- Monitor operations

## Common Issues and Solutions

### 1. Message Routing Issues
**Problem**: Messages not reaching correct agent
**Solution**: 
- Verify agent names match flow configuration
- Check thread creation
- Validate message format

### 2. Performance Issues
**Problem**: Slow message processing
**Solution**:
- Optimize tool usage
- Implement caching
- Monitor resource usage
- Use appropriate batch sizes

### 3. State Management Issues
**Problem**: Lost or corrupted state
**Solution**:
- Enable proper persistence
- Implement backups
- Monitor storage usage
- Handle cleanup properly

## Learn More

- [Creating Tools](creating-tools.md)
- [Agency Configuration](agency-configuration.md)
- [Testing Guide](testing.md) 