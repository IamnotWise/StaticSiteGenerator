import unittest
from blocknode import BlockType, block_to_block_type

class TestBlockNode(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("## Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> line 1\n> line 2"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- one\n- two"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. one\n2. two"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("just text"), BlockType.PARAGRAPH)
    
if __name__ == "__main__":
    unittest.main()