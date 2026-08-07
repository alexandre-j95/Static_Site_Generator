import os
from pathlib import Path

from markdown_blocks import extract_title, markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        origin = f.read()

    with open(template_path) as t:
        template = t.read()

    html_text = markdown_to_html_node(origin).to_html()
    title = extract_title(origin)

    add_title = template.replace("{{ Title }}", title)
    add_content = add_title.replace("{{ Content }}", html_text)
    add_href = add_content.replace('href="/', f'href="{basepath}')
    final_text = add_href.replace('src="/', f'src="{basepath}')

    dir_name = os.path.dirname(dest_path)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    with open(dest_path, "w") as f:
        f.write(final_text)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    directory = os.listdir(dir_path_content)
    for node in directory:
        fullpath = os.path.join(dir_path_content, node)
        fulldest = os.path.join(dest_dir_path, node)
        if os.path.isfile(fullpath):
            fulldest = Path(fulldest).with_suffix(".html")
            generate_page(fullpath, template_path, fulldest, basepath)
        else:
            generate_pages_recursive(fullpath, template_path, fulldest, basepath)
