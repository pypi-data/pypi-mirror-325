# Configuration Guide

This guide covers best practices for configuring Multi-Swarm agencies and agents based on our testing experience.

## Agency Configuration

### 1. Basic Setup

```python
from multi_swarm import Agency, Agent

# Create agents
agent1 = Agent("Agent1")
agent2 = Agent("Agent2")
agent3 = Agent("Agent3")

# Create agency with communication flows
agency = Agency([
    agent1,  # Entry point agent
    [agent1, agent2],  # Agent1 can communicate with Agent2
    [agent2, agent3],  # Agent2 can communicate with Agent3
    [agent1, agent3]   # Agent1 can communicate with Agent3
])
```

### 2. Configuration Options

```python
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class AgencyConfig:
    """Agency configuration options."""
    name: str
    description: str
    storage_path: str = "./storage"
    state_file: str = "agency_state.json"
    max_history: int = 1000
    enable_rag: bool = False
    rag_config: Optional[Dict] = None
    
@dataclass
class AgentConfig:
    """Agent configuration options."""
    name: str
    description: str
    llm_provider: str = "claude"
    provider_config: Dict = None
    temperature: float = 0.5
    max_tokens: int = 4096
    tools_folder: str = "./tools"
```

### 3. Storage Configuration

```python
# File storage configuration
agency = Agency(
    agents=[agent1, agent2],
    config=AgencyConfig(
        name="MyAgency",
        description="My agency description",
        storage_path="./my_agency/storage",
        state_file="my_agency_state.json"
    )
)

# RAG system configuration
agency = Agency(
    agents=[agent1, agent2],
    config=AgencyConfig(
        name="MyAgency",
        description="My agency description",
        enable_rag=True,
        rag_config={
            "embeddings_model": "sentence-transformers/all-mpnet-base-v2",
            "vector_store": "faiss",
            "chunk_size": 1000
        }
    )
)
```

## Model Selection Configuration

### Task-Based Model Selection

The framework provides granular control over which LLM model (Claude or Gemini) is used for different tasks. This is configured through task preferences that map specific task types to the most suitable model.

### Configuration Options

1. **Explicit Provider Selection**
```python
agent = Agent(
    name="CustomAgent",
    description="Custom agent description",
    llm_provider="claude",  # Explicitly set the provider
    provider_config={
        "model": "claude-3-sonnet",
        "api_version": "2024-03"
    }
)
```

2. **Automatic Selection Based on Task**
```python
# For code generation tasks - automatically uses Claude
agent = Agent(
    name="CodeGenerator",
    description="Python code generation specialist",
    # No need to specify llm_provider
)

# For real-time processing - automatically uses Gemini
agent = Agent(
    name="DataProcessor",
    description="Real-time data pipeline processing",
    # No need to specify llm_provider
)
```

### Task Categories and Model Mapping

The framework uses a comprehensive task-to-model mapping:

1. **Code Generation & Development** (Claude)
   - General code generation
   - Language-specific coding (Python, JavaScript, SQL)
   - Code review and debugging
   - Security and optimization

2. **Research & Analysis** (Claude)
   - Academic research
   - Market analysis
   - Technical research
   - Quantitative/Qualitative analysis

3. **Writing & Documentation** (Claude)
   - Technical writing
   - API documentation
   - User guides
   - Business communication

4. **Planning & Strategy** (Claude)
   - Strategic planning
   - Project planning
   - System architecture
   - Risk assessment

5. **Data Processing** (Gemini)
   - Data preprocessing
   - Pipeline processing
   - Real-time streaming
   - Data transformation

6. **Real-time Operations** (Gemini)
   - Processing
   - Monitoring
   - Alerting
   - Analytics

7. **System Operations** (Mixed)
   - Deployment (Gemini)
   - Monitoring (Gemini)
   - Scaling (Gemini)
   - Troubleshooting (Claude)

8. **Integration** (Mixed)
   - Design (Claude)
   - Implementation (Claude)
   - Testing (Claude)
   - Monitoring (Gemini)

9. **Machine Learning** (Mixed)
   - Model Design (Claude)
   - Feature Engineering (Claude)
   - Training (Gemini)
   - Evaluation (Claude)

10. **Natural Language Processing** (Claude)
    - Text Analysis
    - Sentiment Analysis
    - Topic Modeling
    - Text Generation

11. **Domain-Specific** (Claude)
    - Medical
    - Legal
    - Financial
    - Scientific

### Model Selection Process

The framework follows this process to select the appropriate model:

1. **Task Matching**
   ```python
   # Matches specific task type
   agent = Agent(
       name="PythonDev",
       description="Python code generation specialist"
       # Automatically selects Claude based on code_generation_python task
   )
   ```

2. **Category Fallback**
   ```python
   # Falls back to category default
   agent = Agent(
       name="Analyst",
       description="General analysis tasks"
       # Falls back to default_analysis (Claude)
   )
   ```

3. **General Fallback**
   ```python
   # Uses general default
   agent = Agent(
       name="GeneralAgent",
       description="General purpose agent"
       # Falls back to default_general (Gemini)
   )
   ```

### Best Practices

