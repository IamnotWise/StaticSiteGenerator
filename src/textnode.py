from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    plain_text = "text(plain)"
    bold_text = "**Bold text**"
    italic_text = "_Italic text_"
    code_text = "'Code text'"
    links = "[anchor text](url)"
    images = "![alt text](url)"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
        
        if text_node.text_type is TextType.plain_text:
            return LeafNode(None,text_node.text)
        
        if text_node.text_type is TextType.bold_text:
            return LeafNode("b",text_node.text)

        if text_node.text_type is TextType.italic_text:
            return LeafNode("i",text_node.text)

        if text_node.text_type is TextType.code_text:
            return LeafNode("code",text_node.text)

        if text_node.text_type is TextType.links:
            return LeafNode("a",text_node.text,{"href": text_node.url})

        if text_node.text_type is TextType.images:
            return LeafNode("img","",{
                "src": text_node.url,
                "alt": text_node.text
            })
        raise Exception("Type not declared in Enum.")

