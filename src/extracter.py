import re

def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
    print(matches)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\]]*)\]\(([^)]+)\)', text)
    print(matches)
    return matches