

from blocknode import BlockType, block_to_block_type
from delimiter import text_to_text_nodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split('\n\n')
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks

def markdown_to_html_node(markdown):
    parent_node = ParentNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = 0
            while level < len(block) and block[level] == "#":
                level += 1
            heading = block[level + 1:]  # skip the '#'s and the space
            children = text_to_children(heading)
            node = ParentNode(f"h{level}", children)
        elif block_type == BlockType.CODE:
            # block looks like: "```\nsome code\n```"
            # we want just the inner content with the trailing newline preserved
            inner = block[4:-3]  # skip "```\n" and trailing "```"
            raw_text_node = TextNode(inner, TextType.plain_text)
            code_leaf = text_node_to_html_node(raw_text_node)
            code_node = ParentNode("code", [code_leaf])
            node = ParentNode("pre", [code_node])
        elif block_type == BlockType.QUOTE:
            childrent = text_to_children(block.lstrip("> ").replace("\n> ", "\n"))
            node = ParentNode("blockquote", childrent)
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                item_text = item.lstrip("- ").strip()
                children = text_to_children(item_text)
                li_nodes.append(ParentNode("li", children))
            node = ParentNode("ul", li_nodes)
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                item_text = item.lstrip("0123456789. ").strip()
                children = text_to_children(item_text)
                li_nodes.append(ParentNode("li", children))
            node = ParentNode("ol", li_nodes)
        else:
            children = text_to_children(block.replace("\n", " "))
            node = ParentNode("p", children)
        parent_node.children.append(node)
    return parent_node

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    for i, node in enumerate(text_nodes):
        text_nodes[i] = text_node_to_html_node(node)
    return text_nodes
def extract_title(markdown):
    heading = markdown.strip().split('\n')[0]
    if not heading:
        raise Exception("Markdown cannot be empty")
    if not heading.startswith("# "):
        raise Exception("Markdown must begin with # and cannot be empty")
    return heading.lstrip("#").strip()