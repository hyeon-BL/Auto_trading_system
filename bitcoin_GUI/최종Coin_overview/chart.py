from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyupbit
import time

class ChartWorker(QThread):
    dataSent = pyqtSignal(float)
    def run(self):
        self.alive = True
        while self.alive:
            try:
                price = pyupbit.get_current_price("KRW-BTC")
                self.dataSent.emit(price)
            except:
                pass
            time.sleep(1)

    def end(self):
        self.alive = False

class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/최종Coin_overview/chart.ui", self)

        # 1) 데이터 추가
        self.priceData = QLineSeries()

        # 2) 도화지 연결
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()
        self.priceChart.layout().setContentsMargins(0, 0, 0, 0)

        ax = QValueAxis()
        self.priceChart.addAxis(ax, Qt.AlignBottom)

        ay = QValueAxis()
        ay.setVisible(False)
        self.priceChart.addAxis(ay, Qt.AlignLeft)

        self.priceData.attachAxis(ax)
        self.priceData.attachAxis(ay)

        # 3) 위젯에 출력
        self.priceView.setChart(self.priceChart)
        self.priceView.setRenderHints(QPainter.Antialiasing)

        self.cw = ChartWorker()
        self.cw.dataSent.connect(self.appendData)
        self.cw.start()

        self.idx = 0
        self.viewLimit = 60

    def closeEvent(self, event):
        self.cw.end()

    def appendData(self, price):
        if len(self.priceData) == self.viewLimit:
            self.priceData.remove(0)

        self.priceData.append(self.idx, price)
        self.idx += 1

        pvs = self.priceData.pointsVector()
        x = pvs[0].x()

        ax = self.priceChart.axisX()
        ax.setRange( x, x + self.viewLimit - 1)

        ay = self.priceChart.axisY()
        dataY = [item.y() for item in pvs]
        ay.setRange( min(dataY), max(dataY) )



if __name__ == "__main__":
    app = QApplication([])
    m = ChartWidget()
    m.show()
    app.exec_()