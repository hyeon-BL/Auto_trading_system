from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("1000", self) # 그냥 변수, SELF를 넣어야 인스턴스 변수로 사용 가능

        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        print("timeout")

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()