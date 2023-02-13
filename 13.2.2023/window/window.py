from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QTextEdit
from PyQt6 import QtCore
class Mywindow(QMainWindow):
    def __init__(self, width=500, height=500, title="Qt") -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(250,250,width, height)
        self.main_btn = QPushButton("Javob",self)
        self.main_lbl =QLabel("<b> Assolomu alaykum</b>",self)
        self.main_btn.setGeometry(width//2,height//2, 105, 50)
        self.main_btn.adjustSize()
        self.main_lbl.setGeometry(width//2,height//2-95,105,105)
        self.main_lbl.adjustSize()
        self.main_btn.clicked.connect(self.change_lable_text)
    def change_lable_text(self):
        self.main_lbl.setText("<b> Va alaykum assalom </b>") 