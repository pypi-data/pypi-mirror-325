import os
import asyncio
from typing import List, Tuple, Optional, Dict, Union, Any
from pathlib import Path
import json
from datetime import datetime
from pydantic import BaseModel, Field

from multi_swarm.core.base_agent import BaseAgent
from .thread import Thread, ThreadManager, Message
from .file import FileManager
from .interpreter import CodeInterpreter
from .rag import RAGSystem
from .flow import CommunicationFlow

class AgencyConfig(BaseModel):
    """
    Configuration for an agency.
    
    Attributes:
        name: Name of the agency
        description: Description of the agency's purpose
        storage_path: Path for persistent storage
        shared_instructions: Path to shared instructions file
        default_temperature: Default temperature for agents
        default_max_tokens: Default max tokens for agents
        use_code_interpreter: Whether to enable code interpreter
        use_rag: Whether to enable RAG capabilities
        use_file_storage: Whether to enable file storage
    """
    name: str
    description: str
    storage_path: Optional[str] = None
    shared_instructions: Optional[str] = None
    default_temperature: float = 0.7
    default_max_tokens: int = 4096
    use_code_interpreter: bool = False
    use_rag: bool = False
    use_file_storage: bool = False

class Agency:
    """
    Represents a collection of agents working together.
    
    This class manages:
    - Agent initialization and configuration
    - Inter-agent communication
    - Shared resources (files, knowledge base)
    - Task distribution and coordination
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        agents: List[BaseAgent],
        flows: List[Tuple[BaseAgent, BaseAgent]],
        storage_path: Optional[str] = None,
        shared_instructions: Optional[str] = None,
        use_code_interpreter: bool = False,
        use_rag: bool = False,
        use_file_storage: bool = False
    ):
        """
        Initialize the agency.
        
        Args:
            name: Name of the agency
            description: Description of the agency's purpose
            agents: List of agents in the agency
            flows: List of tuples defining communication flows (source, target)
            storage_path: Path for persistent storage
            shared_instructions: Path to shared instructions file
            use_code_interpreter: Whether to enable code interpreter
            use_rag: Whether to enable RAG capabilities
            use_file_storage: Whether to enable file storage
        """
        self.config = AgencyConfig(
            name=name,
            description=description,
            storage_path=storage_path,
            shared_instructions=shared_instructions,
            use_code_interpreter=use_code_interpreter,
            use_rag=use_rag,
            use_file_storage=use_file_storage
        )
        
        # Initialize storage
        if storage_path:
            self.storage_path = Path(storage_path)
            self.storage_path.mkdir(parents=True, exist_ok=True)
        else:
            self.storage_path = None
        
        # Initialize components
        self._init_components()
        
        # Load shared instructions
        self.shared_instructions = self._load_shared_instructions()
        
        # Initialize agents
        self.agents = {agent.config.name: agent for agent in agents}
        
        # Set up communication flows
        self.flows = {}
        for source, target in flows:
            if source.config.name not in self.agents or target.config.name not in self.agents:
                raise ValueError(f"Invalid flow: {source.config.name} -> {target.config.name}")
            
            # Create a thread for this flow
            thread = self.thread_manager.create_thread()
            
            flow = CommunicationFlow(
                source=source.config.name,
                target=target.config.name,
                thread_id=thread.id
            )
            self.flows[(source.config.name, target.config.name)] = flow
    
    def _init_components(self):
        """Initialize agency components."""
        # Initialize thread manager
        self.thread_manager = ThreadManager()
        
        # Initialize file manager if enabled
        self.file_manager = None
        if self.config.use_file_storage:
            file_storage = self.storage_path / "files" if self.storage_path else None
            self.file_manager = FileManager(storage_path=file_storage)
        
        # Initialize code interpreter if enabled
        self.code_interpreter = None
        if self.config.use_code_interpreter:
            interpreter_workspace = self.storage_path / "workspace" if self.storage_path else None
            self.code_interpreter = CodeInterpreter(workspace_dir=interpreter_workspace)
        
        # Initialize RAG system if enabled
        self.rag_system = None
        if self.config.use_rag:
            rag_storage = self.storage_path / "rag" if self.storage_path else None
            self.rag_system = RAGSystem(storage_path=rag_storage)
    
    def _load_shared_instructions(self) -> str:
        """Load shared instructions from file."""
        if not self.config.shared_instructions:
            return ""
            
        if os.path.isfile(self.config.shared_instructions):
            with open(self.config.shared_instructions, 'r') as f:
                return f.read()
        
        return self.config.shared_instructions
    
    def get_agent(self, name: str) -> Optional[BaseAgent]:
        """Get an agent by name."""
        return self.agents.get(name)
    
    def list_agents(self) -> List[str]:
        """List all agents in the agency."""
        return list(self.agents.keys())
    
    def can_communicate(self, source: str, target: str) -> bool:
        """Check if two agents can communicate."""
        return (source, target) in self.flows
    
    def get_flow(self, source: str, target: str) -> Optional[CommunicationFlow]:
        """Get communication flow between two agents."""
        return self.flows.get((source, target))
    
    def send_message(
        self,
        source: str,
        target: str,
        content: str,
        metadata: Dict = None
    ) -> Message:
        """
        Send a message from one agent to another.
        
        Args:
            source: Name of the source agent
            target: Name of the target agent
            content: Message content
            metadata: Additional metadata
            
        Returns:
            The created Message instance
        """
        # Validate communication flow
        if not self.can_communicate(source, target):
            raise ValueError(f"No communication flow from {source} to {target}")
        
        # Get the flow and thread
        flow = self.get_flow(source, target)
        thread = self.thread_manager.get_thread(flow.thread_id)
        
        # Add message to thread
        message = thread.add_message(
            role="user",
            content=content,
            agent_name=source,
            metadata=metadata
        )
        
        # Process message with target agent
        target_agent = self.get_agent(target)
        response = target_agent._process_with_llm(thread)
        
        # Add response to thread
        thread.add_message(
            role="assistant",
            content=response,
            agent_name=target
        )
        
        return message
    
    def broadcast_message(
        self,
        source: str,
        content: str,
        metadata: Dict = None
    ) -> List[Message]:
        """
        Broadcast a message to all connected agents.
        
        Args:
            source: Name of the source agent
            content: Message content
            metadata: Additional metadata
            
        Returns:
            List of created Message instances
        """
        messages = []
        for flow in self.flows.values():
            if flow.source == source:
                message = self.send_message(
                    source=source,
                    target=flow.target,
                    content=content,
                    metadata=metadata
                )
                messages.append(message)
        return messages
    
    def upload_file(
        self,
        file: Any,
        filename: str,
        purpose: str = "attachment",
        metadata: Dict = None
    ):
        """Upload a file to shared storage."""
        if not self.file_manager:
            raise RuntimeError("File storage not enabled for this agency")
        return self.file_manager.upload_file(file, filename, purpose, metadata)
    
    def execute_code(
        self,
        code: str,
        language: str = "python",
        additional_files: Dict[str, str] = None,
        environment: Dict[str, str] = None
    ):
        """Execute code in the shared secure environment."""
        if not self.code_interpreter:
            raise RuntimeError("Code interpreter not enabled for this agency")
        return self.code_interpreter.execute(code, language, additional_files, environment)
    
    def search_knowledge(
        self,
        query: str,
        k: int = 5,
        threshold: float = None
    ):
        """Search the shared knowledge base using RAG."""
        if not self.rag_system:
            raise RuntimeError("RAG not enabled for this agency")
        return self.rag_system.search(query, k, threshold)
    
    def add_to_knowledge(
        self,
        content: str,
        metadata: Dict = None
    ):
        """Add content to the shared knowledge base."""
        if not self.rag_system:
            raise RuntimeError("RAG not enabled for this agency")
        return self.rag_system.add_document(content, metadata)
    
    def save_state(self, path: Optional[str] = None) -> None:
        """Save the agency state to a file."""
        state = {
            "flows": {
                f"{source}-{target}": {
                    "source": source,
                    "target": target,
                    "thread_id": flow.thread_id,
                    "status": flow.status
                }
                for (source, target), flow in self.flows.items()
            },
            "threads": {
                thread.id: {
                    "messages": [
                        {
                            "content": msg.content,
                            "role": msg.role,
                            "agent_name": msg.agent_name,
                            "metadata": msg.metadata,
                            "created_at": msg.created_at.isoformat()
                        }
                        for msg in thread.messages
                    ],
                    "metadata": thread.metadata,
                    "created_at": thread.created_at.isoformat(),
                    "last_active_at": thread.last_active_at.isoformat(),
                    "status": thread.status
                }
                for thread in self.thread_manager.threads.values()
            }
        }
        
        path = path or "agency_state.json"
        with open(path, "w") as f:
            json.dump(state, f, indent=2)
            
    def load_state(self, path: Optional[str] = None) -> None:
        """Load the agency state from a file."""
        path = path or "agency_state.json"
        if not os.path.exists(path):
            return
            
        with open(path, "r") as f:
            state = json.load(f)
            
        # First restore threads
        for thread_id, thread_data in state["threads"].items():
            thread = Thread(
                id=thread_id,
                messages=[
                    Message(
                        content=msg["content"],
                        role=msg["role"],
                        agent_name=msg["agent_name"],
                        metadata=msg["metadata"],
                        created_at=datetime.fromisoformat(msg["created_at"])
                    )
                    for msg in thread_data["messages"]
                ],
                metadata=thread_data["metadata"],
                created_at=datetime.fromisoformat(thread_data["created_at"]),
                last_active_at=datetime.fromisoformat(thread_data["last_active_at"]),
                status=thread_data["status"]
            )
            self.thread_manager.threads[thread_id] = thread
            
        # Then restore flows
        for flow_data in state["flows"].values():
            source = flow_data["source"]
            target = flow_data["target"]
            thread_id = flow_data["thread_id"]
            status = flow_data["status"]
            
            flow = CommunicationFlow(
                source=source,
                target=target,
                thread_id=thread_id,
                status=status
            )
            self.flows[(source, target)] = flow
    
    def run_demo(self):
        """Print welcome message and instructions for the demo."""
        entry_agent = self.get_agent(self.config.name)
        print(f"\nWelcome to the {entry_agent.config.name} Agency Demo!")
        print("\nType 'exit' to end the conversation.")
        print("\nEnter your message:")
        self.demo_loop()
    
    def demo_loop(self):
        """Run the interactive demo loop."""
        try:
            while True:
                user_input = input("> ")
                if user_input.lower() == 'exit':
                    print("\nThank you for using the agency. Goodbye!")
                    break
                
                response = self.process_message(user_input)
                entry_agent = self.get_agent(self.config.name)
                print(f"\n{entry_agent.config.name}: {response}")
        
        except KeyboardInterrupt:
            print("\n\nDemo terminated by user. Goodbye!")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
    
    def process_message(self, message: str) -> str:
        """Process a message through the agency."""
        entry_agent = self.get_agent(self.config.name)
        if not entry_agent:
            return None
        
        # Create a thread for this message
        thread = self.thread_manager.create_thread()
        thread.add_message({
            "role": "user",
            "content": message,
            "agent_name": "user"
        })
        
        # Process with the entry agent
        response = entry_agent._process_with_llm(thread)
        return response 
    
    def run(self, prompt: str) -> str:
        """
        Process a prompt through the agency's workflow.
        
        Args:
            prompt: The input prompt to process
            
        Returns:
            The final response from the agency
        """
        if not prompt:
            return {"error": "Empty prompt provided"}
            
        try:
            # Get the entry point agent (first agent in the list)
            entry_agent = list(self.agents.values())[0]
            
            # Get the first flow's thread
            first_flow = next(iter(self.flows.values()))
            thread = self.thread_manager.get_thread(first_flow.thread_id)
            
            # Add the initial prompt to the thread
            thread.add_message(
                role="user",
                content=prompt,
                agent_name="user"
            )
            
            # Process with entry agent
            response = entry_agent._process_with_llm(thread)
            thread.add_message(
                role="assistant",
                content=response,
                agent_name=entry_agent.config.name
            )
            
            # Process through connected agents based on the response
            for source, target in self.flows.keys():
                if source == entry_agent.config.name:
                    target_agent = self.agents[target]
                    target_response = target_agent._process_with_llm(thread)
                    thread.add_message(
                        role="assistant",
                        content=target_response,
                        agent_name=target
                    )
            
            # Return the combined response
            return self._combine_responses(thread)
            
        except Exception as e:
            return {"error": f"Error processing prompt: {str(e)}"}
    
    def _combine_responses(self, thread: Thread) -> Dict:
        """Combine responses from all agents into a final response."""
        combined = {}
        
        for message in thread.messages:
            if message.role == "assistant":
                try:
                    # Try to parse as JSON
                    response_data = json.loads(message.content)
                    combined.update(response_data)
                except:
                    # If not JSON, add as string
                    combined[f"{message.metadata['agent_name']}_response"] = message.content
        
        return combined 