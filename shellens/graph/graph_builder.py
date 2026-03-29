from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

from shellens.graph.state import ShellLensState

from shellens.graph.nodes import (
    profiler_node, planning_node, execution_node, response_node
)
from shellens.graph.router import router

def build_graph():
    # Persistence
    checkpointer = MemorySaver()
    
    graph=StateGraph(ShellLensState)

    # Consolidated Nodes for speed
    graph.add_node("profiler", profiler_node)
    graph.add_node("planning", planning_node)
    graph.add_node("execution", execution_node)
    graph.add_node("response", response_node)

    # Entry
    graph.set_entry_point("profiler")

    # Flow
    graph.add_edge("profiler", "planning")
    graph.add_edge("planning", "execution")

    # Optimized Loop
    graph.add_conditional_edges(
        "execution",
        router,
        {
            "execution": "execution",
            "response": "response"
        }
    )

    return graph.compile(checkpointer=checkpointer)
