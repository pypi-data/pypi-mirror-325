# Core API Reference

This document provides detailed information about the core classes and functions in Multi-Swarm, updated with the latest testing experience and requirements.

## Message Handling

Messages are the foundation of agent communication. Each message must include:

```python
class Message(BaseModel):
    """
    Represents a message in a conversation thread.
    
    Attributes:
        id: Unique identifier for the message
        role: Role of the message sender (e.g., "user", "assistant", "system")
        content: The actual message content
        created_at: Timestamp when the message was created
        agent_name: Name of the agent that created the message (REQUIRED)
        metadata: Additional metadata about the message
        file_ids: List of file IDs attached to this message
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    role: str
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    agent_name: str  # Required field
    metadata: Dict = Field(default_factory=dict)
    file_ids: List[str] = Field(default_factory=list)
```

### Message Creation Best Practices

Always use the Thread.add_message method:

```python
thread.add_message(
    content="Your message",
    role="user|assistant",
    agent_name="agent_name",  # Required
    metadata={}  # Optional
)
```

Do not create messages directly or pass dictionaries to add_message.

## Agent

The foundation class for all agents in Multi-Swarm.

### Constructor

```python
def __init__(
    self,
    name: str,
    description: str,
    instructions: str,
    tools_folder: str,
    llm_provider: Optional[str] = None,
    provider_config: Optional[Dict[str, Any]] = None,
    temperature: float = 0.7,
    storage_path: Optional[str] = None,
    use_file_storage: bool = False,
    use_rag: bool = False,
    use_code_interpreter: bool = False
)
```

#### Parameters

- **name** (str): Unique identifier for the agent (must match agency name if entry agent)
- **description** (str): Description of the agent's role and capabilities
- **instructions** (str): Path to instructions file
- **tools_folder** (str): Path to tools directory
- **llm_provider** (str, optional): LLM provider to use ("claude" or "gemini")
- **provider_config** (Dict, optional): Provider-specific settings
- **temperature** (float, optional): Response randomness (0.0-1.0)
- **storage_path** (str, optional): Path for persistent storage
- **use_file_storage** (bool): Enable file storage capabilities
- **use_rag** (bool): Enable RAG capabilities
- **use_code_interpreter** (bool): Enable code interpreter

### Automatic Model Selection

The framework automatically selects the most appropriate LLM model based on the task type. Below is the comprehensive mapping of tasks to their optimal models:

