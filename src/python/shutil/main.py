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


if __name__ == "__main__":
    path = '/home/percy/Documents/Project/Tutorials/JavaTutorial/src/main/java/percy/spring'
    func1(path)
    print('Done!')