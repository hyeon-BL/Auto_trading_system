from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        text = QTextEdit(self) # QTextEdit은 여러 줄의 텍스트를 입력할 수 있는 위젯 QlineEdit은 한 줄만 입력 가능
        text.setText('Hello, World!')
        text.append('append는 문자열을 추가하는 메소드입니다.')

        # text.move(10, 10)
        # text.resize(380, 300)
        text.setGeometry(10, 10, 380, 300) # 같은 역할

        self.resize(400, 320)

if __name__ == '__main__':
    app = QApplication([])
    label = MyMainWindow()
    label.show()
    app.exec_()