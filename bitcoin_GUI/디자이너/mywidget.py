from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
class Mywidgetset(QWidget):
    def __init__(self, ticker, parent = None):
        super().__init__(parent)
        uic.loadUi('C:/Users/i4u11/Desktop/Work/Auto_trading_system/디자이너/mywidget.ui', self)

        self.ticker = ticker
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        price = pyupbit.get_current_price(self.ticker)
        self.price.setText(str(price)) # price 라벨에 현재가 출력
        print(f"{self.ticker} 버튼클릭")