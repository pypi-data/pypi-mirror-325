"""Web Research Graph.

This module defines a workflow for conducting web research and generating structured content.
"""

from web_research_graph.graph import graph
from web_research_graph.configuration import Configuration
from web_research_graph.state import State, InputState, OutputState

__all__ = [
    "graph",
    "Configuration",
    "State",
    "InputState", 
    "OutputState"
]