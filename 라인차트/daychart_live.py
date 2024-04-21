import pyupbit
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class Worker(QThread):
    dataSent = pyqtSignal(float)
    def run(self):
        while True:
            df = pyupbit.get_current_price("KRW-BTC")
            self.dataSent.emit(df)
            time.sleep(1)


class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/라인차트/chart.ui",self)

        # 1) 데이터 추가
        self.chartData = QLineSeries()

        # 2) 도화지 연결
        self.lineChart = QChart()
        self.lineChart.addSeries(self.chartData)
        self.lineChart.legend().hide()
        self.lineChart.layout().setContentsMargins(0, 0, 0, 0)

        ax = QValueAxis()
        self.lineChart.addAxis(ax, Qt.AlignBottom)

        data = self.chartData.pointsVector()
        dataY = [p.y() for p in data]

        ay = QValueAxis()
        self.lineChart.addAxis(ay, Qt.AlignLeft)

        self.chartData.attachAxis(ax)
        self.chartData.attachAxis(ay) 

        # 3) 위젯에 출력
        self.priceview.setChart(self.lineChart)
        self.priceview.setRenderHint(QPainter.Antialiasing)


        self.worker = Worker()
        self.worker.dataSent.connect(self.updateData)
        self.worker.start()

        self.idx = 0
        self.viewlimit = 30

    def updateData(self, price):
        if self.idx > self.viewlimit:
            self.chartData.remove(0)

        self.chartData.append(self.idx, price)
        self.idx += 1

        pvs = self.chartData.pointsVector()
        x = pvs[0].x()

        ax = self.lineChart.axisX()
        ax.setRange(x, x + self.viewlimit - 1)

        ay = self.lineChart.axisY()
        dataY = [p.y() for p in pvs]
        ay.setRange(min(dataY), max(dataY))


if __name__ == "__main__":
    app = QApplication([])
    chart = ChartWidget()
    chart.show()
    app.exec_()
