
from markdown import extract_title, markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
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
    final_html = template_file
    #Write the final html to the dest path
    with open(dest_path, 'w') as file:
        file.write(final_html)
    print(f"Final_html: {final_html}")
