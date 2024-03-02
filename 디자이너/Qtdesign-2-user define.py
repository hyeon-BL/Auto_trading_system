from mywidget import Mywidgetset
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w0 = Mywidgetset("BTC",self)

        self.w1 = Mywidgetset("LTC",self)
        self.w1.move(0, 60)

        self.w2 = Mywidgetset("XRP",self)
        self.w2.move(0, 120)

if __name__ == "__main__":
    app = QApplication([])
    Mywindow = MyWindow()
    Mywindow.show()
    app.exec_()