import os
import time
from pathlib import Path

import pytest

from ezpy_logs.LoggerFactory import LoggerFactory, BASE_LOG_DIR


@pytest.fixture
def log_dir(tmp_path):
    """Create a temporary directory for logs"""
    return str(tmp_path / BASE_LOG_DIR)


@pytest.fixture
def cleanup():
    """Cleanup fixture to reset LoggerFactory state between tests"""
    yield
    LoggerFactory.is_setup = False
    LoggerFactory.output_files = []
    LoggerFactory.replaced = []
    LoggerFactory.setup_loggers = []


def test_import():
    """Test that we can import the library"""
    from ezpy_logs.LoggerFactory import LoggerFactory
    assert LoggerFactory is not None


def test_basic_logging(log_dir, cleanup):
    """Test that we can log something and it's saved to a file"""
    LoggerFactory.setup_LoggerFactory(log_dir=log_dir)
    logger = LoggerFactory.getLogger(__name__)

    test_message = "Test log message"
    logger.info(test_message)

    # Check Latest.log exists and contains our message
    latest_log = Path(log_dir) / "Latest.log"
    assert latest_log.exists()
    assert test_message in latest_log.read_text()


def test_error_logging(log_dir, cleanup):
    """Test that errors are logged to both normal and error files"""
    LoggerFactory.setup_LoggerFactory(log_dir=log_dir)
    logger = LoggerFactory.getLogger(__name__)
    
    error_message = "Test error message"
    logger.error(error_message)
    
    # Check both Latest.log and Latest_ERRORS.log
    latest_log = Path(log_dir) / "Latest.log"
    error_log = Path(log_dir) / "Latest_ERRORS.log"
    
    assert latest_log.exists()
    assert error_log.exists()
    
    latest_content = latest_log.read_text()
    error_content = error_log.read_text()
    
    assert error_message in latest_content
    assert error_message in error_content


def test_old_logs_deletion(log_dir, cleanup, monkeypatch):
    """Test that old log files are deleted"""
    # Create some old log files
    old_archive_dir = Path(log_dir) / "archive"
    old_archive_dir.mkdir(parents=True)
    old_file = old_archive_dir / "old_log.log"
    old_file.write_text("old content")
    
    # Set file's modification time to 31 days ago
    old_time = time.time() - (31 * 24 * 60 * 60)
    os.utime(old_file, (old_time, old_time))
    
    # Create a new log file
    new_file = old_archive_dir / "new_log.log"
    new_file.write_text("new content")
    
    # Setup logger which should trigger old log deletion
    LoggerFactory.setup_LoggerFactory(log_dir=log_dir, clean_old_logs=True)
    logger = LoggerFactory.getLogger(__name__)
    
    # Old file should be gone, new file should remain
    assert not old_file.exists()
    assert new_file.exists() 
