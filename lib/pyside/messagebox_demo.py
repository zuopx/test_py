"""对话框

"""
import sys

from PySide6.QtWidgets import QApplication, QMessageBox


def func():
    app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText("The document has been modified.")
    msgBox.show()
    sys.exit(app.exec())

def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
