# Multi-Swarm Release Notes

## v1.0.2 (03/02/2024)

### Improvements

#### Agent System
- Added task-specific model configurations for improved performance
- Enhanced provider selection based on task type
- Added detailed task preferences for different operations
- Updated model configurations with latest versions:
  - Claude: `claude-3-5-sonnet-latest` with 2024-03 API
  - Gemini: `gemini-2.0-flash-exp` with 2024-01 API

#### Agency Management
- Introduced new `AgencyConfig` class for better configuration management
- Enhanced file storage and RAG capabilities
- Improved code interpreter integration
- Added new communication flow management system
- Enhanced state management and persistence

#### Thread System
- Added enhanced message handling with metadata support
- Improved thread persistence and state management
- Added UTC timestamp handling for better time tracking
- Enhanced message context window management
- Added improved thread status tracking

#### Core Components
- Added new `ThreadManager` for better conversation management
- Introduced `CommunicationFlow` for improved agent interactions
- Added centralized configuration system
- Updated base agent class with enhanced capabilities

### Dependencies
- No changes to core dependencies
- Maintained compatibility with existing installations

### Migration
- No breaking changes
- Existing code will continue to work as before
- New features are opt-in and backward compatible

# Multi-Swarm v1.0.0 Release Notes

## 🎉 First Major Release

Multi-Swarm is a powerful framework for creating collaborative AI agent swarms, leveraging multiple LLM providers including Claude and Gemini. This first major release provides a stable API and comprehensive feature set for production use.

### ✨ Core Features

#### Multi-Agent Architecture
- Create collaborative agent swarms with distinct roles and capabilities
- Define custom agents with specific instructions and tools
- Flexible agency configuration with customizable communication flows
- Easy-to-use agent template creation system
- Automatic tool discovery and registration

#### LLM Integration
- Support for multiple LLM providers:
  - Claude (Anthropic) with claude-3-sonnet model
  - Gemini (Google) with gemini-pro model
- Configurable temperature and response parameters
- Automatic API key management and validation
- Graceful error handling for API limits and failures

#### Tool System
- Built-in tool creation framework using Pydantic
- Type validation and error handling
- Easy-to-extend base classes for custom tools
- Automatic tool registration and discovery
- Support for both synchronous and asynchronous tools

#### Communication System
- Full async/await support for concurrent operations
- Efficient message routing between agents
- Configurable communication flows
- Built-in conversation history management
- Support for complex multi-agent interactions

### 🔧 Technical Features

#### Code Quality
- Type hints throughout the codebase
- Comprehensive docstrings following Google style
- PEP 8 compliant
- Modular and extensible design

#### Testing & CI/CD
- Comprehensive test suite with pytest
- Async test support with pytest-asyncio
- Code coverage reporting
- Automated CI/CD pipeline with GitHub Actions

#### Documentation
- Detailed README with quick start guide
- Advanced usage examples
- API documentation
- Contributing guidelines
- Example implementations

### 📚 Getting Started

#### Installation
```bash
pip install multi-swarm
```

For development:
```bash
pip install multi-swarm[dev]
```

#### Environment Setup
Required environment variables:
```bash
ANTHROPIC_API_KEY=your_claude_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

#### Basic Usage
```python
from multi_swarm import Agency, BaseAgent

# Create custom agents
class MyAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="MyAgent",
            description="A custom agent for specific tasks",
            instructions="path/to/instructions.md",
            tools_folder="path/to/tools",
            model="claude-3-sonnet",
            temperature=0.7
        )

# Initialize and run agency
agency = Agency(
    agents=[MyAgent()],
    shared_instructions="agency_manifesto.md"
)
agency.run_demo()
```

### 🔜 Roadmap for v1.1.0

#### New Features
- Additional LLM providers:
  - OpenAI GPT-4
  - Cohere Command
  - Anthropic Claude 3 Opus
- Enhanced tool capabilities
- Web interface and dashboard
- Built-in visualization tools

#### Improvements
- Memory management system
- Performance optimizations
- Enhanced error handling
- Better rate limiting
- Caching system

#### Developer Experience
- CLI tool for agent creation
- Interactive documentation
- More example implementations
- Enhanced debugging tools

### 🐛 Known Issues

None at this time. This is a stable release ready for production use.

### 📝 Requirements

- Python 3.9+
- API keys for chosen LLM providers
- Internet connection for API access

### 🙏 Acknowledgments

Special thanks to all contributors who helped make this first major release possible. Your feedback, suggestions, and contributions have been invaluable in shaping Multi-Swarm into a robust framework for AI agent development.

## v1.0.1 (31/01/2024)

### Updates
- Updated Claude model to `claude-3-5-sonnet-latest` with API version 2024-03
- Updated Gemini model to `gemini-2.0-flash-exp` with API version 2024-01
- Improved automatic model selection based on agent roles
- Added Cursor AI integration instructions

### Fixed
- Fixed model configuration in base agent class
- Fixed agency initialization issues
- Improved error handling for model selection

## v1.0.0 (30/01/2025)

### Features
- Initial release of Multi-Swarm Framework
- Support for multiple LLM providers (Claude and Gemini)
- Agent template creation system
- Flexible agency configuration
- Built-in tools system
- Asynchronous communication between agents
- File management and storage
- Code execution environment
- Knowledge base integration 