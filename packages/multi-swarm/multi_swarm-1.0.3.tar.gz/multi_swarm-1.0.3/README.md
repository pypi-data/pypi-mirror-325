# Multi-Swarm Framework

A powerful framework for creating collaborative AI agent swarms, supporting multiple LLM providers and advanced agent management capabilities.

## Features

- **Multi-LLM Support**
  - Claude (Anthropic) integration with latest models
  - Gemini (Google) integration with latest models
  - Automatic model selection based on agent roles

- **Advanced Agency Management**
  - Flexible agent creation and configuration
  - Sophisticated communication flows between agents
  - State persistence and thread management
  - Automated task distribution and coordination

- **Built-in Tools**
  - Code Interpreter for executing Python code
  - File Search with RAG capabilities
  - Docker integration for isolated environments
  - Customizable tool creation framework

## Installation

```bash
pip install multi-swarm
```

## Quick Start

```python
from multi_swarm import Agency, Agent

# Create agents with specific roles
ceo = Agent(
    name="CEO",
    description="Manages overall strategy and coordination",
    llm_provider="claude",
    provider_config={
        "model": "claude-3-sonnet",
        "api_version": "2024-03"
    }
)

developer = Agent(
    name="Developer",
    description="Handles technical implementation",
    llm_provider="gemini",
    provider_config={
        "model": "gemini-pro",
        "api_version": "2024-01"
    }
)

# Create agency with communication flows
agency = Agency([
    ceo,  # Entry point for user communication
    [ceo, developer],  # CEO can communicate with Developer
])

# Run the agency
agency.run()
```

## Documentation

For detailed documentation, visit:
- [Getting Started Guide](https://github.com/bartvanspitaels99/multi-swarm/docs/getting-started)
- [API Reference](https://github.com/bartvanspitaels99/multi-swarm/docs/api)
- [Examples](https://github.com/bartvanspitaels99/multi-swarm/docs/examples)

## Requirements

- Python 3.8+
- Dependencies:
  - anthropic>=0.18.1
  - google-generativeai>=0.3.2
  - pydantic>=2.0.0
  - python-dotenv>=1.0.0
  - docker>=6.1.0
  - sentence-transformers>=2.2.0
  - faiss-cpu>=1.7.4
  - transformers>=4.38.0
  - torch>=2.0.0
  - numpy>=1.24.0
  - click>=8.0.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## Support

- Report issues on [GitHub Issues](https://github.com/bartvanspitaels99/multi-swarm/issues)
- Join discussions in [GitHub Discussions](https://github.com/bartvanspitaels99/multi-swarm/discussions)

## Authors

- Bart Van Spitaels (bart.vanspitaels@gmail.com) 