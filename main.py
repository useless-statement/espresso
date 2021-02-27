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


class AddForm(QWidget):
    def __init__(self, id=-1):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
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
