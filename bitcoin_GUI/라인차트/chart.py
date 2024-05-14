from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/i4u11/Desktop/Work/Auto_trading_system/라인차트/chart.ui",self)

        # 1) 데이터 추가
        self.chartData = QLineSeries()
        self.chartData.append(0, 6)
        self.chartData.append(2, 4)

        # 2) 도화지 연결
        self.lineChart = QChart()
        self.lineChart.addSeries(self.chartData)
        self.lineChart.legend().hide()
        self.lineChart.layout().setContentsMargins(0, 0, 0, 0)

        # 3) 위젯에 출력
        self.priceview.setChart(self.lineChart)
        self.priceview.setRenderHint(QPainter.Antialiasing)

if __name__ == "__main__":
    app = QApplication([])
    chart = ChartWidget()
    chart.show()
    app.exec_()