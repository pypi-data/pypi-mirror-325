import pytest
from pathlib import Path
import json
import os
from typing import List, Tuple

from multi_swarm import Agency, Agent, BaseAgent
from multi_swarm.tools import BaseTool
from multi_swarm.core.thread import Thread

class MockTool(BaseTool):
    """A mock tool for testing."""
    def run(self):
        return {"status": "success"}

class TestAgent(Agent):
    """A test agent implementation."""
    def __init__(self, name: str):
        current_dir = Path(__file__).parent
        instructions_file = current_dir / "test_instructions.md"
        
        # Create tools directory if it doesn't exist
        tools_dir = current_dir / "tools"
        tools_dir.mkdir(exist_ok=True)
        
        super().__init__(
            name=name,
            description=f"Test agent {name}",
            instructions=str(instructions_file),
            tools_folder=str(tools_dir),
            llm_provider="mock",
            provider_config={"model": "mock"}
        )
        
    def _process_with_llm(self, thread: Thread) -> str:
        """Mock LLM processing for testing."""
        if self.config.llm_provider not in ["mock", "claude", "gemini"]:
            raise ValueError(f"Invalid provider: {self.config.llm_provider}")
        
        # Add a message to the thread
        thread.add_message({
            "role": "assistant",
            "content": "Mock response",
            "agent_name": self.config.name
        })
        
        return json.dumps({
            "response": "Mock response",
            "agent": self.config.name,
            "thread_id": thread.id
        })

def create_test_agency() -> Tuple[Agency, List[Agent]]:
    """Create a test agency with multiple agents."""
    agent1 = TestAgent("Agent1")
    agent2 = TestAgent("Agent2")
    agent3 = TestAgent("Agent3")
    
    flows = [
        (agent1, agent2),
        (agent2, agent3),
        (agent1, agent3)
    ]
    
    agency = Agency(
        name="Agent1",
        description="Test agency for integration testing",
        agents=[agent1, agent2, agent3],
        flows=flows
    )
    
    return agency, [agent1, agent2, agent3]

def test_full_agency_workflow():
    """Test the complete workflow of an agency."""
    agency, agents = create_test_agency()
    
    # Test initialization
    assert len(agency.agents) == 3
    assert len(agency.flows) == 3
    
    # Test communication flows
    assert agency.can_communicate("Agent1", "Agent2")
    assert agency.can_communicate("Agent2", "Agent3")
    assert agency.can_communicate("Agent1", "Agent3")
    assert not agency.can_communicate("Agent3", "Agent1")  # Reverse flow not allowed
    
    # Test message processing
    response = agency.run("Test message")
    assert response is not None
    assert isinstance(response, (dict, str))
    
    # Test thread management
    first_flow = next(iter(agency.flows.values()))
    thread = agency.thread_manager.get_thread(first_flow.thread_id)
    assert thread is not None
    assert len(thread.messages) > 0

def test_agent_initialization():
    """Test that agents are initialized correctly with all components."""
    agent = TestAgent("TestAgent")
    
    # Test basic properties
    assert agent.config.name == "TestAgent"
    assert agent.config.llm_provider == "mock"
    
    # Test tool loading
    assert hasattr(agent, "tools")
    assert isinstance(agent.tools, dict)
    
    # Test LLM client initialization
    assert hasattr(agent, "client")
    
    # Test thread management
    thread = agent.thread_manager.create_thread()
    assert thread is not None
    assert thread.id in agent.thread_manager.threads

def test_error_handling():
    """Test error handling across the entire system."""
    agency, agents = create_test_agency()
    
    # Test invalid flow
    with pytest.raises(ValueError):
        agency.send_message("NonexistentAgent", "Agent1", "Test message")
    
    # Test invalid provider
    with pytest.raises(ValueError):
        invalid_agent = TestAgent("InvalidAgent")
        invalid_agent.config.llm_provider = "invalid_provider"
        invalid_agent._process_with_llm(Thread())

def test_state_persistence():
    """Test that agency state can be saved and loaded."""
    agency, agents = create_test_agency()
    
    # Create some state
    agency.run("Test message 1")
    agency.run("Test message 2")
    
    # Save state
    agency.save_state()
    
    # Create new agency and load state
    new_agency, _ = create_test_agency()
    new_agency.load_state()
    
    # Verify state was restored
    for (source, target), flow in agency.flows.items():
        new_flow = new_agency.get_flow(source, target)
        assert new_flow is not None
        assert new_flow.thread_id == flow.thread_id

def test_concurrent_operations():
    """Test that the agency can handle concurrent operations."""
    import threading
    import queue
    
    agency, agents = create_test_agency()
    results = queue.Queue()
    
    def worker(message):
        try:
            response = agency.run(message)
            results.put(("success", response))
        except Exception as e:
            results.put(("error", str(e)))
    
    # Start multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(f"Test message {i}",))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Check results
    while not results.empty():
        status, result = results.get()
        assert status == "success"
        assert isinstance(result, (dict, str))

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 