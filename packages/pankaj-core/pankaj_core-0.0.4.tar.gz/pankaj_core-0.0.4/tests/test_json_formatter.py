import pytest
import json
from pankaj_core.utils.json_formatter import format_json

@pytest.fixture
def valid_json(tmp_path):
    """Create a temporary valid JSON file."""
    file = tmp_path / "valid.json"
    file.write_text(json.dumps({"name": "Pankaj", "age": 30}))
    return file

@pytest.fixture
def invalid_json(tmp_path):
    """Create a temporary invalid JSON file."""
    file = tmp_path / "invalid.json"
    file.write_text("{name: Pankaj, age: 30}")  # Invalid JSON
    return file

def test_format_json_valid(valid_json, capsys):
    """Test formatting of valid JSON."""
    format_json(str(valid_json))
    captured = capsys.readouterr()
    assert '"name": "Pankaj"' in captured.out

def test_format_json_invalid(invalid_json, capsys):
    """Test handling of invalid JSON."""
    format_json(str(invalid_json))
    captured = capsys.readouterr()
    assert "Invalid JSON" in captured.out

