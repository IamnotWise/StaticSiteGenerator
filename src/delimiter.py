from extracter import extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain_text:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"No closing delimiter found for {delimiter} in {node.text}")
        split_text = node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.plain_text))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.plain_text:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for alt, url in images:
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.plain_text))
            new_nodes.append(TextNode(alt, TextType.images, url))
            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.plain_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain_text:
            new_nodes.append(node)
            continue
        split_text = node.text.split("[")
        for i, text in enumerate(split_text):         
            if text == "":
                continue
            if i == 0:
                new_nodes.append(TextNode(text, TextType.plain_text))
            else:
                link_text, url = text.split("](")
                url,remaining = url.split(")",1)
                new_nodes.append(TextNode(link_text, TextType.links, url))
                if remaining != "":
                    new_nodes.append(TextNode(remaining, TextType.plain_text))
    return new_nodes
def text_to_text_nodes(text):
    nodes = [TextNode(text, TextType.plain_text)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold_text)
    nodes = split_nodes_delimiter(nodes, "_", TextType.italic_text)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code_text)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


