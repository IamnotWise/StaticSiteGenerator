from pagegeneration import generate_page
from textnode import TextNode, TextType
import os, shutil

def copy_static():
    if os.path.exists('public'):
        shutil.rmtree('public')
    shutil.copytree('static', 'public')
    #testing page generation
    generated_page = generate_page('content/index.md','template.html','public/index.html')
       
def main():
    copy_static()

if __name__ == '__main__':
    main()
