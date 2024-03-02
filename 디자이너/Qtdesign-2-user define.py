from mywidget import Mywidgetset
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        w0 = Mywidgetset(self)

        w1 = Mywidgetset(self)
        w1.move(0, 40)

        # w2 = Mywidgetset(self)
        # w2.move(0, 80)

if __name__ == "__main__":
    app = QApplication([])
    Mywindow = MyWindow()
    Mywindow.show()
    app.exec_()