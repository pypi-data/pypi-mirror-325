import pytest
import threading
import time
from pankaj_core.utils.log_monitor import tail_log

@pytest.fixture
def log_file(tmp_path):
    """Create a temporary log file for testing."""
    file = tmp_path / "test.log"
    with open(file, "w") as f:
        f.write("Initial log\n")
    return file

def test_tail_log(log_file):
    """Test log monitoring by appending new lines."""
    def write_to_log():
        time.sleep(2)
        with open(log_file, "a") as f:
            f.write("New log entry\n")

    writer_thread = threading.Thread(target=write_to_log)
    writer_thread.start()

    tail_log(str(log_file))  # Should print new log lines

