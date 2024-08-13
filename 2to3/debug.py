"""test 2to3 package

source -> tree -> refactor tree-> new tree -> new sourse
refactor tree: fixer.start_tree, fixer.match, fixer.transform, fixer.finish_tree
"""
import lib2to3.main


def debug_2to3():
    lib2to3.main.main("lib2to3.fixes", ["-f" "long", "2to3/script_long.py", ])


def main():
    debug_2to3()
    print("hello, world")


if __name__ == "__main__":
    main()
