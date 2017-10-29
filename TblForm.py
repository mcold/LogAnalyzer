# -*- coding: UTF-8 -*-
import sys
import os.path
from PyQt4 import QtCore, QtGui
from sqlalchemy import create_engine


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

class _db():
    def __init__(self):
        self.engine = create_engine('oracle+cx_oracle://system:15151@127.0.0.1:1521/sidname')

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TblForm()
        self.ui.setupUi(self)


class Ui_TblForm(object):
    def setupUi(self, winMain):
        winMain.resize(500, 500)
#        self.centralwidget = QtGui.QWidget(winMain)
        # create table

        tblData = QtGui.QTableWidget()
        tblData.setGeometry(QtCore.QRect(20, 20, 400, 400))
        # change
        tblData.setColumnCount(3)
        tblData.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        tblData.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        tblData.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        tblData.setHorizontalHeaderItem(2, item)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addItem(tblData)
        self.setLayout(vbox)

        #self.retranslateUi(winMain)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        winMain.setWindowTitle(_translate("winMain", "LogAnalyzer", None))
        item = self.tblData.horizontalHeaderItem(0)
        item.setText(_translate("winMain", "Num", None))
        item = self.tblData.horizontalHeaderItem(1)
        item.setText(_translate("winMain", "Param", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
