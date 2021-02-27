import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 793)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tw = QtWidgets.QTableWidget(self.centralwidget)
        self.tw.setGeometry(QtCore.QRect(10, 0, 781, 681))
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(7)
        self.tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(6, item)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(690, 710, 93, 28))
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 720, 461, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "сорт"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "обжарка"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "молотый/в зернах"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "описание вкуса"))
        item = self.tw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "цена (руб.)"))
        item = self.tw.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "объем упаковки (г)"))
        self.btn.setText(_translate("MainWindow", "Новый пункт"))
        self.label.setText(_translate("MainWindow", "Чтобы редактировать пункт меню дважды щелкните по нужной строке."))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 722)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setGeometry(QtCore.QRect(10, 40, 681, 22))
        self.le_name.setObjectName("le_name")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_type = QtWidgets.QLineEdit(Form)
        self.le_type.setGeometry(QtCore.QRect(10, 100, 681, 22))
        self.le_type.setObjectName("le_type")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cb = QtWidgets.QComboBox(Form)
        self.cb.setGeometry(QtCore.QRect(200, 130, 111, 22))
        self.cb.setObjectName("cb")
        self.cb.addItem("")
        self.cb.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.le_taste = QtWidgets.QLineEdit(Form)
        self.le_taste.setGeometry(QtCore.QRect(10, 200, 681, 61))
        self.le_taste.setObjectName("le_taste")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 661, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.le_price = QtWidgets.QLineEdit(Form)
        self.le_price.setGeometry(QtCore.QRect(10, 290, 681, 22))
        self.le_price.setObjectName("le_price")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 681, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.le_package = QtWidgets.QLineEdit(Form)
        self.le_package.setGeometry(QtCore.QRect(10, 350, 681, 22))
        self.le_package.setObjectName("le_package")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(600, 680, 93, 28))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(500, 680, 93, 28))
        self.btn_ok.setObjectName("btn_ok")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 680, 481, 21))
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(130, 270, 271, 16))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(220, 320, 271, 16))
        self.label_9.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "сорт кофе"))
        self.label.setText(_translate("Form", "Введите название сорта кофе:"))
        self.label_2.setText(_translate("Form", "Введите степень/тип обжарки:"))
        self.label_3.setText(_translate("Form", "Выберите тип помола:"))
        self.cb.setItemText(0, _translate("Form", "В зернах"))
        self.cb.setItemText(1, _translate("Form", "Молотый"))
        self.label_4.setText(_translate("Form", "Введите краткое описание:"))
        self.label_5.setText(_translate("Form", "Введите цену:"))
        self.label_6.setText(_translate("Form", "Введите объем упаковки:"))
        self.btn_cancel.setText(_translate("Form", "Отмена"))
        self.btn_ok.setText(_translate("Form", "Сохранить"))
        self.label_7.setText(_translate("Form", "Все поля обязательны для ввода."))
        self.label_8.setText(_translate("Form", "Допускаются только цифры."))
        self.label_9.setText(_translate("Form", "Допускаются только цифры."))


class mw(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.open_add_form)
        self.show_table()
        self.tw.itemDoubleClicked.connect(self.open_add_form_with_id)

    def show_table(self):
        self.tw.clearContents()
        info = cur.execute("select * from main").fetchall()
        self.tw.setRowCount(len(info))
        j = 0
        for i in range(len(info)):
            self.tw.setItem(j, 0, QTableWidgetItem(str(info[i][0])))
            self.tw.setItem(j, 1, QTableWidgetItem(info[i][1]))
            self.tw.setItem(j, 2, QTableWidgetItem(info[i][2]))
            self.tw.setItem(j, 3, QTableWidgetItem("в зернах" if info[i][3] == 0 else "молотый"))
            self.tw.setItem(j, 4, QTableWidgetItem(info[i][4]))
            self.tw.setItem(j, 5, QTableWidgetItem(str(info[i][5])))
            self.tw.setItem(j, 6, QTableWidgetItem(str(info[i][6])))
            j += 1

    def open_add_form(self):
        self.add_form = AddForm()
        self.add_form.show()
        self.add_form.btn_ok.clicked.connect(self.show_table)

    def open_add_form_with_id(self):
        id = self.tw.item(self.sender().currentRow(), 0).text()
        # id = 1
        self.add_form = AddForm(id)
        self.add_form.show()
        self.add_form.btn_ok.clicked.connect(self.show_table)


class AddForm(QWidget, Ui_Form):
    def __init__(self, id=-1):
        super().__init__()
        self.setupUi(self)
        self.initUI(id)

    def initUI(self, id):
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.id = id
        self.btn_cancel.clicked.connect(self.close)
        if id != -1:
            self.set_info()
            self.btn_ok.clicked.connect(self.change_point)
        else:
            self.btn_ok.clicked.connect(self.new_point)

    def set_info(self):
        info = cur.execute(f"select * from main where id={self.id}").fetchall()[0]
        self.le_name.setText(info[1])
        self.le_type.setText(info[2])
        self.cb.setCurrentIndex(int(info[3]))
        self.le_taste.setText(info[4])
        self.le_price.setText(str(info[5]))
        self.le_package.setText(str(info[6]))

    def change_point(self):
        if self.check():
            name = self.le_name.text()
            roast = self.le_type.text()
            taste = self.le_taste.text()
            price = self.le_price.text()
            package = self.le_package.text()
            form = self.cb.currentIndex()
            print(self.id)
            cur.execute(
                f"update main set type='{name}', roast='{roast}', form={bool(form)}, taste='{taste}', price={price}, package={package} where id={self.id}")
            con.commit()
            self.close()

    def new_point(self):
        if self.check():
            name = self.le_name.text()
            roast = self.le_type.text()
            taste = self.le_taste.text()
            price = self.le_price.text()
            package = self.le_package.text()
            form = self.cb.currentIndex()
            cur.execute(f"""INSERT INTO main(type, roast, form, taste, price, package)
                                     VALUES('{name}', '{roast}', {bool(form)}, '{taste}', {price}, {package})""")
            con.commit()
            self.close()

    def check(self):
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        ok_name = self.check_name()
        ok_roast = self.check_roast()
        ok_taste = self.check_taste()
        ok_price = self.check_price()
        ok_package = self.check_package()
        if ok_name and ok_price and ok_roast and ok_taste and ok_package:
            return True
        return False

    def check_name(self):
        text = self.le_name.text()
        if text == '':
            self.label_7.show()
            return False
        return True

    def check_roast(self):
        text = self.le_type.text()
        if text == '':
            self.label_7.show()
            return False
        return True

    def check_taste(self):
        text = self.le_taste.text()
        if text == '':
            self.label_7.show()
            return False
        return True

    def check_price(self):
        text = self.le_price.text()
        if text == '':
            self.label_7.show()
            return False
        elif not text.isdigit():
            self.label_8.show()
            return False
        return True

    def check_package(self):
        text = self.le_package.text()
        if text == '':
            self.label_7.show()
            return False
        elif not text.isdigit():
            self.label_9.show()
            return False
        return True


if __name__ == '__main__':
    con = sqlite3.connect("coffee.sqlite")
    cur = con.cursor()
    app = QApplication(sys.argv)

    ex = mw()
    ex.show()
    sys.exit(app.exec_())
