"""表格

三种基本元素
    表格 QTableWidget
    表头 QTableWidget.setHorizontalHeaderLabels
    单元格 QTableWidgetItem

为表格添加单元格 QTableWidget.setItem(row, col, item)
"""
import sys

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QColor

colors = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
    ("Black", "#000000"),
    ("White", "#FFFFFF"),
    ("Electric Green", "#41CD52"),
    ("Dark Blue", "#222840"),
    ("Yellow", "#F9E56d")
]


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


def func():
    app = QApplication(sys.argv)

    table = QTableWidget()
    table.setRowCount(len(colors))
    table.setColumnCount(len(colors[0]) + 1)
    table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

    for i, (name, code) in enumerate(colors):
        item_name = QTableWidgetItem(name)
        item_code = QTableWidgetItem(code)
        item_color = QTableWidgetItem()
        item_color.setBackground(get_rgb_from_hex(code))

        table.setItem(i, 0, item_name)
        table.setItem(i, 1, item_code)
        table.setItem(i, 2, item_color)

    table.show()
    sys.exit(app.exec())


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
