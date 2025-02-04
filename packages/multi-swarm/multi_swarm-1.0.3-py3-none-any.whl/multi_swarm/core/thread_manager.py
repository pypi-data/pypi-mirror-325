"""
Thread management for agent communication.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, UTC
from pydantic import BaseModel, Field
import uuid

class Message(BaseModel):
    """A message in a thread."""
    content: str = Field(..., description="Content of the message")
    role: str = Field(..., description="Role of the sender (user, assistant, system)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the message")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC), description="When the message was created")

class Thread(BaseModel):
    """A thread of messages between agents."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the thread")
    messages: List[Message] = Field(default_factory=list, description="Messages in the thread")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the thread")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC), description="When the thread was created")
    last_active_at: datetime = Field(default_factory=lambda: datetime.now(UTC), description="When the thread was last active")
    status: str = Field(default="active", description="Status of the thread (active, archived)")
    
    def add_message(self, content: str, role: str = "user", metadata: Optional[Dict[str, Any]] = None) -> None:
        """Add a message to the thread."""
        message = Message(
            content=content,
            role=role,
            metadata=metadata or {},
            created_at=datetime.now(UTC)
        )
        self.messages.append(message)
        self.last_active_at = datetime.now(UTC)
        
    def get_messages(self) -> List[Message]:
        """Get all messages in the thread."""
        return self.messages
        
    def get_recent_messages(self, limit: int = 10) -> List[Message]:
        """Get the most recent messages in the thread."""
        return self.messages[-limit:]
        
    def clear(self) -> None:
        """Clear all messages from the thread."""
        self.messages = []
        self.last_active_at = datetime.now(UTC)

class ThreadManager:
    """Manages threads for agent communication."""
    def __init__(self):
        """Initialize the thread manager."""
        self.threads: Dict[str, Thread] = {}
        
    def create_thread(self, metadata: Optional[Dict[str, Any]] = None) -> Thread:
        """Create a new thread."""
        thread = Thread(metadata=metadata or {})
        self.threads[thread.id] = thread
        return thread
        
    def get_thread(self, thread_id: str) -> Optional[Thread]:
        """Get a thread by ID."""
        return self.threads.get(thread_id)
        
    def delete_thread(self, thread_id: str) -> None:
        """Delete a thread."""
        if thread_id in self.threads:
            del self.threads[thread_id]
            
    def list_threads(self) -> List[Thread]:
        """List all threads."""
        return list(self.threads.values())
        
    def clear_all(self) -> None:
        """Clear all threads."""
        self.threads = {} 