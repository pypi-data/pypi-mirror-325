import pytest
from pankaj_core.utils.system_monitor import system_monitor

def test_system_monitor(capsys):
    """Test that system monitor prints CPU and memory usage."""
    system_monitor()
    captured = capsys.readouterr()
    assert "CPU Usage" in captured.out

