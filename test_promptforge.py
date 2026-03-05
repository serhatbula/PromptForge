# test_promptforge.py
"""
Tests for PromptForge module.
"""

import unittest
from promptforge import PromptForge

class TestPromptForge(unittest.TestCase):
    """Test cases for PromptForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PromptForge()
        self.assertIsInstance(instance, PromptForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PromptForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
