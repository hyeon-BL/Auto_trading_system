from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUI('"C:/Users/i4u11/Desktop/Work/Auto_trading_system/라인차트/chart.ui"',self)


if __name__ == "__main__":
    app = QApplication([])
    chart = ChartWidget()
    chart.show()
    app.exec_()