"""
Multi-Swarm Framework

A framework for creating collaborative AI agent swarms.
"""

from multi_swarm.core.base_agent import BaseAgent
from multi_swarm.core.agent import Agent
from multi_swarm.core.agency import Agency

__version__ = "1.0.1"
__author__ = "Bart Van Spitaels"
__email__ = "bart.vanspitaels@gmail.com"

__all__ = [
    "Agency",
    "Agent",
    "BaseAgent"
] 