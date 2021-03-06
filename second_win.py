from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)


class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
        
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
        self.send_button = QPushButton(txt_sendresults)
        self.txt_timer = QLabel(txt_timer)
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
        self.l_line.addWidget(self.send_button, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.txt_timer, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        txt_timer = str(self.timer)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
        txt_timer = str(self.timer)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
        txt_timer = str(self.timer)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.txt_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def connects(self):
        self.test_button1.clicked.connect(self.timer_test)
        self.test_button2.clicked.connect(self.timer_sits)
        self.test_button3.clicked.connect(self.timer_final)
        self.send_button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.input_age.text(), self.txt_hinttest1.text(), self.txt_hinttest2.text(), self.txt_hinttest3.text())
        self.tw = FinalWin(self.exp)
if __name__ == "__main__":
    app = QApplication([])
    main_win = TestWin()
    app.exec_()
