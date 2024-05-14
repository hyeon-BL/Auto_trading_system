from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/i4u11/Desktop/Work/Auto_trading_system/디자이너/ex.ui', self)

        self.edit.setText("Hello")
        self.button.clicked.connect(self.btn_clicked)
        
        self.clickflg = True
    def btn_clicked(self):
        if self.clickflg:
            self.edit.setText("버튼클릭")
            self.clickflg = False
        else:
            self.edit.setText("버튼클릭안함")
            self.clickflg = True

if __name__ == "__main__":
    app = QApplication([])
    Mywindow = MyWindow()
    Mywindow.show()
    app.exec_()