"""os.system()
"""
import os


def create_file(dirs, target):
    for d in dirs:
        file = os.path.join(d, target)
        # print(file)
        os.system(f'touch {file}')


if __name__ == "__main__":
    target = 'README.md'
    root = os.path.join(os.getcwd(), 'src')
    dirs = filter(os.path.isdir, map(lambda filename: os.path.join(root, filename), os.listdir(root)))
    create_file(dirs, target)