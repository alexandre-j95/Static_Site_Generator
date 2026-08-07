import sys
from copy_static_files import copy_files
from generate_content import generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_files("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
