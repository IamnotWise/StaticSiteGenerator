
from markdown import extract_title, markdown_to_html_node
import os



def generate_page(from_path, template_path, dest_path, basepath):
    #Page geneartion message
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    #Read the markdown file and template file
    with open (from_path, 'r') as file:
        markdown_file = file.read()
    with open (template_path, 'r') as file:
        template_file = file.read()
    #Convert the markdown file to html
    node = markdown_to_html_node(markdown_file)
    html = node.to_html()
    #Grab title from markdown file
    title = extract_title(markdown_file)
    #Replace the {{content}} and {{title}} in the template with the html and title
    template_file = template_file.replace("{{ Content }}", html)
    template_file = template_file.replace("{{ Title }}", title)

    template_file = template_file.replace('href="/', f'href="{basepath}')
    template_file = template_file.replace('src="/', f'src="{basepath}')

    final_html = template_file
    #Write the final html to the dest path
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(final_html)
    print(f"Final_html: {final_html}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        full_entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_entry_path):
            if full_entry_path.endswith('.md'):
                generate_page(full_entry_path, template_path, os.path.join(dest_dir_path, entry.replace('.md', '.html')),basepath)
        else:
            generate_pages_recursive(full_entry_path, template_path, os.path.join(dest_dir_path, entry), basepath)