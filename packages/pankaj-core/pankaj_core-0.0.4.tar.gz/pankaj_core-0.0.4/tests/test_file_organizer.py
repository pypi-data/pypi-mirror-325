import pytest
import os
from pankaj_core.utils.file_organizer import organize_files

@pytest.fixture
def test_dir(tmp_path):
    """Create a test directory with mixed file types."""
    dir_path = tmp_path / "test_files"
    dir_path.mkdir()
    (dir_path / "doc1.txt").write_text("Text file")
    (dir_path / "image1.jpg").write_text("JPEG file")
    (dir_path / "script.py").write_text("Python script")
    return dir_path

def test_organize_files(test_dir):
    """Test if files are moved into corresponding directories."""
    organize_files(str(test_dir))
    
    assert (test_dir / "txt" / "doc1.txt").exists()
    assert (test_dir / "jpg" / "image1.jpg").exists()
    assert (test_dir / "py" / "script.py").exists()

