# API Reference

This is the API reference for Multi-Swarm, documenting all public classes and methods.

## Core Classes

### Agency

```python
class Agency:
    """
    Main agency class that manages agents and their communication.
    
    Args:
        agents (List[Union[Agent, List[Agent]]]): List of agents and communication flows
        config (Optional[AgencyConfig]): Agency configuration
        
    Attributes:
        name (str): Agency name
        agents (Dict[str, Agent]): Dictionary of agents by name
        thread_manager (ThreadManager): Thread management system
        state_manager (StateManager): State persistence system
        rag_system (Optional[RAGSystem]): RAG system if enabled
    """
    
    def process_message(
        self,
        message: str,
        thread_id: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> Message:
        """
        Process a message through the agency.
        
        Args:
            message (str): Message content
            thread_id (Optional[str]): Thread ID for continuing conversations
            metadata (Optional[Dict]): Additional message metadata
            
        Returns:
            Message: Response message from the agency
        """
        
    def save_state(self) -> None:
        """Save agency state to storage."""
        
    def load_state(self) -> None:
        """Load agency state from storage."""
```

### Agent

```python
class Agent:
    """
    Base agent class that handles message processing and tool usage.
    
    Args:
        name (str): Agent name
        config (Optional[AgentConfig]): Agent configuration
        
    Attributes:
        name (str): Agent name
        tools (List[BaseTool]): List of available tools
        thread_manager (ThreadManager): Thread management system
        llm_client (LLMClient): LLM client for processing
    """
    
    def process_message(
        self,
        message: Message,
        thread: Thread
    ) -> Message:
        """
        Process a message and return a response.
        
        Args:
            message (Message): Input message
            thread (Thread): Message thread
            
        Returns:
            Message: Response message
        """
        
    def add_tool(self, tool: BaseTool) -> None:
        """
        Add a tool to the agent.
        
        Args:
            tool (BaseTool): Tool to add
        """
```

### Thread

```python
class Thread:
    """
    Message thread management.
    
    Args:
        id (Optional[str]): Thread ID
        
    Attributes:
        id (str): Thread ID
        messages (List[Message]): List of messages
        metadata (Dict): Thread metadata
    """
    
    def add_message(
        self,
        content: str,
        role: str,
        agent_name: str,
        metadata: Optional[Dict] = None
    ) -> Message:
        """
        Add a message to the thread.
        
        Args:
            content (str): Message content
            role (str): Message role (user/assistant)
            agent_name (str): Name of the agent
            metadata (Optional[Dict]): Message metadata
            
        Returns:
            Message: Created message
        """
        
    def get_messages(self) -> List[Message]:
        """Get all messages in the thread."""
```

### Message

```python
class Message:
    """
    Message class for agent communication.
    
    Args:
        content (str): Message content
        role (str): Message role (user/assistant)
        agent_name (str): Name of the agent
        metadata (Optional[Dict]): Message metadata
        
    Attributes:
        id (str): Message ID
        content (str): Message content
        role (str): Message role
        agent_name (str): Agent name
        metadata (Dict): Message metadata
        timestamp (datetime): Creation timestamp
    """
```

### BaseTool

```python
class BaseTool:
    """
    Base class for agent tools.
    
    All tools must inherit from this class and implement the run method.
    """
    
    def run(self) -> Any:
        """
        Execute the tool's functionality.
        
        Returns:
            Any: Tool execution result
        
        Raises:
            ToolError: If tool execution fails
        """
        raise NotImplementedError
```

## Configuration Classes

### AgencyConfig

```python
@dataclass
class AgencyConfig:
    """
    Agency configuration options.
    
    Args:
        name (str): Agency name
        description (str): Agency description
        storage_path (str): Path for storage
        state_file (str): State file name
        max_history (int): Maximum message history
        enable_rag (bool): Enable RAG system
        rag_config (Optional[Dict]): RAG configuration
    """
    name: str
    description: str
    storage_path: str = "./storage"
    state_file: str = "agency_state.json"
    max_history: int = 1000
    enable_rag: bool = False
    rag_config: Optional[Dict] = None
```

### AgentConfig

```python
@dataclass
class AgentConfig:
    """
    Agent configuration options.
    
    Args:
        name (str): Agent name
        description (str): Agent description
        llm_provider (str): LLM provider name
        provider_config (Dict): Provider configuration
        temperature (float): LLM temperature
        max_tokens (int): Maximum tokens
        tools_folder (str): Tools folder path
    """
    name: str
    description: str
    llm_provider: str = "claude"
    provider_config: Dict = None
    temperature: float = 0.5
    max_tokens: int = 4096
    tools_folder: str = "./tools"
```

## System Classes

### ThreadManager

```python
class ThreadManager:
    """
    Manages message threads.
    
    Args:
        max_history (int): Maximum thread history
        
    Methods:
        create_thread() -> Thread
        get_thread(thread_id: str) -> Thread
        get_all_threads() -> List[Thread]
        cleanup_old_threads() -> None
    """
```

### StateManager

```python
class StateManager:
    """
    Manages state persistence.
    
    Args:
        storage_path (str): Storage path
        state_file (str): State file name
        
    Methods:
        save_state(state: Dict) -> None
        load_state() -> Dict
        cleanup_old_states() -> None
    """
```

### RAGSystem

```python
class RAGSystem:
    """
    Retrieval-Augmented Generation system.
    
    Args:
        config (Dict): RAG configuration
        
    Methods:
        add_document(content: str, metadata: Dict) -> None
        search(query: str, k: int = 3) -> List[Document]
        update_index() -> None
    """
```

## Exceptions

### ToolError

```python
class ToolError(Exception):
    """
    Error raised by tools.
    
    Args:
        message (str): Error message
        error_type (str): Error type
        context (Dict): Error context
    """
```

### AgencyError

```python
class AgencyError(Exception):
    """
    Error raised by agency operations.
    
    Args:
        message (str): Error message
        error_type (str): Error type
        context (Dict): Error context
    """
```

## Learn More

- [User Guide](../user-guide/index.md)
- [Configuration Guide](../user-guide/configuration.md)
- [Testing Guide](../user-guide/testing.md) 