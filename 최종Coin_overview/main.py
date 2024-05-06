from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/최종Coin_overview/main.ui", self)
        # main.ui 파일을 불러옴(모든 위젯이 들어있음)

    def closeEvent(self, event):
        self.overview.closeEvent(event)
        self.chart.closeEvent(event)
        self.orderbook.closeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()