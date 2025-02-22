import random
import sys
import io
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow


temp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Кнопка</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class AlphaManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)
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
        qp.setBrush(QColor('yellow'))
        r = random.randint(10, 80)
        qp.drawEllipse(random.randint(100, 800), random.randint(100, 600), r, r)
        self.k = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())