1. **Task Description**
   - Use specific task-related terms in descriptions
   - Match descriptions to task categories
   - Be explicit about primary functionality

2. **Model Selection**
   - Let automatic selection work when possible
   - Override only when necessary
   - Consider task characteristics

3. **Performance Optimization**
   - Use Claude for quality-critical tasks
   - Use Gemini for speed-critical tasks
   - Consider hybrid approaches for complex workflows

4. **Cost Management**
   - Monitor usage by model
   - Use appropriate model for task complexity
   - Consider batching similar tasks

## Best Practices

### 1. Agency Setup

1. **Agent Naming**
   - Use descriptive, unique names
   - Match agency name with entry agent
   - Follow consistent naming convention

2. **Communication Flows**
   - Define explicit flows
   - Consider bi-directional needs
   - Avoid circular dependencies

3. **Storage Management**
   - Use dedicated storage paths
   - Implement cleanup policies
   - Monitor storage usage

4. **Performance**
   - Configure appropriate limits
   - Enable caching when needed
   - Monitor resource usage

### 2. Security

1. **API Keys**
   ```python
   # Load from environment
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   agent = Agent(
       name="SecureAgent",
       config=AgentConfig(
           name="SecureAgent",
           description="Secure agent configuration",
           provider_config={
               "api_key": os.getenv("ANTHROPIC_API_KEY")
           }
       )
   )
   ```

2. **File Access**
   ```python
   # Secure file paths
   import os
   from pathlib import Path
   
   def secure_path(base_path: str, *parts: str) -> Path:
       """Create secure file path."""
       path = Path(base_path).resolve()
       for part in parts:
           if ".." in part:
               raise ValueError("Path traversal not allowed")
       return path.joinpath(*parts)
   
   storage_path = secure_path("./storage", "agency_data")
   ```

### 3. Error Handling

1. **Configuration Validation**
   ```python
   def validate_config(config: AgencyConfig):
       """Validate agency configuration."""
       if not config.name:
           raise ValueError("Agency name is required")
           
       if not os.path.exists(config.storage_path):
           os.makedirs(config.storage_path)
           
       if config.enable_rag and not config.rag_config:
           raise ValueError("RAG configuration required when RAG is enabled")
   ```

2. **Resource Management**
   ```python
   class ResourceManager:
       """Manage agency resources."""
       def __init__(self, config: AgencyConfig):
           self.config = config
           self.resources = {}
           
       def cleanup(self):
           """Clean up resources."""
           for resource in self.resources.values():
               try:
                   resource.close()
               except Exception as e:
                   logger.error(f"Cleanup failed: {str(e)}")
   ```

## Common Issues and Solutions

### 1. Message Routing

**Problem**: Messages not reaching intended agents
**Solution**:
```python
# Explicit flow definition
agency = Agency([
    agent1,
    [agent1, agent2, "forward"],  # Specify direction
    [agent2, agent1, "backward"]  # Enable bi-directional
])
```

### 2. Storage Problems

**Problem**: State not persisting
**Solution**:
```python
# Robust storage configuration
config = AgencyConfig(
    name="MyAgency",
    storage_path="./storage",
    state_file="state.json",
    max_history=1000  # Prevent excessive growth
)

# Regular cleanup
def cleanup_old_states(storage_path: str, max_age: int = 7):
    """Remove old state files."""
    for file in Path(storage_path).glob("*.json"):
        if file.stat().st_mtime < time.time() - max_age * 86400:
            file.unlink()
```

### 3. Performance Issues

**Problem**: Slow message processing
**Solution**:
```python
# Optimize configuration
config = AgencyConfig(
    name="MyAgency",
    max_history=100,  # Reduce history size
    enable_rag=True,
    rag_config={
        "chunk_size": 500,  # Smaller chunks
        "cache_size": 1000  # Enable caching
    }
)
```

### 4. Configuration Errors

**Problem**: Invalid configuration
**Solution**:
```python
# Configuration validation
def validate_agent_config(config: AgentConfig):
    """Validate agent configuration."""
    if config.temperature < 0 or config.temperature > 1:
        raise ValueError("Temperature must be between 0 and 1")
        
    if config.max_tokens < 1:
        raise ValueError("Max tokens must be positive")
        
    if not os.path.exists(config.tools_folder):
        raise ValueError(f"Tools folder not found: {config.tools_folder}")
```

## Configuration Checklist

Before deploying your agency:

1. **Basic Setup**
   - [ ] Agency name matches entry agent
   - [ ] All agents have unique names
   - [ ] Communication flows are correct
   - [ ] Storage paths are configured

2. **Security**
   - [ ] API keys are loaded from environment
   - [ ] File paths are secured
   - [ ] Access controls are in place
   - [ ] Sensitive data is protected

3. **Performance**
   - [ ] History limits are set
   - [ ] Cache is configured
   - [ ] Resource limits are defined
   - [ ] Monitoring is enabled

4. **Error Handling**
   - [ ] Configuration validation is implemented
   - [ ] Error recovery is in place
   - [ ] Resource cleanup is configured
   - [ ] Logging is set up

## Learn More

- [Creating Agents](creating-agents.md)
- [Testing Guide](testing.md)
- [API Reference](../api/configuration.md) 