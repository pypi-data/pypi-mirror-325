"""
Configuration classes for Multi-Swarm components.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class AgentConfig(BaseModel):
    """Configuration for an agent."""
    name: str = Field(..., description="Name of the agent")
    description: str = Field(..., description="Description of what the agent does")
    instructions: str = Field(..., description="Path to the instructions file for the agent")
    tools_folder: str = Field(..., description="Path to the folder containing the agent's tools")
    llm_provider: str = Field(default="claude", description="LLM provider to use")
    provider_config: Dict[str, Any] = Field(default_factory=dict, description="Provider-specific configuration")
    temperature: float = Field(default=0.5, description="Temperature for LLM responses")
    max_prompt_tokens: int = Field(default=25000, description="Maximum number of tokens in the prompt")
    
    class Config:
        """Pydantic model configuration."""
        arbitrary_types_allowed = True 