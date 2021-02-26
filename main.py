import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5 import uic


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        info = cur.execute("select * from main").fetchall()
        self.tw.setRowCount(len(info))
        j = 0
        for i in range(len(info)):
            if info[i][6] != 1:
                self.tw.setItem(j, 0, QTableWidgetItem(str(info[i][0])))
                self.tw.setItem(j, 1, QTableWidgetItem(info[i][1]))
                self.tw.setItem(j, 2, QTableWidgetItem(info[i][2]))
                self.tw.setItem(j, 3, QTableWidgetItem("в зернах" if info[i][3] == 0 else "молотый"))
                self.tw.setItem(j, 4, QTableWidgetItem(info[i][4]))
                self.tw.setItem(j, 5, QTableWidgetItem(str(info[i][5])))
                self.tw.setItem(j, 6, QTableWidgetItem(str(info[i][6])))
                j += 1


if __name__ == '__main__':
    con = sqlite3.connect("coffee.sqlite")
    cur = con.cursor()
    app = QApplication(sys.argv)

    ex = mw()
    ex.show()
    sys.exit(app.exec_())
