from typing import Optional, Dict, Any, List
from pathlib import Path
import os
from .base_agent import BaseAgent
from .thread import Thread
import importlib
import inspect
from multi_swarm.tools import BaseTool
from multi_swarm.core.config import AgentConfig
from .thread_manager import ThreadManager

class MockClient:
    """Mock LLM client for testing."""
    def messages(self):
        return self
        
    def create(self, *args, **kwargs):
        return type('Response', (), {
            'content': [type('Content', (), {'text': 'Mock response'})()]
        })

class Agent(BaseAgent):
    """
    Base class for all agents in the Multi-Swarm framework.
    
    This class provides core functionality for agents, including:
    - Thread management for conversations
    - File storage and retrieval
    - Code execution in a secure environment
    - RAG capabilities for knowledge retrieval
    - Tool management and execution
    - Automatic LLM provider selection
    """
    
    # Latest model configurations with task-specific settings
    CLAUDE_CONFIG = {
        "default": {
            "model": "claude-3-5-sonnet-latest",
            "max_tokens": 4096,
            "api_version": "2024-03"
        },
        "code": {
            "model": "claude-3-5-sonnet-latest",
            "max_tokens": 4096,
            "api_version": "2024-03",
            "temperature": 0.1  # Lower temperature for code tasks
        },
        "research": {
            "model": "claude-3-5-opus-latest",  # Use Opus for research
            "max_tokens": 4096,
            "api_version": "2024-03",
            "temperature": 0.7  # Higher temperature for research
        }
    }
    
    GEMINI_CONFIG = {
        "default": {
            "model": "gemini-2.0-flash-exp",  # Always use Flash Experimental for best performance
            "max_tokens": 4096,
            "api_version": "2024-01"
        },
        "data": {
            "model": "gemini-2.0-flash-exp",  # Use Flash Experimental for data tasks
            "max_tokens": 4096,
            "api_version": "2024-01",
            "temperature": 0.3  # Lower temperature for data tasks
        },
        "realtime": {
            "model": "gemini-2.0-flash-exp",  # Use Flash Experimental for realtime tasks
            "max_tokens": 2048,  # Lower tokens for faster response
            "api_version": "2024-01",
            "temperature": 0.5
        }
    }
    
    # Task categories and their preferred providers
    TASK_PREFERENCES = {
        # Code Generation & Development
        "code_generation": "claude",  # General code generation
        "code_review": "claude",      # Code review and analysis
        "debugging": "claude",        # Debugging and error analysis
        "refactoring": "claude",      # Code refactoring and optimization
        "api_design": "claude",       # API design and documentation
        
        # Research & Analysis
        "research": "claude",         # Deep research and analysis
        "planning": "claude",         # Strategic planning
        "architecture": "claude",     # System architecture design
        "documentation": "claude",    # Technical documentation
        "security": "claude",         # Security analysis
        
        # Writing & Documentation
        "technical_writing": "claude", # Technical documentation
        "content_creation": "claude",  # Content generation
        "documentation": "claude",     # General documentation
        
        # Data Processing & Analysis
        "data_processing": "gemini",   # Data transformation
        "statistical_analysis": "gemini", # Statistical analysis
        "data_pipeline": "gemini",     # Data pipeline operations
        "data_validation": "gemini",   # Data validation and cleaning
        
        # Real-time Operations
        "monitoring": "gemini",        # System monitoring
        "alerting": "gemini",         # Alert management
        "metrics": "gemini",          # Metrics processing
        "logging": "gemini",          # Log analysis
        
        # System Operations
        "deployment": "gemini",       # Deployment operations
        "integration": "gemini",      # System integration
        "automation": "gemini",       # Process automation
        "optimization": "gemini",     # Performance optimization
        
        # Machine Learning Operations
        "ml_training": "gemini",      # Model training
        "ml_inference": "gemini",     # Model inference
        "ml_pipeline": "gemini",      # ML pipeline operations
        "ml_monitoring": "gemini",    # Model monitoring
    }
    
    # Task categories grouped by provider
    TASK_CATEGORIES = {
        "code": ["code_generation", "code_review", "debugging", "refactoring", "api_design"],
        "research": ["research", "planning", "architecture", "documentation", "security"],
        "writing": ["technical_writing", "content_creation", "documentation"],
        "data": ["data_processing", "statistical_analysis", "data_pipeline", "data_validation"],
        "realtime": ["monitoring", "alerting", "metrics", "logging"],
        "system": ["deployment", "integration", "automation", "optimization"],
        "ml": ["ml_training", "ml_inference", "ml_pipeline", "ml_monitoring"]
    }
    
    # Category to provider mapping
    CATEGORY_PREFERENCES = {
        "code": "claude",
        "research": "claude",
        "writing": "claude",
        "data": "gemini",
        "realtime": "gemini",
        "system": "gemini",
        "ml": "gemini"
    }
    
    # Task-related keywords for better matching
    TASK_KEYWORDS = {
        'code': ['programming', 'software', 'development', 'coding', 'debugging', 'refactoring'],
        'research': ['research', 'study', 'investigation', 'planning', 'architecture'],
        'writing': ['documentation', 'content', 'text', 'technical writing'],
        'data': ['statistics', 'statistical analysis', 'analytics', 'dataset', 'processing', 'pipeline', 'data'],
        'realtime': ['monitoring', 'alerts', 'live', 'metrics', 'logging'],
        'system': ['deployment', 'infrastructure', 'operations', 'integration'],
        'ml': ['machine learning', 'ai', 'model', 'training', 'inference']
    }
    
    def __init__(self, name: str, description: str, instructions: str, tools_folder: str,
                 llm_provider: Optional[str] = None, provider_config: Optional[Dict[str, Any]] = None,
                 temperature: float = 0.5, max_prompt_tokens: int = 25000):
        """Initialize the agent with the given configuration.
        
        Args:
            name: The name of the agent
            description: Description of the agent's role and capabilities
            instructions: Path to the agent's instruction file
            tools_folder: Path to the folder containing the agent's tools
            llm_provider: Optional provider override. If not specified, will be determined from description
            provider_config: Optional provider configuration override
            temperature: Temperature for LLM responses
            max_prompt_tokens: Maximum tokens to include in prompt context
        """
        # Store the provider selection for use in config generation
        self.llm_provider = llm_provider or self._determine_provider_from_description(description)
        
        # Get the base configuration for the selected provider and task
        base_config = self._get_provider_config(None, description)
        
        # If provider_config is provided, merge it with base_config
        if provider_config is not None:
            # For complete override, use provider_config directly
            if all(key in provider_config for key in ["model", "max_tokens", "api_version"]):
                base_config = provider_config.copy()
            else:
                # For partial override, preserve defaults and update with provided values
                base_config.update(provider_config)
        
        self.config = AgentConfig(
            name=name,
            description=description,
            instructions=instructions,
            tools_folder=tools_folder,
            llm_provider=self.llm_provider,
            provider_config=base_config,
            temperature=temperature,
            max_prompt_tokens=max_prompt_tokens
        )
        
        self._validate_environment()
        self._initialize_llm()
        self.tools = self._load_tools()
        self.thread_manager = ThreadManager()
        
    def _determine_provider(self) -> str:
        """Determine the best LLM provider based on the agent's role."""
        # Default to Claude for most tasks
        return "claude"
        
    def _determine_provider_from_description(self, description: str) -> str:
        """Automatically determine the best LLM provider based on agent description."""
        description_lower = description.lower()
        
        # Special case for statistical analysis
        if "statistical analysis" in description_lower:
            return "gemini"
        
        # First try exact task matching
        for task, provider in self.TASK_PREFERENCES.items():
            task_name = task.replace("_", " ")
            if task_name in description_lower:
                return provider
        
        # If no exact match, try category matching using keywords
        for category, keywords in self.TASK_KEYWORDS.items():
            if any(keyword in description_lower for keyword in keywords):
                return self.CATEGORY_PREFERENCES[category]
        
        # Default to Claude for complex/unknown tasks
        return "claude"
        
    def _get_provider_config(self, config: Optional[Dict[str, Any]] = None, description: Optional[str] = None) -> Dict[str, Any]:
        """Get provider configuration, using defaults if not specified."""
        # If config is provided, use it directly without modification
        if config is not None:
            return config.copy()
            
        # Get the default config first
        if self.llm_provider == "claude":
            provider_config = self.CLAUDE_CONFIG["default"].copy()
        else:  # gemini
            provider_config = self.GEMINI_CONFIG["default"].copy()
            
        # Determine the task category from description
        description_lower = description.lower() if description else ""
        task_category = "default"
        
        # First try to match exact tasks
        for task, provider in self.TASK_PREFERENCES.items():
            task_name = task.replace("_", " ")
            if task_name in description_lower and provider == self.llm_provider:
                # Find the category this task belongs to
                for category, tasks in self.TASK_CATEGORIES.items():
                    if task in tasks:
                        task_category = category
                        break
                break
        
        # If no exact task match, try category matching
        if task_category == "default":
            for category, keywords in self.TASK_KEYWORDS.items():
                if any(keyword in description_lower for keyword in keywords):
                    if self.CATEGORY_PREFERENCES[category] == self.llm_provider:
                        task_category = category
                        break
        
        # Update with task-specific config if available
        if task_category != "default":
            if self.llm_provider == "claude":
                task_config = self.CLAUDE_CONFIG.get(task_category)
            else:  # gemini
                task_config = self.GEMINI_CONFIG.get(task_category)
                
            if task_config:
                provider_config.update(task_config)
            
        return provider_config
        
    def _load_tools(self) -> Dict[str, BaseTool]:
        """Load all tools from the tools directory."""
        tools = {}
        if not os.path.exists(self.config.tools_folder):
            return tools
            
        for file in os.listdir(self.config.tools_folder):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                module_path = os.path.join(self.config.tools_folder, file)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and issubclass(obj, BaseTool) 
                            and obj != BaseTool):
                            tool = obj()
                            tools[tool.name or name.lower()] = tool
        return tools
        
    def _validate_environment(self) -> None:
        """Validate that all required environment variables are set."""
        # First validate the provider
        valid_providers = ["claude", "gemini", "mock"]
        if self.llm_provider not in valid_providers:
            raise ValueError(f"Invalid LLM provider: {self.llm_provider}. Must be one of {valid_providers}")
            
        required_vars = {
            "claude": ["ANTHROPIC_API_KEY"],
            "gemini": ["GOOGLE_API_KEY"],
            "mock": []  # Mock provider doesn't need any environment variables
        }
        
        missing = []
        for var in required_vars[self.llm_provider]:
            if not os.getenv(var):
                missing.append(var)
                
        if missing:
            raise ValueError(
                f"Missing required environment variables for {self.llm_provider}: "
                f"{', '.join(missing)}"
            )
            
    def _process_with_llm(self, thread: Thread) -> str:
        """Process a thread with the LLM provider."""
        # Get the last few messages from the thread
        messages = thread.get_recent_messages(self.config.max_prompt_tokens)
        
        # Format messages for the provider
        if self.llm_provider == "claude":
            formatted_messages = [
                {
                    "role": msg.role,
                    "content": msg.content
                }
                for msg in messages
            ]
            
            response = self.client.messages.create(
                model=self.config.provider_config["model"],
                max_tokens=self.config.provider_config.get("max_tokens", 4096),
                messages=formatted_messages,
                system=self.instructions
            )
            return response.content[0].text
            
        elif self.llm_provider == "gemini":
            # For Gemini, include instructions in the system message
            formatted_messages = [
                {
                    "role": "system",
                    "content": self.instructions
                }
            ]
            formatted_messages.extend([
                {
                    "role": msg.role,
                    "content": msg.content
                }
                for msg in messages
            ])
            
            response = self.client.chat.completions.create(
                model=self.config.provider_config["model"],
                messages=formatted_messages
            )
            return response.choices[0].message.content
            
        elif self.llm_provider == "mock":
            return self.client.create().content[0].text
            
        else:
            raise ValueError(f"Unsupported LLM provider: {self.llm_provider}")

    def _initialize_llm(self) -> None:
        """Initialize the LLM client based on the provider."""
        if self.llm_provider == "claude":
            from anthropic import Anthropic
            self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        elif self.llm_provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            self.client = genai.GenerativeModel(
                model_name=self.config.provider_config["model"]
            )
        elif self.llm_provider == "mock":
            self.client = MockClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {self.llm_provider}") 