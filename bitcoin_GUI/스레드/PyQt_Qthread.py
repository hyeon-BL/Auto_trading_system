from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit

class Worker(QThread):
    def __init__(self, ticker="KRW-BTC"):
        self.ticker = ticker
        super().__init__()
    def run(self):
        while True:
            print(pyupbit.get_current_price(self.ticker))
            print("working...")
            self.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w0 = Worker()
        self.w0.start() # QThread 안에 정의된 start 메소드에 의해 run 메소드가 실행된다.
        self.w1 = Worker("KRW-ETH")
        self.w1.start()

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()