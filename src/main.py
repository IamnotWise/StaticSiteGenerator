from pagegeneration import generate_pages_recursive
import os, shutil, sys

def copy_static():
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    shutil.copytree('static', 'docs')
    #testing page generation
       
def main():
    args = sys.argv
    basepath = ""
    if len(args) > 1:
        basepath = args[1]
    else:
        basepath = "/"

    copy_static()

    generate_pages_recursive('content', 'template.html', 'docs', basepath)

if __name__ == '__main__':
    main()
