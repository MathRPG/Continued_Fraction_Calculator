import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1080, 720)
    win.setWindowTitle("Hello, world!")

    label = QtWidgets.QLabel(win)
    label.setText("This is a label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
