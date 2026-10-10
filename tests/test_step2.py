from app.features.workflows.providers.tool_registry import discover_tools

def test_tools_have_schemas():
    assert all(t["input_schema"]["type"]=="object" for t in discover_tools())
def test_registry_is_not_mutable_by_caller():
    discover_tools()[0]["name"]="evil"
    assert discover_tools()[0]["name"]=="read_request"
