from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5 import uic
# import pyupbit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/최종Coin_overview/main.ui", self)
        # main.ui 파일을 불러옴(모든 위젯이 들어있음)

    #     with open('key.txt') as f:
    #         lines = f.readlines()
    #         access = lines[0].strip()
    #         secret = lines[1].strip()

    #     self.key0.setText(access)
    #     self.key1.setText(secret)

    #     self.btn.setText("로그인")
    #     self.btn.clicked.connect(self.login)
    
    # def login(self):
    #     if self.btn.text() == "로그아웃":
    #         self.upbit = None
    #         self.log.append("로그아웃 되었습니다.")
    #         self.btn.setText("로그인")
    #         return
    #     else:
    #         self.upbit = pyupbit.Upbit(key0.text(), key1.text())
    #         balance = self.upbit.get_balance("KRW")
    #         self.log.append(f"로그인 성공: {balance} 원 보유 중")
    #         self.btn.setText("로그아웃")



    def closeEvent(self, event):
        self.overview.closeEvent(event)
        self.chart.closeEvent(event)
        self.orderbook.closeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()