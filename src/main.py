from textnode import TextNode, TextType
import os, shutil

def copy_static():
    if os.path.exists('public'):
        shutil.rmtree('public')
    shutil.copytree('static', 'public')
       
def main():
    # This is just a test to make sure the TextNode class works
    #print("hello world")
    #node = TextNode("Need a Latina",TextType.links, "https://www.boot.dev")
    #print(node)
    copy_static()

if __name__ == '__main__':
    main()
