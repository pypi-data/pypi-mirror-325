"""
Multi-Swarm Tools Module

This module provides base classes and utilities for creating tools that agents can use.
"""

from pydantic import BaseModel, Field
from typing import Any, Dict, Optional

class BaseTool(BaseModel):
    """
    Base class for all tools in the Multi-Swarm framework.
    
    Tools are the primary way for agents to interact with external systems and perform actions.
    Each tool should inherit from this class and implement the run method.
    """
    
    name: str = Field(default="", description="Name of the tool")
    description: str = Field(default="", description="Description of what the tool does")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the tool")
    
    def run(self) -> Any:
        """
        Execute the tool's functionality.
        
        This method must be implemented by all tool classes.
        
        Returns:
            The result of the tool's operation
        """
        raise NotImplementedError("Tool must implement run method")
    
    def validate(self) -> bool:
        """
        Validate that the tool is properly configured.
        
        Returns:
            True if the tool is valid, False otherwise
        """
        return True
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get tool metadata.
        
        Returns:
            Dictionary containing tool metadata
        """
        return self.metadata
    
    def set_metadata(self, key: str, value: Any) -> None:
        """
        Set tool metadata.
        
        Args:
            key: Metadata key
            value: Metadata value
        """
        self.metadata[key] = value
    
    class Config:
        """Pydantic model configuration."""
        arbitrary_types_allowed = True 