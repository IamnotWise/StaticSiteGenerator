import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)

        node3 = TextNode("This is a text node", TextType.code_text)
        node4 = TextNode("This is a text node", TextType.italic_text,None)
        
        self.assertEqual(node, node2)
        self.assertNotEqual(node3,node4)


if __name__ == "__main__":
    unittest.main()