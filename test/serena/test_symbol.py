import unittest
from unittest.mock import MagicMock, patch

from serena.symbol import Symbol


class TestSymbol(unittest.TestCase):
    def test_to_dict_includes_end_location(self):
        """Test that to_dict includes end location information when location=True."""
        # Create a mock symbol with the required structure
        mock_symbol_info = {
            "name": "TestSymbol",
            "kind": 5,  # Class
            "location": {
                "relativePath": "test/file.py",
                "range": {
                    "start": {"line": 10, "character": 0},
                    "end": {"line": 20, "character": 3}
                }
            },
            "selectionRange": {
                "start": {"line": 10, "character": 6},
                "end": {"line": 10, "character": 16}
            },
            "children": []
        }
        
        symbol = Symbol(mock_symbol_info)
        
        # Call to_dict with location=True
        result = symbol.to_dict(kind=True, location=True)
        
        # Verify the dictionary contains both start and end locations
        self.assertTrue("location" in result, "Dictionary should include location")
        self.assertTrue("end_location" in result, "Dictionary should include end_location")
        
        # Verify values
        self.assertEqual(result["location"]["line"], 10)
        self.assertEqual(result["location"]["column"], 6)
        self.assertEqual(result["end_location"]["line"], 20)
        self.assertEqual(result["end_location"]["column"], 3)


if __name__ == "__main__":
    unittest.main()
