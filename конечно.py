import sys
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Миникалькулятор')

        self.name1 = QLabel(self)
        self.name1.setText('Первое число(целое):')
        self.name1.move(20, 10)

        self.name2 = QLabel(self)
        self.name2.setText('Второе число(целое):')
        self.name2.move(20, 75)

        self.c1 = QLineEdit(self)
        self.c1.move(17, 35)

        self.c2 = QLineEdit(self)
        self.c2.move(17, 100)

        self.btn = QPushButton('->', self)
        self.btn.resize(50, 20)
        self.btn.move(140, 66)
        self.btn.clicked.connect(self.inc_click)


        self.summa = QLabel(self)
        self.summa.setText('Сумма:')
        self.summa.move(250, 25)

        self.summacount = QLCDNumber(self)
        self.summacount.move(300, 20)

        self.razn = QLabel(self)
        self.razn.setText('Разность:')
        self.razn.move(235, 50)

        self.razncount = QLCDNumber(self)
        self.razncount.move(300, 45)

        self.proizv = QLabel(self)
        self.proizv.setText('Произведение:')
        self.proizv.move(209, 75)

        self.proizvcount = QLCDNumber(self)
        self.proizvcount.move(300, 70)

        self.chast = QLabel(self)
        self.chast.setText('Частное:')
        self.chast.move(240, 100)

        self.chastcount = QLCDNumber(self)
        self.chastcount.move(300, 95)

    def strela(self):
        self.btn.setText('->')

    def inc_click(self):
        if self.c1.text().isnumeric() and self.c2.text().isnumeric():
            self.summacount.display(int(self.c1.text()) +\
                                    int(self.c2.text()))
            self.razncount.display(int(self.c1.text()) -\
                                    int(self.c2.text()))
            self.proizvcount.display(int(self.c1.text()) *\
                                    int(self.c2.text()))
            if float(self.c2.text()) != 0:
                self.chastcount.display(int(self.c1.text()) /\
                                    int(self.c2.text()))
            else:
                self.chastcount.display('ERROR')
        else:
            self.summacount.display('ERROR')
            self.razncount.display('ERROR')
            self.proizvcount.display('ERROR')
            self.chastcount.display('ERROR')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())