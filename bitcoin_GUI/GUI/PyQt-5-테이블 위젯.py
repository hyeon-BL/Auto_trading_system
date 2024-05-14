from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        tw = QTableWidget(self)

        tw.setRowCount(5)
        tw.setColumnCount(3)

        tw.setHorizontalHeaderLabels(['금액', '잔고', '개수'])
        # v = tw.verticalHeader()
        # v.setVisible(False)
        tw.verticalHeader().setVisible(False) # 위와 같은 역할

        tw.setItem(0, 0, QTableWidgetItem('안녕'))
        tw.setItem(0, 1, QTableWidgetItem('HI'))

        tw.resize(400, 300)
        self.resize(400, 300)


if __name__ == '__main__':
    app = QApplication([])
    label = MyMainWindow()
    label.show()
    app.exec_()