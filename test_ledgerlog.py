# test_ledgerlog.py
"""
Tests for LedgerLog module.
"""

import unittest
from ledgerlog import LedgerLog

class TestLedgerLog(unittest.TestCase):
    """Test cases for LedgerLog class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerLog()
        self.assertIsInstance(instance, LedgerLog)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerLog()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
