import pyupbit
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime, Qt, QThread, pyqtSignal
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

        ax = QDateTimeAxis()
        ax.setFormat("hh:mm:ss")
        ax.setTickCount(4)
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

        self.viewlimit = 30

    def updateData(self, price):
        if len(self.chartData) > self.viewlimit:
            self.chartData.remove(0)

        curr = QDateTime.currentDateTime()
        self.chartData.append(curr.toMSecsSinceEpoch(), price)

        pvs = self.chartData.pointsVector()
        x = pvs[0].x()

        s = QDateTime.fromMSecsSinceEpoch(int(x))
        e = s.addSecs(self.viewlimit)

        ax = self.lineChart.axisX()
        ax.setRange(s, e)

        ay = self.lineChart.axisY()
        dataY = [p.y() for p in pvs]

        minval = min(dataY)
        maxval = max(dataY)
        margin = (maxval - minval) * 0.2

        ay.setRange(minval - margin, maxval + margin)


if __name__ == "__main__":
    app = QApplication([])
    chart = ChartWidget()
    chart.show()
    app.exec_()
