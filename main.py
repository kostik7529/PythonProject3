import random
import sys
import io
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from UI import Ui_MainWindow



class AlphaManagement(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.k = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.k = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.k:
            self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        r = random.randint(10, 80)
        qp.drawEllipse(random.randint(100, 800), random.randint(100, 600), r, r)
        self.k = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())