from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
        
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            else:
                return txt_res5
        if int(self.exp.age) <= 14 and int(self.exp.age) >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.5 and self.index>=12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            else:
                return txt_res5
        if int(self.exp.age) <= 12 and int(self.exp.age) >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index<18 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            else:
                return txt_res5
        if int(self.exp.age) <= 10 and int(self.exp.age) >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<19.5 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            else:
                return txt_res5
        if int(self.exp.age) <= 8 and int(self.exp.age) >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index<21 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            else:
                return txt_res5

    def initUI(self):
        self.lbl_workheart=QLabel(txt_workheart + str(self.results()))
        self.lbl_index=QLabel(txt_index + str(self.index))
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
