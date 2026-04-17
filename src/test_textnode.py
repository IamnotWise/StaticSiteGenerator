import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)

        node3 = TextNode("This is a text node", TextType.code_text)
        node4 = TextNode("This is a text node", TextType.italic_text,None)
        
        self.assertEqual(node, node2)
        self.assertNotEqual(node3,node4)

    def test_text(self):
        node = TextNode("This is a text node", TextType.plain_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is bold text", TextType.bold_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")
    def test_link(self):
        node = TextNode("Google", TextType.links, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "https://google.com"})
if __name__ == "__main__":
    unittest.main()