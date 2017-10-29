# -*- coding: utf-8 -*-

import sys
import os.path

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from LogForm import Ui_winMain
import tblDataForm
import cx_Oracle

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

sql = 'select country_id, country_name from countries'

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_winMain()
        self.ui.setupUi(self)

        self.ui.btnGen.clicked.connect(self.genData)
        #self.ui.btnGen.clicked.connect(DataForm())

    def genData(self):
        #print(self.ui.eSrc.toPlainText().toUtf8())
        self.parse_data()
        #sql = 'select country_id, country_name from countries'
        #mf = tblDataForm.MainForm()
        #mf.show()
        #tblDataForm.show_select('select country_id, country_name from countries')
        # SELECT

        for k,v in self.d_sel.items():
            global sql
            sql = v
            mf = DataForm()


    def parse_data(self):
        """
            Parse text on items
        """
        d = dict()
        text = str(self.ui.eSrc.toPlainText().toUtf8()).split('\n')
        n = 0
        s_add = ""
        flag = ""
        for i in range(len(text)):
            s = text[i].strip()

            if s.startswith('SEL'):
                s_add = s_add + " " + s
                flag = "sel"
                continue
            if s.find('параметр')>0:
                if not flag == '':
                    n += 1
                    d[n] = [flag, s_add]
                    flag = ''
                    s_add = ''
                s_add = s
                flag = "par"
                n += 1
                val = s_add.rpartition(' ')[-1]
                d[n] = [flag, val]
                flag = ""
                s_add = ""
                continue
            if s.find('прав')>0:
                if not flag == '':
                    n += 1
                    d[n] = [flag, s_add]
                    flag = ''
                    s_add = ''
                s_add = s
                s_add = s
                flag = "righ"
                n += 1
                val = s_add.rpartition(' ')[-1]
                d[n] = [flag, val]
                flag = ""
                s_add = ""
                continue
            if s.startswith('CALL'):
                if not flag == '':
                    n += 1
                    d[n] = [flag, s_add]
                    flag = ''
                    s_add = ''
                s_add = s[5:]
                flag = "func"
                continue
            if s.startswith('EXECUTE'):
                if not flag == '':
                    n += 1
                    d[n] = [flag, s_add]
                    flag = ''
                    s_add = ''
                s_add = s[8:]
                flag = "proc"
                continue
            if s == "" or s == "\n":
                n += 1
                d[n] = [flag, s_add]
                flag = ""
                s_add = ""
                continue
            if str(s[0]).isdigit():
                if not flag == '':
                    n += 1
                    d[n] = [flag, s_add]
                    flag = ''
                    s_add = ''
                continue
            else:
                s_add = s_add + " " + s
        self.d_param = dict()
        self.d_right = dict()
        self.d_proc = dict()
        self.d_func = dict()
        self.d_sel = dict()
        for k, v in d.items():
            if v[0] == 'sel':
                self.d_sel[len(self.d_sel)+1] = v[1]
            if v[0] == 'par':
                self.d_param[len(self.d_param)+1] = v[1]
            if v[0] == 'righ':
                self.d_right[len(self.d_right)+1] = v[1]
            if v[0] == 'proc':
                self.d_proc[len(self.d_proc)+1] = v[1]
            if v[0] == 'func':
                self.d_func[len(self.d_func)+1] = v[1]
        print('test')


class Ui_Form(object):
    def setupUi(self, Form):
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
        global sql
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
    i_1 = sql.index('SELECT') + 7
    i_2 = sql.index('FROM')
    l = sql[i_1:i_2].split(',')
    l_res = list()
    for i in range(len(l)):
        l_res.append(l[i].strip())
    return l_res


class DataForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def __call__(self, Form):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())


