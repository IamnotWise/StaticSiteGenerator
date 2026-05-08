from pagegeneration import generate_pages_recursive
import os, shutil

def copy_static():
    if os.path.exists('public'):
        shutil.rmtree('public')
    shutil.copytree('static', 'public')
    #testing page generation
    generate_pages_recursive('content', 'template.html', 'public')
       
def main():
    copy_static()

if __name__ == '__main__':
    main()
