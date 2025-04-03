import os.path
import shutil

from extract_md import extract_title
from md_to_html import markdown_to_html_node
from textnode import TextNode, TextType

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path) as f:
        md = f.read()

    with open(template_path) as f:
        tmpl = f.read()

    nodes = markdown_to_html_node(md)
    html = nodes.to_html()
    title = extract_title(md)

    tmpl = tmpl.replace('{{ Title }}', title)
    tmpl = tmpl.replace('{{ Content }}', html)

    with open(dest_path, 'w') as of:
        of.write(tmpl)

def generate_pages_rc(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        print(f"Making dir {dest_dir_path}")
        os.mkdir(dest_dir_path)

    entries = os.listdir(dir_path_content)
    for e in entries:
        entpath = os.path.join(dir_path_content, e)
        entdst = os.path.join(dest_dir_path, e)
        if os.path.isfile(entpath):
            entdst = entdst.replace('.md', '.html')
            print(f"Generating html from {entpath} to: {entdst}")
            generate_page(entpath, template_path, entdst)
        else:
            generate_pages_rc(entpath, template_path, entdst)


def copy_static(path, srcpath, destpath):
    srcdir = os.path.join(srcpath,path)
    destdir = os.path.join(destpath,path)
    if not os.path.exists(destdir):
        print(f"Making dir {destdir}")
        os.mkdir(destdir)

    entries = os.listdir(srcdir)
    for e in entries:
        entpath = os.path.join(srcdir, e)
        entdst = os.path.join(destdir, e)
        if os.path.isfile(entpath):
            print(f"Copying file {entpath} to: {entdst}")
            shutil.copy(entpath, entdst)
        else:
            print(f"Entering Dir {entpath}.")
            copy_static(e, srcdir, destdir)



def publish_static(rel = ''):
    if os.path.exists(f'{rel}public'):
       shutil.rmtree(f'{rel}public')
    os.mkdir(f'{rel}public')
    copy_static('' , f'{rel}static', f'{rel}public')

def main(rel = ''):
    publish_static(rel)
    generate_pages_rc(f'{rel}content', f'{rel}template.html', f'{rel}public')

if __name__ == '__main__':
    main()