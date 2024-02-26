from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QIcon

class Mywidget(QMainWindow): # QMainWindow는 전체 윈도우를 의미
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Hello, World!')
        self.setWindowIcon(QIcon("C:/Users/i4u11/Desktop/Work/Auto_trading_system/GUI/analytics_chart_growth_increasing_stocks_icon.svg"))

app = QApplication([])

label = Mywidget()
label.show()

app.exec_()