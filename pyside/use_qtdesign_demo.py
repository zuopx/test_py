"""使用qtdesign

三步走
    完成xxx.ui
    转换为xxx.py
    导入xxx.py
"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_qtdesign_demo import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 把self传进去


def func():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
