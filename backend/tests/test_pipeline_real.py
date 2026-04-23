import pytest
import app.agents.graph as graph_mod

@pytest.mark.asyncio
async def test_pipeline_real_llm():
    """
    End-to-end test with real LLM (no monkeypatching).
    Requires valid API keys and model access.
    """
    state = {
        "price": 1000000,
        "expected_rent": 10000,
        "location": "Nairobi"
    }
    result = await graph_mod.run_pipeline(state)
    print(result)
    assert "metrics" in result
    assert "decision" in result
    assert "explanation" in result
