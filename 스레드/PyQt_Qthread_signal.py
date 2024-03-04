from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit

class Worker(QThread):
    currPrice = pyqtSignal( float )

    def __init__(self, ticker="KRW-BTC"):
        self.ticker = ticker
        super().__init__()

    def run(self):
        while True:
            self.currPrice.emit( pyupbit.get_current_price(self.ticker) )
            print("working...")
            self.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w0 = Worker()
        self.w0.currPrice.connect( self.btcPrice ) # WorkThread의 Signal을 connect하여 MainThread에서 btcPrice 메소드를 실행시킨다.
        self.w0.start()
        self.w1 = Worker("KRW-ETH")
        self.w1.start()

    def btcPrice(self, price):
        print("BTC: ", price)


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()