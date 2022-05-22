from PyQt5.QtCore import Qt
from final_win import TestWin
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        self.lbl_index=QLabel(txt_index)
        self.lbl_workheart=QLabel(txt_workheart)
        self.vlayout_main=QVBoxLayout()
        self.vlayout_main.addWidget(self.lbl_index, alignment = Qt.AlignCenter)
        self.vlayout_main.addWidget(self.lbl_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.vlayout_main)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

if __name__ == '__main__':
    app = QApplication([])
    mw = FinalWin()
    app.exec_()