#### Code Generation & Development
```python
TASK_PREFERENCES = {
    # Code Generation & Development
    "code_generation_general": "claude",      # Better code structure and patterns
    "code_generation_python": "claude",       # Superior Python understanding
    "code_generation_javascript": "claude",   # Better JS and web concepts
    "code_generation_sql": "claude",         # Strong database and query optimization
    "code_generation_algorithms": "claude",   # Better algorithm implementation
    "code_review": "claude",                 # Better code quality assessment
    "code_debugging": "claude",              # Superior step-by-step debugging
    "code_optimization": "claude",           # Better performance optimization
    "code_security": "claude",               # Better security principle understanding
    "code_documentation": "claude",          # Better code documentation
    
    # Research & Analysis
    "research_academic": "claude",           # Better academic paper comprehension
    "research_market": "claude",             # Better market analysis
    "research_technical": "claude",          # Better technical depth
    "research_scientific": "claude",         # Better scientific reasoning
    "research_legal": "claude",              # Better legal comprehension
    "analysis_quantitative": "claude",       # Better numerical analysis
    "analysis_qualitative": "claude",        # Better pattern recognition
    "analysis_sentiment": "claude",          # Better emotional understanding
    
    # Writing & Documentation
    "writing_technical": "claude",           # Better technical clarity
    "writing_creative": "claude",            # Better creative writing
    "writing_business": "claude",            # Better business communication
    "writing_documentation": "claude",       # Better documentation structure
    "writing_api_docs": "claude",            # Better API documentation
    "writing_user_guides": "claude",         # Better user-focused writing
    
    # Planning & Strategy
    "planning_strategic": "claude",          # Better strategic thinking
    "planning_project": "claude",            # Better project planning
    "planning_architecture": "claude",       # Better system architecture
    "planning_risk": "claude",               # Better risk assessment
    
    # Data Processing & Analysis
    "data_preprocessing": "gemini",          # Faster data preprocessing
    "data_pipeline": "gemini",               # Better pipeline processing
    "data_streaming": "gemini",              # Better real-time processing
    "data_transformation": "gemini",         # Faster data transformation
    "data_validation": "claude",             # Better data validation logic
    "data_visualization_code": "claude",     # Better visualization coding
    "data_visualization_realtime": "gemini", # Better real-time visualization
    
    # Real-time Operations
    "realtime_processing": "gemini",         # Faster processing speed
    "realtime_monitoring": "gemini",         # Better monitoring capabilities
    "realtime_alerting": "gemini",           # Faster alert processing
    "realtime_analytics": "gemini",          # Better real-time analytics
    
    # System Operations
    "ops_deployment": "gemini",              # Better deployment handling
    "ops_monitoring": "gemini",              # Better system monitoring
    "ops_scaling": "gemini",                 # Better scaling operations
    "ops_troubleshooting": "claude",         # Better problem analysis
    
    # Integration
    "integration_design": "claude",          # Better integration design
    "integration_implementation": "claude",   # Better integration code
    "integration_testing": "claude",         # Better test design
    "integration_monitoring": "gemini",      # Better integration monitoring
    
    # Machine Learning
    "ml_model_design": "claude",            # Better model architecture
    "ml_feature_engineering": "claude",      # Better feature design
    "ml_training": "gemini",                # Faster training processing
    "ml_optimization": "claude",            # Better optimization strategy
    "ml_evaluation": "claude",              # Better evaluation analysis
    
    # Natural Language Processing
    "nlp_text_analysis": "claude",          # Better text understanding
    "nlp_sentiment_analysis": "claude",     # Better sentiment comprehension
    "nlp_topic_modeling": "claude",         # Better topic extraction
    "nlp_text_generation": "claude",        # Better text generation
    "nlp_summarization": "claude",          # Better text summarization
    
    # Domain-Specific
    "domain_medical": "claude",             # Better medical knowledge
    "domain_legal": "claude",               # Better legal understanding
    "domain_financial": "claude",           # Better financial analysis
    "domain_scientific": "claude",          # Better scientific comprehension
    
    # Default Fallbacks
    "default_analysis": "claude",           # Default for analysis tasks
    "default_processing": "gemini",         # Default for processing tasks
    "default_general": "gemini"             # General default
}
```

#### Model Selection Strategy

The framework uses the following strategy to select the appropriate model:

1. **Task-Based Selection**: First attempts to match the specific task type (e.g., "code_generation_python")
2. **Category Fallback**: If no specific task match, falls back to category default (e.g., "default_analysis")
3. **General Fallback**: If no category match, uses "default_general"

Example usage:

```python
from multi_swarm import Agent

# The agent's description is used to determine the task type
agent = Agent(
    name="PythonDev",
    description="Python code generation and review specialist",
    # No need to specify llm_provider - automatically selects Claude
    temperature=0.7
)

# For data processing tasks
agent = Agent(
    name="DataProcessor",
    description="Real-time data pipeline processing",
    # Automatically selects Gemini
    temperature=0.5
)
```

### Methods

#### process_message

```python
def process_message(
    self,
    thread_id: str,
    content: str,
    role: str = "user",
    metadata: Dict = None
) -> Message:
    """
    Process a message in a thread.
    
    Args:
        thread_id: ID of the thread to process
        content: Message content
        role: Message role (default: "user")
        metadata: Additional metadata
        
    Returns:
        The created Message instance
        
    Note:
        The agent_name is automatically set to the agent's name
    """
```

#### create_thread

```python
def create_thread(
    self,
    metadata: Dict = None
) -> Thread:
    """Create a new conversation thread."""
```

#### upload_file

```python
def upload_file(
    self,
    file: Any,
    filename: str,
    purpose: str = "attachment",
    metadata: Dict = None
):
    """Upload a file to storage."""
```

#### execute_code

```python
def execute_code(
    self,
    code: str,
    language: str = "python",
    additional_files: Dict[str, str] = None,
    environment: Dict[str, str] = None
):
    """Execute code in the secure environment."""
```

#### search_knowledge

```python
def search_knowledge(
    self,
    query: str,
    k: int = 5,
    threshold: float = None
):
    """Search the knowledge base using RAG."""
```

## Agency

The main class for managing agent interactions.

### Constructor

```python
def __init__(
    self,
    name: str,
    description: str,
    agents: List[Agent],
    flows: List[Tuple[BaseAgent, BaseAgent]],
    storage_path: Optional[str] = None,
    shared_instructions: Optional[str] = None,
    use_code_interpreter: bool = False,
    use_rag: bool = False,
    use_file_storage: bool = False
)
```

#### Important Notes

