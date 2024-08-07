""""""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from PySide6.QtWidgets import QVBoxLayout


class Form(QDialog):
    def __init__(self, *args):
        super().__init__(*args)

        self.setWindowTitle("My Form")

        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show Greetings")
        self.greet = QLineEdit("hello")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.greet)

        self.button.clicked.connect(self.greeting)

    def greeting(self):
        print(f"Hello, {self.edit.text()}")
        self.greet.setText(f"Hello, {self.edit.text()}")


def func():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
