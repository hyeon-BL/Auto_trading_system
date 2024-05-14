from PyQt5.QtWidgets import QApplication, QLabel


# Create an application
app = QApplication([])
label = QLabel('Hello World!')
label.show()


app.exec_()