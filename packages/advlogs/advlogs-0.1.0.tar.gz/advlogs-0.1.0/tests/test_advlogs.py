import unittest
import sys
import os

# Ensure Python finds advlogs correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from advlogs import advlogs
from cryptography.fernet import Fernet
import os

class TestAdvLogs(unittest.TestCase):
    def setUp(self):
        """Setup before each test case."""
        self.key = Fernet.generate_key().decode()
        self.logger = advlogs(log_file="test_advlogs.log", encrypt=True, key=self.key)

    def test_log_creation(self):
        """Ensure log file is created."""
        self.logger.log("INFO", "Test log entry")
        self.assertTrue(os.path.exists("test_advlogs.log"))

    def test_compress_logs(self):
        """Ensure logs can be compressed."""
        compressed_file = self.logger.compress_logs(log_file="test_advlogs.log", compressed_file="test_advlogs.gz")
        self.assertTrue(os.path.exists(compressed_file))

    def test_multi_threaded_logging(self):
        """Ensure multi-threaded logging works."""
        messages = ["Threaded log 1", "Threaded log 2", "Threaded log 3"]
        self.logger.multi_threaded_logging(messages)
        self.assertTrue(os.path.exists("test_advlogs.log"))

if __name__ == "__main__":
    unittest.main()
