import unittest

from delimiter import split_nodes_delimiter, split_nodes_images, split_nodes_link, text_to_text_nodes
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("This is a **bold** text", TextType.plain_text)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.bold_text)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, TextType.plain_text)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.bold_text)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.plain_text)
    def test_split_nodes_delimiter_code(self):
        old_nodes = [TextNode("This is a `code` text", TextType.plain_text)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.code_text)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, TextType.plain_text)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.code_text)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.plain_text)
    def test_split_nodes_delimiter_italic(self):
        old_nodes = [TextNode("This is an _italic_ text", TextType.plain_text)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.italic_text)
        self.assertEqual(new_nodes[0].text, "This is an ")
        self.assertEqual(new_nodes[0].text_type, TextType.plain_text)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.italic_text)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.plain_text)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.plain_text,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.plain_text),
                TextNode("image", TextType.images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.plain_text),
                TextNode(
                    "second image", TextType.images, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.facebook.com)",
            TextType.plain_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.plain_text),
                TextNode("link", TextType.links, "https://www.google.com"),
                TextNode(" and another ", TextType.plain_text),
                TextNode(
                    "second link", TextType.links, "https://www.facebook.com"
                ),
            ],
            new_nodes,
        )
    def test_text_to_text_nodes(self):
        text = "This is a **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)"
        new_nodes = text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.plain_text),
                TextNode("bold", TextType.bold_text),
                TextNode(" text with an ", TextType.plain_text),
                TextNode("image", TextType.images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.plain_text),
                TextNode("link", TextType.links, "https://www.google.com"),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()