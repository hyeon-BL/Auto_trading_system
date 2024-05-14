from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import pyupbit

class Worker(QThread):
    currPrice = pyqtSignal( float ) # 출력값이 실수이므로 float으로 선언
    diffPrice = pyqtSignal(  str ) # 출력값이 문자열이므로 str로 선언

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        prev = None
        while True:
            price = pyupbit.get_current_price(self.ticker)
            self.currPrice.emit(  price  )

            if prev != None:
                if prev < price :
                    self.diffPrice.emit("up")
                else:
                    self.diffPrice.emit("down")

            prev = price
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("1000", self)
        self.label_diff_0 = QLabel("-", self)
        self.label_diff_0.move(100, 0)

        self.label2 = QLabel("1000", self)
        self.label2.move(0, 40)

        self.w0 = Worker("KRW-BTC")
        self.w0.currPrice.connect(self.btcPrice)
        self.w0.diffPrice.connect(self.btcDiffPrice)
        self.w0.start()

        self.w1 = Worker("KRW-SOL")
        self.w1.currPrice.connect(self.solPrice)
        self.w1.start()

    def btcDiffPrice(self, value):
        self.label_diff_0.setText(value)

    def solPrice(self, value):
        self.label2.setText(str(value))

    def btcPrice(self, value):
        self.label.setText(str(value))


app = QApplication([])
m = MyWindow()
m.show()
app.exec_()