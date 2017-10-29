# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tblDataForm.ui'
#
# Created: Sat Oct 28 15:48:13 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
import sys
import os.path
from PyQt4 import QtCore, QtGui
import cx_Oracle

#sql = "select country_id, country_name, region_id, test from countries"
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form, sql="select country_id, country_name, region_id, test from countries"):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 219)
        self.tblData = QtGui.QTableWidget(Form)
        self.tblData.setGeometry(QtCore.QRect(10, 10, 371, 192))
        self.tblData.setObjectName(_fromUtf8("tblData"))
        self.tblData.setColumnCount(0)
        self.tblData.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        """
        try:
            sql = sys.argv[1]
        except:
            sql = "select country_id, country_name, region_id, test from countries"
        """
        # take columns from sql
        l_cols = parse_column(sql)
        # add columns to table

        self.tblData.setColumnCount(len(l_cols))
        #            self.tblParams.setRowCount(0)
        for i in range(len(l_cols)):
            item = QtGui.QTableWidgetItem(l_cols[i])
            self.tblData.setHorizontalHeaderItem(i, item)
        self.tblData.setRowCount(len(l_cols))


        con = cx_Oracle.connect('system/15151@127.0.0.1/XE')
        cur = con.cursor()
        l_data = get_data(sql, cur)



        self.tblData.setRowCount(len(l_data))
        for i in range(len(l_data)):
            for j in range(len(l_data[i])):
                test = l_data[i][j]

                try:
                    if str(test).isdigit() and not type(test) == unicode:
                        s = test
                    else:
                        s = test.encode('utf-8')
                except:
                    s = test

                self.tblData.setItem(i, j, QtGui.QTableWidgetItem(s))

        cur.execute(sql)

        cur.close()
        con.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Data", None))

def get_data(sql, cur):
    """
        Receive data from DataBase
        params: sql - select-query
                cur - cx_Oracle cursor
    """
    cur.execute(sql)
    l_d = cur.fetchall()
    l = list()
    for i in range(len(l_d)):
        ss = list()
        for j in range(len(l_d[i])):
            test = l_d[i][j]
            try:
                test = test.decode('cp1251')
            except:
                pass
            ss.append(test)

        l.append(ss)
    return l



def parse_column(sql):
    ### TODO: if sql is None take metadata of table
    ### TODO: split sql on sequence of selects
    i_1 = sql.index('select') + 7
    i_2 = sql.index('from')
    l = sql[i_1:i_2].split(',')
    l_res = list()
    for i in range(len(l)):
        l_res.append(l[i].strip())
    return l_res

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None, sql="select country_id, country_name, region_id, test from countries"):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self, sql)

    def __call__(self, Form):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        """Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 219)
        QtGui.QWidget.__init__(Form)
        self.ui = Ui_Form()
        Form.setObjectName(_fromUtf8("Form"))
        self.resize(400, 219)
        self.tblData = QtGui.QTableWidget(self)
        self.tblData.setGeometry(QtCore.QRect(10, 10, 371, 192))
        self.tblData.setObjectName(_fromUtf8("tblData"))
        self.tblData.setColumnCount(0)
        self.tblData.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        try:
            sql = sys.argv[1]
        except:
            sql = "select country_id, country_name, region_id, test from countries"
        

        # take columns from sql
        l_cols = parse_column(sql)
        # add columns to table

        self.tblData.setColumnCount(len(l_cols))
        #            self.tblParams.setRowCount(0)
        for i in range(len(l_cols)):
            item = QtGui.QTableWidgetItem(l_cols[i])
            self.tblData.setHorizontalHeaderItem(i, item)
        self.tblData.setRowCount(len(l_cols))

        con = cx_Oracle.connect('system/15151@127.0.0.1/XE')
        cur = con.cursor()
        l_data = get_data(sql, cur)

        self.tblData.setRowCount(len(l_data))
        for i in range(len(l_data)):
            for j in range(len(l_data[i])):
                test = l_data[i][j]

                try:
                    if str(test).isdigit() and not type(test) == unicode:
                        s = test
                    else:
                        s = test.encode('utf-8')
                except:
                    s = test

                self.tblData.setItem(i, j, QtGui.QTableWidgetItem(s))

        cur.execute(sql)

        cur.close()
        con.close()
        """
        self.show()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Data", None))

def show_select(sql):
    """
        Show window with data source
    :param sql:
    :return:
    """
    app = QtGui.QApplication(sys.argv)
    mf = MainForm()
    mf.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())

    # show_select("select country_id, country_name, region_id, test from countries")