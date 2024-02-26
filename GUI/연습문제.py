from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTableWidget
import pyupbit

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tw = QTableWidget(self)
        tw.setRowCount(5)
        tw.setColumnCount(2)
        tw.resize(400, 300)
        self.resize(400, 300)
        tw.setHorizontalHeaderLabels(['코인', '가격'])

        df = pyupbit.get_orderbook("KRW-BTC")
        for item in df[0]['orderbook_units']:
            for i in range(len(df[0]['orderbook_units'])):
                tw.setItem(i, 0, QLabel(str(item['ask_price'])))
                tw.setItem(i, 1, QLabel(str(item['ask_size'])))

        self.move(300, 300)
        self.setWindowTitle('호가창')

        
if __name__ == '__main__':
    app = QApplication([])
    label = MyMainWindow()
    label.show()
    app.exec_()