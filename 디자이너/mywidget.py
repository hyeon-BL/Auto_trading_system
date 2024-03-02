from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class Mywidgetset(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi('C:/Users/i4u11/Desktop/Work/Auto_trading_system/디자이너/mywidget.ui', self)

        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼클릭")