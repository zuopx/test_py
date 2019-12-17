"""
Process filesystem
"""
import os
import glob
import shutil


def func1(path):
    """
    """
    dirname, basename = os.path.split(path)
    newpath = os.path.join(dirname, 'new' + basename)
    os.mkdir(newpath)
    for subdir in os.listdir(path):
        newsubpath = os.path.join(newpath, subdir.lower().replace('_', ''))
        os.mkdir(newsubpath)
        fs = glob.glob(path + '/subdir/**/src/**/*.*', recursive=True)
        for f in fs:
            shutil.copy(f, newsubpath)
        # d = os.path.join(path, subdir, 'src/app')
        # fs = os.listdir(d)
        # for f in fs:
        #     shutil.copy(os.path.join(d, f), newsubpath)

def create_gitkeep(path):
    """Create a file named .gitkeep in each empty directory rooted path.
    """
    for dirname, subdirs, files in os.walk(path):
        if not files and not subdirs and dirname:
            print(dirname)

if __name__ == "__main__":
    path = os.getcwd()
    create_gitkeep(path)
    print('Done!')