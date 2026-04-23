

import logging
import time
import asyncio

from langgraph.graph import StateGraph, END

from app.agents.state import AgentState
from app.agents.nodes.parser import parser_node
from app.agents.nodes.financial import financial_node
from app.agents.nodes.market import market_node
from app.agents.nodes.risk import risk_node
from app.agents.nodes.decision import decision_node
from app.agents.nodes.explanation import explanation_node

logger = logging.getLogger(__name__)

def async_timing_wrapper(name, node):
	async def wrapped(state):
		start = time.time()
		logger.info(f"[Graph] Starting node: {name}")
		if asyncio.iscoroutinefunction(node):
			result = await node(state)
		else:
			result = node(state)
		elapsed = time.time() - start
		logger.info(f"[Graph] Finished node: {name} ({elapsed:.2f}s)")
		return result
	return wrapped

def build_graph():
	builder = StateGraph(AgentState)


	builder.add_node("parser", async_timing_wrapper("parser", parser_node))
	builder.add_node("financial", async_timing_wrapper("financial", financial_node))
	builder.add_node("market_node", async_timing_wrapper("market_node", market_node))
	builder.add_node("risk_node", async_timing_wrapper("risk_node", risk_node))
	builder.add_node("decision_node", async_timing_wrapper("decision_node", decision_node))
	builder.add_node("explanation_node", async_timing_wrapper("explanation_node", explanation_node))

	builder.set_entry_point("parser")

	builder.add_edge("parser", "financial")
	builder.add_edge("financial", "market_node")
	builder.add_edge("market_node", "risk_node")
	builder.add_edge("risk_node", "decision_node")
	builder.add_edge("decision_node", "explanation_node")
	builder.add_edge("explanation_node", END)

	return builder.compile()


property_graph = build_graph()

async def run_pipeline(initial_state: AgentState) -> AgentState:
    """
    Executes LangGraph pipeline and returns final merged state.
    """

    logger.info("[Pipeline] Starting property analysis pipeline")

    final_state: Dict[str, Any] = dict(initial_state)

    async for event in property_graph.astream(initial_state):
        logger.info(f"[Pipeline] Event: {event}")

        if isinstance(event, dict):
            for _, update in event.items():
                if isinstance(update, dict):
                    final_state.update(update)

    logger.info("[Pipeline] Pipeline completed successfully")

    return final_state
