import sys
from math import sin, cos, pi
from random import randint
from PyQt5 import uic

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QInputDialog



class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = randint(20, 100)
        # self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(randint(100, 700) - R / 2,
                            randint(100, 500) - R / 2, R, R)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())
