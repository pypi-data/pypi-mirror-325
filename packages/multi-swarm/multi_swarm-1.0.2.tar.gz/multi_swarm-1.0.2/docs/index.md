# Multi-Swarm Framework Documentation

Latest Version: 1.0.2

## What's New

### v1.0.2 Features
- Task-specific model configurations for optimal performance
- Enhanced agency management with `AgencyConfig`
- Improved thread management and message handling
- New communication flow system
- Better state persistence and configuration management

# Welcome to Multi-Swarm

Multi-Swarm is a powerful framework for creating collaborative AI agent swarms. It enables you to build complex systems where multiple AI agents work together, each with specific roles and capabilities.

## Key Features

### 🤖 Intelligent Agents
- Create specialized agents with distinct roles
- Automatic model selection based on agent tasks
- Built-in support for Claude and Gemini models
- Extensible agent capabilities through custom tools

### 🔄 Communication Flows
- Directional message routing between agents
- Thread-based conversations
- Broadcast messaging capabilities
- State persistence and recovery

### 🛠️ Custom Tools
- Create powerful tools using Pydantic
- Built-in error handling and validation
- Support for async operations
- Resource management and monitoring

### 📚 Knowledge Management
- Built-in RAG (Retrieval-Augmented Generation)
- File storage and management
- Code interpretation capabilities
- Shared knowledge base across agents

### 🔒 Security & Reliability
- Secure code execution environment
- API key management
- Error handling and recovery
- State persistence and backup

## Quick Start

```python
from multi_swarm import Agency, Agent

# Create specialized agents
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

# Define communication flows
flows = [
    (ceo, developer),     # CEO can assign tasks to Developer
    (developer, ceo),     # Developer can report back to CEO
]

# Create agency
agency = Agency(
    name="CEO",           # Must match entry agent name
    description="Development Agency",
    agents=[ceo, developer],
    flows=flows
)

# Run the agency
agency.run_demo()
```

## Installation

```bash
pip install multi-swarm
```

## Environment Setup

```bash
# Required for Claude integration
ANTHROPIC_API_KEY=your_claude_key

# Required for Gemini integration
GOOGLE_API_KEY=your_gemini_key
```

## Core Concepts

### Agents
Agents are the building blocks of your system. Each agent has:
- A specific role and set of responsibilities
- Custom tools for performing tasks
- Access to LLM capabilities
- Communication abilities with other agents

### Tools
Tools are the actions agents can perform:
- Built using Pydantic for validation
- Can integrate with external services
- Support async operations
- Include proper error handling

### Communication Flows
Messages flow between agents through:
- Directional connections
- Thread-based conversations
- Broadcast capabilities
- State persistence

### Agency
The agency manages:
- Agent coordination
- Message routing
- Resource allocation
- State management

## Best Practices

1. **Agent Design**
   - Give agents focused responsibilities
   - Match agent names with roles
   - Provide clear instructions
   - Enable appropriate features

2. **Message Handling**
   - Use proper message format
   - Include required fields
   - Handle errors gracefully
   - Maintain thread context

3. **State Management**
   - Enable state persistence
   - Use proper storage paths
   - Implement backups
   - Monitor resource usage

4. **Security**
   - Secure API keys
   - Validate inputs
   - Control code execution
   - Monitor operations

## Next Steps

- [Installation Guide](getting-started/installation.md)
- [Quick Start Guide](getting-started/quickstart.md)
- [Creating Agents](user-guide/creating-agents.md)
- [Creating Tools](user-guide/creating-tools.md)
- [Agency Configuration](user-guide/agency-configuration.md)
- [Testing Guide](user-guide/testing.md)

## Support

- [GitHub Issues](https://github.com/yourusername/multi-swarm/issues)
- [Documentation](https://multi-swarm.readthedocs.io/)
- [Examples](examples/basic_agency.md)
- [Contributing](contributing.md) 