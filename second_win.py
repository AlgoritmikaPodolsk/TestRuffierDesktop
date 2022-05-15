from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)




class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(1000, 600)
        self.move(200, 100)
    def initUI(self):
        self.txt_name = QLabel(txt_name)
        self.input_name = QLineEdit(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.input_age = QLineEdit(txt_hintage)
        self.txt_test1 = QLabel(txt_test1)
        self.test_button1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.test_button2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.test_button3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.input_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.input_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test_button1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test_button2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test_button3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest3, alignment = Qt.AlignLeft)
        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)
    def connects(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    main_win = TestWin()
    app.exec_()
