from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pyupbit
import time

class orderbookworker(QThread):
    datarecieved = pyqtSignal(dict) # pyqtSignal을 통해 데이터를 보내줄 수 있음

    def run(self): # thread 실행시 실행되는 함수
        self.alive = True
        while self.alive: # qthread는 무한루프를 돌면서 계속 실행
            data = pyupbit.get_orderbook("KRW-BTC")
            self.datarecieved.emit(data) # 데이터를 보내줌
            time.sleep(0.2)

    def end(self):
        self.alive = False

class orderbookwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('C:/Users/i4u11/Desktop/Work/Auto_trading_system/스레드/orderbook.ui', self)
        
        self.askani = []
        self.bidani = []
        
        self.worker = orderbookworker()
        self.worker.datarecieved.connect(self.update_orderbook) # worker로부터 데이터를 받으면 update_orderbook함수 실행
        self.worker.start() # orderbookworker의 run함수 실행

        for i in range(10):
            d = QTableWidgetItem(str(""))
            d.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.asktable.setItem(i, 0, d)
            d = QTableWidgetItem(str(""))
            d.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.asktable.setItem(i, 1, d)
            d = QProgressBar(self.asktable)
            d.setStyleSheet("QProgressBar::chunk {background-color: rgba(255,0,0,0.5);}")
            d.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            ani = QPropertyAnimation(d, b"value")
            ani.setDuration(200)
            ani.setStartValue(0)
            self.askani.append(ani)
            self.asktable.setCellWidget(i, 2, d)

            d = QTableWidgetItem(str(""))
            d.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.bidtable.setItem(i, 0, d)
            d = QTableWidgetItem(str(""))
            d.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.bidtable.setItem(i, 1, d)
            d = QProgressBar(self.bidtable)
            d.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            d.setStyleSheet("QProgressBar::chunk {background-color: rgba(0,0,255,0.5);}")
            ani = QPropertyAnimation(d, b"value")
            ani.setDuration(200)
            ani.setStartValue(0)
            self.bidani.append(ani)
            self.bidtable.setCellWidget(i, 2, d)

    def update_orderbook(self, data):
        data = data['orderbook_units']

        values = []
        for item in data[:10]:
            value = item['ask_price'] * item['ask_size']
            values.append(value)
            value = item['bid_price'] * item['bid_size']
            values.append(value)

        max_value = max(values)


        for item in data[:10]:
            i = data.index(item)
            value = item['ask_price'] * item['ask_size']

            d = self.asktable.item(9-i, 0)
            d.setText(str(item['ask_price'])) 
            d = self.asktable.item(9-i, 1)
            d.setText(str(item['ask_size']))
            d = self.asktable.cellWidget(9-i, 2)
            d.setRange(0, int(max_value))
            d.setFormat(f"{value:,.0f}")
            self.askani[9-i].setStartValue(d.value())
            self.askani[9-i].setEndValue(int(value)) 
            self.askani[9-i].start()

            value = item['bid_price'] * item['bid_size']
            d = self.bidtable.item(i, 0)
            d.setText(str(item['bid_price']))
            d = self.bidtable.item(i, 1)
            d.setText(str(item['bid_size']))
            d = self.bidtable.cellWidget(i, 2)
            d.setRange(0, int(max_value))
            d.setFormat(f"{value:,.0f}")
            self.bidani[i].setStartValue(d.value())
            self.bidani[i].setEndValue(int(value)) 
            self.bidani[i].start()

    def closeEvent(self, event):
        self.worker.end()


if __name__ == '__main__':
    app = QApplication([])
    ex = orderbookwidget()
    ex.show()
    app.exec_()