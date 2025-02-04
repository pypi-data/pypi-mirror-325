# Agency Configuration Guide

This guide provides detailed information about configuring Multi-Swarm agencies, based on testing experience and best practices.

## Agency Configuration Best Practices

### Agent Naming
- The entry agent's name must match the agency's name for proper message routing
- Agent names must be unique within an agency
- Agent names are case-sensitive
- Use descriptive names that reflect the agent's role

### Communication Flows
- Flows are directional (source → target)
- Each flow creates its own thread
- The first flow's thread is used for initial message processing
- Reverse flows must be explicitly defined if bi-directional communication is needed

## Configuration Example

Here's a complete example of setting up an agency with proper configuration:

```python
from multi_swarm import Agency, Agent

# Create agents with proper naming
ceo = Agent(
    name="CEO",
    description="Chief Executive Officer - Main decision maker",
    instructions="path/to/ceo_instructions.md",
    tools_folder="path/to/ceo_tools"
)

developer = Agent(
    name="Developer",
    description="Software Developer - Implements solutions",
    instructions="path/to/dev_instructions.md",
    tools_folder="path/to/dev_tools"
)

assistant = Agent(
    name="Assistant",
    description="Virtual Assistant - Handles routine tasks",
    instructions="path/to/assistant_instructions.md",
    tools_folder="path/to/assistant_tools"
)

# Define communication flows
flows = [
    (ceo, developer),     # CEO can assign tasks to Developer
    (developer, ceo),     # Developer can report back to CEO
    (ceo, assistant),     # CEO can delegate to Assistant
    (assistant, ceo),     # Assistant can report to CEO
    (developer, assistant) # Developer can request assistance
]

# Create agency with matching name
agency = Agency(
    name="CEO",           # Matches the entry agent's name
    description="Software Development Agency",
    agents=[ceo, developer, assistant],
    flows=flows,
    storage_path="path/to/storage",
    shared_instructions="path/to/shared_instructions.md",
    use_code_interpreter=True,
    use_rag=True,
    use_file_storage=True
)
```

## Configuration Options

### Agency Configuration
```python
class AgencyConfig:
    name: str                    # Must match entry agent name
    description: str             # Agency purpose description
    storage_path: Optional[str]  # Path for persistent storage
    shared_instructions: Optional[str]  # Shared instructions file
    default_temperature: float = 0.7    # Default LLM temperature
    default_max_tokens: int = 4096      # Default max tokens
    use_code_interpreter: bool = False  # Enable code execution
    use_rag: bool = False              # Enable RAG capabilities
    use_file_storage: bool = False     # Enable file storage
```

### Agent Configuration
```python
class AgentConfig:
    name: str              # Unique agent name
    description: str       # Agent role description
    instructions: str      # Path to instructions file
    tools_folder: str      # Path to tools directory
    llm_provider: str      # LLM provider name
    provider_config: Dict  # Provider-specific settings
    temperature: float     # LLM temperature
    max_tokens: int        # Max tokens per response
```

## Storage Configuration

### File Storage
- Enable with `use_file_storage=True`
- Set `storage_path` for persistent storage
- Files are stored in `{storage_path}/files`
- Each file gets a unique ID and metadata

### State Persistence
- State is saved in JSON format
- Includes all threads and messages
- Preserves flow configurations
- Maintains message history

### RAG System
- Enable with `use_rag=True`
- Knowledge base stored in `{storage_path}/rag`
- Supports document search and retrieval
- Maintains document embeddings

## Best Practices

### 1. Agency Setup
- Match agency name with entry agent
- Use descriptive agent names
- Define clear communication flows
- Enable only needed features

### 2. Storage Management
- Use absolute paths for storage
- Implement regular state backups
- Clean up unused files
- Monitor storage usage

### 3. Performance Optimization
- Limit number of agents
- Optimize flow patterns
- Use appropriate LLM settings
- Monitor resource usage

### 4. Security Considerations
- Secure storage paths
- Validate file uploads
- Control code execution
- Manage API keys safely

## Common Issues and Solutions

### 1. Message Routing Issues
**Problem**: Messages not reaching intended agents
**Solution**: 
- Verify agency name matches entry agent
- Check flow definitions
- Ensure agents exist in agency

### 2. Storage Problems
**Problem**: Files or state not persisting
**Solution**:
- Check storage path permissions
- Verify path exists
- Use absolute paths
- Enable required features

### 3. Performance Issues
**Problem**: Slow message processing
**Solution**:
- Optimize flow patterns
- Adjust LLM settings
- Monitor resource usage
- Implement caching

### 4. Configuration Errors
**Problem**: Agency initialization fails
**Solution**:
- Verify all paths exist
- Check agent names
- Validate flow definitions
- Enable required features

## Configuration Checklist

Before deploying your agency, verify:

- [ ] Agency name matches entry agent
- [ ] All agent names are unique
- [ ] Communication flows are correctly defined
- [ ] Storage paths are valid and accessible
- [ ] Required features are enabled
- [ ] Instructions files exist
- [ ] Tool folders are properly set up
- [ ] LLM providers are configured
- [ ] API keys are properly set
- [ ] State persistence is tested 