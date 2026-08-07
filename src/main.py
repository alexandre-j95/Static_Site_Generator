from copy_static_files import copy_files
from textnode import TextNode


def main():
    copy_files("static", "public")
    test_node = TextNode("this is some anchor text", "link", "https://www.boot.dev")
    print(test_node)


main()
