# import data
# from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
# import sys
# from PyQt6.QtGui import QIcon
# from PyQt6 import QtCore
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setWindowTitle("MyWindow")
#     win.setGeometry(500,400,500,400)
#     win.setWindowIcon(QIcon("C:\\Users\\User\\Desktop\\PYTHON\\13.2.2023\\icon\\calculator.png"))
#     # win.setFixedSize(400,400)
#     # win.setWindowOpacity(0.6)
#     style = """
#     background:no-repeat url('C:/Users/User/Desktop/PYTHON/13.2.2023/icon/123.jpg');
#     """
#     win.setStyleSheet(style)
#     # win.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
#     win.show()
#     app.exec()
# 2-qism mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from window.window import Mywindow,QApplication
import sys
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Mywindow(600,600,'My_Project')
    win.show()
    app.exec()