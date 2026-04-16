import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("p", "text", [], None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_attr(self):
        node = HTMLNode("a", "click", [], {"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_multiple_attrs(self):
        node = HTMLNode("a", "click", [], {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Prologue")
        self.assertEqual(node.to_html(), "<h1>Prologue</h1>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click me", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">click me</a>')

if __name__ == "__main__":
    unittest.main()
