import pytest
import app.agents.graph as graph_mod

@pytest.mark.asyncio
async def test_pipeline_happy_path(monkeypatch):
    # Patch LLM nodes to return deterministic outputs
    monkeypatch.setattr("app.agents.nodes.risk.risk_node", lambda state: {"risk": {"risks": ["None"], "risk_score": 2}})
    monkeypatch.setattr("app.agents.nodes.decision.decision_node", lambda state: {"decision": {"verdict": "Good Investment", "score": 8, "confidence": 0.9}})
    monkeypatch.setattr("app.agents.nodes.explanation.explanation_node", lambda state: {"explanation": "This is a good investment based on ROI and low risk."})
    # Rebuild the graph so it picks up the monkeypatched nodes
    graph_mod.property_graph = graph_mod.build_graph()
    state = {
        "price": 1000000,
        "expected_rent": 10000,
        "location": "Nairobi"
    }
    result = await graph_mod.run_pipeline(state)
    assert "metrics" in result
    assert "decision" in result
    assert "explanation" in result

@pytest.mark.asyncio
async def test_pipeline_missing_data():
    state = {"price": 1000000, "expected_rent": 10000}
    with pytest.raises(Exception):
        await graph_mod.run_pipeline(state)