1. The agency's name MUST match the entry agent's name
2. Flows are directional (source → target)
3. Each flow creates its own thread
4. Bi-directional communication requires explicit flows in both directions

### State Persistence

The agency state includes:

1. **Threads**:
   - Messages with all fields
   - Thread metadata
   - Creation and activity timestamps
   - Thread status

2. **Flows**:
   - Source and target agents
   - Thread IDs
   - Flow status

3. **Storage**:
   - File storage (if enabled)
   - RAG indexes (if enabled)
   - Code interpreter state (if enabled)

### Methods

#### run

```python
def run(self, prompt: str) -> Union[str, Dict]:
    """
    Process a prompt through the agency's workflow.
    
    Args:
        prompt: The input prompt to process
        
    Returns:
        Combined response from all agents
        
    Note:
        Uses the first flow's thread for processing
    """
```

#### process_message

```python
def process_message(self, message: str) -> str:
    """
    Process a message through the agency.
    
    Args:
        message: The message to process
        
    Returns:
        Response from the entry agent
        
    Note:
        Creates a new thread for each message
    """
```

## Thread Management

Threads maintain conversation state and ensure proper message handling:

```python
class Thread(BaseModel):
    """
    Represents a conversation thread.
    
    Attributes:
        id: Unique thread identifier
        messages: List of messages in the thread
        metadata: Thread metadata
        created_at: Thread creation timestamp
        last_active_at: Last activity timestamp
        status: Thread status
    """
    id: str
    messages: List[Message]
    metadata: Dict
    created_at: datetime
    last_active_at: datetime
    status: str
    
    def add_message(
        self,
        content: str,
        role: str = "user",
        agent_name: str = "user",
        metadata: Optional[Dict] = None
    ) -> None:
        """
        Add a message to the thread.
        
        Args:
            content: Message content
            role: Message role
            agent_name: Name of the agent (REQUIRED)
            metadata: Additional metadata
        """
```

## Configuration

### Environment Variables

```bash
# Required for Claude
ANTHROPIC_API_KEY=your_claude_key

# Required for Gemini
GOOGLE_API_KEY=your_gemini_key
```

### Provider Configurations

```python
# Claude Configuration
CLAUDE_CONFIG = {
    "model": "claude-3-sonnet",
    "api_version": "2024-03",
    "max_tokens": 4096
}

# Gemini Configuration
GEMINI_CONFIG = {
    "model": "gemini-pro",
    "api_version": "2024-01",
    "max_tokens": 4096
}
```

## Error Handling

The framework includes comprehensive error handling:

```python
try:
    response = agency.run("Test message")
except AgencyError as e:
    if "message_error" in str(e):
        # Handle message processing error
        handle_message_error(e)
    elif "flow_error" in str(e):
        # Handle flow routing error
        handle_flow_error(e)
    elif "state_error" in str(e):
        # Handle state persistence error
        handle_state_error(e)
    else:
        # Handle other agency errors
        raise
```

## Best Practices

1. **Message Handling**
   - Always use Thread.add_message
   - Include required agent_name
   - Use proper message roles
   - Keep metadata JSON-serializable

2. **State Management**
   - Enable state persistence for production
   - Use absolute paths for storage
   - Implement regular backups
   - Monitor storage usage

3. **Flow Configuration**
   - Match agency name with entry agent
   - Define explicit bi-directional flows
   - Monitor thread creation
   - Handle flow errors

4. **Error Handling**
   - Implement comprehensive error handling
   - Log errors with context
   - Monitor error patterns
   - Implement recovery strategies

## Usage Example

```python
from multi_swarm import Agency, Agent

# Create custom agent
class DevelopmentAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Developer",
            description="Code generation and review specialist",
            instructions="instructions.md",
            tools_folder="./tools",
            # Let the framework choose between Claude and Gemini
            temperature=0.7,
            use_code_interpreter=True
        )

# Create agency
dev_agent = DevelopmentAgent()
qa_agent = QAAgent()

agency = Agency(
    name="Development Team",
    description="Software development team simulation",
    agents=[dev_agent, qa_agent],
    flows=[
        (dev_agent.name, qa_agent.name),
        (qa_agent.name, dev_agent.name)
    ],
    shared_instructions="manifesto.md",
    use_code_interpreter=True
)

# Run interactive demo
agency.run_demo()
```

## Learn More

- [Agent API](agents.md)
- [Tool API](tools.md)
- [Agency API](agency.md)
- [User Guide](../user-guide/creating-agents.md) 