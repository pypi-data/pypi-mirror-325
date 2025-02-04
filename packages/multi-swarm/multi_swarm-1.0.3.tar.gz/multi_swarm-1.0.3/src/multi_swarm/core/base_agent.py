import os
from openai import OpenAI
import anthropic
from typing import Optional, Dict, Any, List
from pathlib import Path
from datetime import datetime
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from .thread import Thread, ThreadManager, Message
from .file import FileManager
from .interpreter import CodeInterpreter
from .rag import RAGSystem

# Load environment variables
load_dotenv(override=True)  # Force reload of environment variables

class AgentConfig(BaseModel):
    """
    Configuration for an agent.
    
    Attributes:
        name: Name of the agent
        description: Description of the agent's role
        instructions_path: Path to the agent's instructions file
        tools_folder: Path to the agent's tools folder
        llm_provider: LLM provider to use
        provider_config: Provider-specific configuration
        temperature: Temperature for LLM sampling
        max_prompt_tokens: Maximum tokens in conversation history
        storage_path: Path for persistent storage
        use_code_interpreter: Whether to enable code interpreter
        use_rag: Whether to enable RAG capabilities
        use_file_storage: Whether to enable file storage
    """
    name: str = Field(..., description="Name of the agent")
    description: str = Field(..., description="Description of the agent's role")
    instructions_path: str
    tools_folder: Optional[str] = Field(None, description="Path to the agent's tools folder")
    llm_provider: str = Field(..., description="LLM provider to use (claude/gemini)")
    provider_config: Dict[str, Any] = Field(..., description="Provider-specific configuration")
    temperature: float = Field(0.7, description="Temperature for generation")
    max_prompt_tokens: int = 4096
    storage_path: Optional[str] = None
    use_code_interpreter: bool = False
    use_rag: bool = False
    use_file_storage: bool = False

class MockClient:
    """Mock LLM client for testing."""
    def messages(self):
        return self
        
    def create(self, *args, **kwargs):
        return type('Response', (), {
            'content': [type('Content', (), {'text': 'Mock response'})()]
        })

class BaseAgent:
    """Base class for all agents in the framework."""
    def __init__(
        self,
        name: str,
        description: str,
        instructions: str,
        llm_provider: str,
        provider_config: Dict[str, Any],
        temperature: float = 0.7
    ):
        self.config = AgentConfig(
            name=name,
            description=description,
            instructions_path=instructions,
            llm_provider=llm_provider,
            provider_config=provider_config,
            temperature=temperature
        )
        
        # Initialize LLM client based on provider
        if llm_provider == "claude":
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        elif llm_provider == "gemini":
            self.client = OpenAI(
                api_key=os.getenv("GOOGLE_API_KEY"),
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
            )
        elif llm_provider == "mock":
            self.client = MockClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")
        
        # Load instructions
        with open(instructions, 'r') as f:
            self.instructions = f.read()
            
    def _determine_provider(self) -> str:
        """Determine the best LLM provider based on the agent's role."""
        raise NotImplementedError("This method should be implemented by Agent class")
        
    def _get_provider_config(self, config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Get provider configuration, using defaults if not specified."""
        raise NotImplementedError("This method should be implemented by Agent class")
        
    def _load_tools(self) -> List[Any]:
        """Load tools from the tools folder."""
        raise NotImplementedError("This method should be implemented by Agent class")
        
    def _validate_environment(self) -> None:
        """Validate that all required environment variables are set."""
        raise NotImplementedError("This method should be implemented by Agent class")

    def process_message(self, message: str) -> str:
        """Process a message using the appropriate LLM."""
        try:
            # Check if the message contains a request to another agent
            if "@Gemini" in message and self.config.llm_provider == "claude":
                # Split the message at @Gemini
                analysis, request = message.split("@Gemini")
                # First get Claude's response
                claude_response = self._process_with_llm(analysis)
                # Then forward to Gemini
                gemini_request = f"Claude's analysis:\n{claude_response}\n\nRequest:{request}"
                return f"{claude_response}\n\nForwarding to Gemini for optimization suggestions..."
            
            # Process normally if no agent routing
            if self.config.llm_provider == "claude":
                # Check for API key
                api_key = os.getenv("ANTHROPIC_API_KEY")
                if not api_key:
                    return "Error: ANTHROPIC_API_KEY not found in environment variables"
                
                # Create message using the correct format for Claude
                response = self.client.messages.create(
                    model=self.config.provider_config["model"],
                    max_tokens=self.config.provider_config.get("max_tokens", 4096),
                    messages=[
                        {
                            "role": "user",
                            "content": message
                        }
                    ],
                    system=self.instructions
                )
                return response.content[0].text
            
            elif self.config.llm_provider == "gemini":
                # Check for API key
                api_key = os.getenv("GOOGLE_API_KEY")
                if not api_key:
                    return "Error: GOOGLE_API_KEY not found in environment variables"
                
                # For Gemini, include instructions in the user message
                full_message = f"Instructions: {self.instructions}\n\nUser message: {message}\n\nAssistant:"
                
                # Create message using OpenAI compatibility layer
                response = self.client.chat.completions.create(
                    model="gemini-pro",
                    messages=[
                        {
                            "role": "user",
                            "content": full_message
                        }
                    ]
                )
                return response.choices[0].message.content
            
        except Exception as e:
            return f"Error processing message: {str(e)}\nPlease check your API keys and try again."

    def _process_with_llm(self, thread: Thread) -> str:
        """
        Process a thread with the LLM provider.
        
        This method should be implemented by specific provider implementations.
        """
        raise NotImplementedError

    def upload_file(
        self,
        file: Any,
        filename: str,
        purpose: str = "attachment",
        metadata: Dict = None
    ):
        """Upload a file to storage."""
        if not self.file_manager:
            raise RuntimeError("File storage not enabled for this agent")
        return self.file_manager.upload_file(file, filename, purpose, metadata)

    def execute_code(
        self,
        code: str,
        language: str = "python",
        additional_files: Dict[str, str] = None,
        environment: Dict[str, str] = None
    ):
        """Execute code in the secure environment."""
        if not self.code_interpreter:
            raise RuntimeError("Code interpreter not enabled for this agent")
        return self.code_interpreter.execute(code, language, additional_files, environment)

    def search_knowledge(
        self,
        query: str,
        k: int = 5,
        threshold: float = None
    ):
        """Search the knowledge base using RAG."""
        if not self.rag_system:
            raise RuntimeError("RAG not enabled for this agent")
        return self.rag_system.search(query, k, threshold)

    def add_to_knowledge(
        self,
        content: str,
        metadata: Dict = None
    ):
        """Add content to the knowledge base."""
        if not self.rag_system:
            raise RuntimeError("RAG not enabled for this agent")
        return self.rag_system.add_document(content, metadata)

    def get_tool(self, tool_name: str) -> Optional[Any]:
        """Get a tool by name."""
        return self.tools.get(tool_name)

    def list_tools(self) -> List[str]:
        """List available tools."""
        return list(self.tools.keys())

    def save_state(self):
        """Save agent state to storage."""
        if not self.storage_path:
            return
            
        self.thread_manager.save_all_threads()
        if self.file_manager:
            self.file_manager._save_index()
        if self.rag_system:
            self.rag_system._save_state()
    
    def load_state(self):
        """Load agent state from storage."""
        if not self.storage_path:
            return
            
        self.thread_manager.load_all_threads()
        if self.file_manager:
            self.file_manager._load_index()
        if self.rag_system:
            self.rag_system._load_state() 