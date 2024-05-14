from pyupbit import WebSocketManager
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread): # 서브 스레드
    received = pyqtSignal(dict)
    def run(self):
        wm = WebSocketManager("ticker", ["KRW-BTC", "KRW-ETH"]) # 웹소켓 매니저 생성(새로운 프로세스 생성)
        self.alive = True
        while self.alive:
            data = wm.get() # 큐를 통해 데이터를 받음
            self.received.emit(data) # 데이터를 메인 프로세스로 보냄
        wm.terminate()

    def stop(self):
        self.alive = False


class MyWindow(QMainWindow): # 메인 프로세스
    def __init__(self):
        super().__init__()

        self.worker = Worker() # 스레드 생성
        self.worker.received.connect(self.process_data) 
        self.worker.start() # Worker의 run함수 실행

    def process_data(self, data):
        print(data)

    def closeEvent(self, event):
        self.worker.stop()
        event.accept() # 창을 닫을 때 스레드도 종료


if __name__ == "__main__":
    app = QApplication([])
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
    
    
