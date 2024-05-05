from pyupbit import WebSocketManager
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class Worker(QThread): # 서브 스레드
    received = pyqtSignal(dict)
    def run(self):
        wm = WebSocketManager("ticker", ["KRW-BTC"]) # 웹소켓 매니저 생성(새로운 프로세스 생성)
        self.alive = True
        while self.alive:
            data = wm.get() # 큐를 통해 데이터를 받음
            self.received.emit(data) # 데이터를 메인 프로세스로 보냄
        wm.terminate()

    def stop(self):
        self.alive = False


class OverviewWidget(QWidget): # 메인 프로세스
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/Coin_overview/overview.ui",self)

        self.worker = Worker() # 스레드 생성
        self.worker.received.connect(self.process_data) 
        self.worker.start() # Worker의 run함수 실행

    def process_data(self, data):
        self.price.setText(str(data['trade_price']))
        self.diff.setText(f"{data['signed_change_rate']*100:.2f} %")
        self.volume.setText(str(data['acc_trade_volume_24h']))
        self.value.setText(f"{data['acc_trade_price_24h']/100000000:,.2f} 억원")
        self.strength.setText(f"{data['acc_ask_volume']/data['acc_bid_volume']*100:.2f}")
        self.high.setText(str(data['high_price']))
        self.low.setText(str(data['low_price']))
        self.last.setText(str(data['prev_closing_price']))
    
        if data['change'] == "RISE":
            self.price.setStyleSheet("color: red")
            self.diff.setStyleSheet("color: white ; background-color: red")
        else:
            self.price.setStyleSheet("color: blue")
            self.diff.setStyleSheet("color: white ; background-color: blue")

    def closeEvent(self, event):
        self.worker.stop()
        event.accept() # 창을 닫을 때 스레드도 종료


if __name__ == "__main__":
    app = QApplication([])
    mywindow = OverviewWidget()
    mywindow.show()
    app.exec_()
    
    
