import pytest
from app.agents.nodes.parser import parser_node

def test_parser_valid():
	state = {"price": 1000000, "expected_rent": 10000, "location": "Nairobi"}
	result = parser_node(state)
	assert "property" in result
	assert result["property"]["price"] == 1000000
	assert result["property"]["expected_rent"] == 10000
	assert result["property"]["location"] == "Nairobi"

def test_parser_missing():
	state = {"price": 1000000, "expected_rent": 10000}
	with pytest.raises(ValueError):
		parser_node(state)
