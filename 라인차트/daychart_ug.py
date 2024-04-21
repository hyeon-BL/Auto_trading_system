import pyupbit
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/라인차트/chart.ui",self)

        # 1) 데이터 추가
        self.chartData = QLineSeries()
        df = pyupbit.get_ohlcv("KRW-BTC", interval="day")
        print(df.loc["2023", "close"])

        for i in range(len(df.loc["2023","close"])):
            self.chartData.append(i, df.loc["2023", "close"][i])

        # 2) 도화지 연결
        self.lineChart = QChart()
        self.lineChart.addSeries(self.chartData)
        self.lineChart.legend().hide()
        self.lineChart.layout().setContentsMargins(0, 0, 0, 0)

        ax = QValueAxis()
        ax.setRange(0, len(df.loc["2023","close"]))


        data = self.chartData.pointsVector()
        dataY = [p.y() for p in data]

        ay = QValueAxis()
        ay.setRange(min(dataY),max(dataY))
        self.lineChart.addAxis(ay, Qt.AlignLeft)

        # 3) 위젯에 출력
        self.priceview.setChart(self.lineChart)
        self.priceview.setRenderHint(QPainter.Antialiasing)

if __name__ == "__main__":
    app = QApplication([])
    chart = ChartWidget()
    chart.show()
    app.exec_()
