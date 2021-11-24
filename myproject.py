import sys
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # создание окна
        self.setGeometry(300, 150, 1000, 700)
        self.setWindowTitle('Библиотека')
        # надпись
        self.bib = QLabel(self)
        self.bib.setText('Библиотека.Книги')
        self.bib.move(10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())