import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(60, 70, 1000, 800)
        self.setWindowTitle('Библиотека')



        self.bibl = QLabel(self)
        self.bibl.setText('Сайт библиотеки')
        self.bibl.move(400, 10)
        self.bibl.setFont(QtGui.QFont('Calibri', 20))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = Window1()
    w1.show()
    sys.exit(app.exec())