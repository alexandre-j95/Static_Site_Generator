import os
import shutil


# Function that prepares the destination directory and calls a helper to copy each file from source
def copy_files(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise ValueError("invalide source folder")

    if os.path.exists(destination):
        print(f"Removing directory {destination}")
        shutil.rmtree(destination)
    copy_files_helper(source, destination)


def copy_files_helper(source: str, destination: str) -> None:
    print(f"Creating directory {destination}")
    os.mkdir(destination)
    nodes = os.listdir(source)
    for node in nodes:
        path = os.path.join(source, node)
        if os.path.isfile(path):
            print(f"Copying {path} to destination")
            shutil.copy(path, destination)
        else:
            copy_files_helper(path, os.path.join(destination, node))
