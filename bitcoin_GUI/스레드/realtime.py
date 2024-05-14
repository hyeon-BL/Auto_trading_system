from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pyupbit
import time

class orderbookworker(QThread):
    datarecieved = pyqtSignal(dict) # pyqtSignal을 통해 데이터를 보내줄 수 있음

    def run(self): # thread 실행시 실행되는 함수
        while True: # qthread는 무한루프를 돌면서 계속 실행
            data = pyupbit.get_orderbook("KRW-BTC")
            self.datarecieved.emit(data) # 데이터를 보내줌
            time.sleep(0.2)

class orderbookwidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/i4u11/Desktop/Work/Auto_trading_system/스레드/orderbook.ui', self)
        self.worker = orderbookworker()
        self.worker.datarecieved.connect(self.update_orderbook) # worker로부터 데이터를 받으면 update_orderbook함수 실행
        self.worker.start() # orderbookworker의 run함수 실행

    def update_orderbook(self, data):
        data = data['orderbook_units']
        for item in data[:10]:
            i = data.index(item)
            value = item['ask_price'] * item['ask_size']
            d = QTableWidgetItem(str(item['ask_price']))
            self.asktable.setItem(9-i, 0, d)
            d = QTableWidgetItem(str(item['ask_size']))
            self.asktable.setItem(9-i, 1, d)
            d = QTableWidgetItem(str(value))
            self.asktable.setItem(9-i, 2, d)

            value = item['bid_price'] * item['bid_size']
            d = QTableWidgetItem(str(item['bid_price']))
            self.bidtable.setItem(9-i, 0, d)
            d = QTableWidgetItem(str(item['bid_size']))
            self.bidtable.setItem(9-i, 1, d)
            d = QTableWidgetItem(str(value))
            self.bidtable.setItem(9-i, 2, d)


if __name__ == '__main__':
    app = QApplication([])
    ex = orderbookwidget()
    ex.show()
    app.exec_()