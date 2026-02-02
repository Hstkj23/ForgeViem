# test_forgeviem.py
"""
Tests for ForgeViem module.
"""

import unittest
from forgeviem import ForgeViem

class TestForgeViem(unittest.TestCase):
    """Test cases for ForgeViem class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForgeViem()
        self.assertIsInstance(instance, ForgeViem)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForgeViem()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
