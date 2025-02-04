"""
Communication flow between agents.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
import uuid

class CommunicationFlow(BaseModel):
    """A communication flow between two agents."""
    source: str = Field(..., description="Source agent name")
    target: str = Field(..., description="Target agent name")
    thread_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="ID of the thread for this flow")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the flow")
    status: str = Field(default="active", description="Status of the flow (active, paused, closed)")
    
    class Config:
        """Pydantic model configuration."""
        arbitrary_types_allowed = True 