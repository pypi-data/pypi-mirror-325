import pytest
import os
from pankaj_core.utils.backup import backup_directory

@pytest.fixture
def test_dir(tmp_path):
    """Create a temporary directory with files for backup."""
    dir_path = tmp_path / "test_data"
    dir_path.mkdir()
    (dir_path / "file1.txt").write_text("Hello, world!")
    return dir_path

def test_backup_directory(test_dir, tmp_path):
    """Test if backup is created successfully."""
    backup_dir = tmp_path / "backup"
    backup_directory(str(test_dir), str(backup_dir))
    
    backups = list(backup_dir.glob("*.zip"))
    assert len(backups) == 1  # Ensure a backup zip was created

