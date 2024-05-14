from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton('1', self)
        btn2 = QPushButton('2', self)
        btn3 = QPushButton('3', self)
        btn4 = QPushButton('4', self)

        btn1.clicked.connect(self.btn_clicked)
        btn2.clicked.connect(self.btn_clicked)
        btn3.clicked.connect(self.btn_clicked)
        btn4.clicked.connect(self.btn_clicked)
        btn1.move(30, 30) # 왼쪽 위 모서리가 (0, 0)이다.
        btn2.move(130, 30)
        btn3.move(30, 60)
        btn4.move(130, 60)

        btn1.resize(100, 30)
        btn2.resize(100, 30)
        btn3.resize(100, 30)
        btn4.resize(100, 30)

        self.resize(260, 120)

    def btn_clicked(self):
        b = self.sender()
        print(b.text(),'button clicked')

if __name__ == '__main__':
    app = QApplication([])
    label = MyMainWindow()
    label.show()
    app.exec_()