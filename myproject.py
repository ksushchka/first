import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 100)

        self.text = QLineEdit(self)
        self.text.move(5, 55)
        self.text.resize(345, 30)

        self.setWindowTitle('Азбука Морзе 2')
        self.alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
        self.morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                      'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                      'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                      'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                      'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                      'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                      'y': '-.--', 'z': '--..'}
        x = 5
        y = 10
        k = 1
        num = 0
        for j in range(2):
            for i in range(15):
                if i == 11 and j == 1:
                    k = 0
                    break
                self.btn = QPushButton(self.alf[num], self)
                self.btn.resize(20, 20)
                self.btn.move((x + 20) * i + 5, (y + 20) * j)
                self.btn.clicked.connect(self.button)
                num += 1
            if i == 11 and k == 0:
                break

    def button(self):
        rez = str(self.morze[self.btn.text()])
        self.text.setText(rez)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())