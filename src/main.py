from copy_static_files import copy_files
from generate_content import generate_page, generate_pages_recursive
from textnode import TextNode


def main():
    copy_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

    # test_node = TextNode("this is some anchor text", "link", "https://www.boot.dev")
    # print(test_node)


main()
