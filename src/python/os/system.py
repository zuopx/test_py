"""os.system()
"""
import os


def create_file(dirs, target):
    for d in dirs:
        file = os.path.join(d, target)
        # print(file)
        os.system(f'touch {file}')


def add_lib(dir: str, template: str):
    """Add .jar files within the given directory into .classpath file based the template."""
    result = map(lambda filename: template.replace("?", filename), os.listdir(dir))
    return result


if __name__ == "__main__":
    dir = '/home/percy/Projects/Tutorials/mrbbs/WebContent/WEB-INF/lib'
    template = '<classpathentry kind="lib" path="WebContent/WEB-INF/lib/?"/>'
    result = add_lib(dir, template)
    for r in result:
        print(r)
