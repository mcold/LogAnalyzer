# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogForm.ui'
#
# Created: Sat Oct 28 14:43:45 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName(_fromUtf8("winMain"))
        winMain.resize(958, 555)
        self.centralwidget = QtGui.QWidget(winMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.eSrc = QtGui.QTextEdit(self.centralwidget)
        self.eSrc.setGeometry(QtCore.QRect(10, 49, 400, 301))
        self.eSrc.setObjectName(_fromUtf8("eSrc"))
        self.btnGen = QtGui.QPushButton(self.centralwidget)
        self.btnGen.setGeometry(QtCore.QRect(10, 0, 121, 41))
        self.btnGen.setObjectName(_fromUtf8("btnGen"))
        self.tblParams = QtGui.QTableWidget(self.centralwidget)
        self.tblParams.setGeometry(QtCore.QRect(420, 50, 531, 161))
        self.tblParams.setObjectName(_fromUtf8("tblParams"))
        self.tblParams.setColumnCount(3)
        self.tblParams.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblParams.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblParams.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblParams.setHorizontalHeaderItem(2, item)
        self.tblRights = QtGui.QTableWidget(self.centralwidget)
        self.tblRights.setGeometry(QtCore.QRect(420, 220, 531, 131))
        self.tblRights.setObjectName(_fromUtf8("tblRights"))
        self.tblRights.setColumnCount(3)
        self.tblRights.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblRights.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblRights.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblRights.setHorizontalHeaderItem(2, item)
        self.tblCalls = QtGui.QTableWidget(self.centralwidget)
        self.tblCalls.setGeometry(QtCore.QRect(10, 360, 401, 121))
        self.tblCalls.setObjectName(_fromUtf8("tblCalls"))
        self.tblCalls.setColumnCount(3)
        self.tblCalls.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblCalls.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblCalls.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblCalls.setHorizontalHeaderItem(2, item)
        self.tblParamCalls = QtGui.QTableWidget(self.centralwidget)
        self.tblParamCalls.setGeometry(QtCore.QRect(420, 360, 531, 121))
        self.tblParamCalls.setObjectName(_fromUtf8("tblParamCalls"))
        self.tblParamCalls.setColumnCount(2)
        self.tblParamCalls.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblParamCalls.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblParamCalls.setHorizontalHeaderItem(1, item)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.eUID = QtGui.QLineEdit(self.centralwidget)
        self.eUID.setGeometry(QtCore.QRect(470, 17, 61, 20))
        self.eUID.setAlignment(QtCore.Qt.AlignCenter)
        self.eUID.setObjectName(_fromUtf8("eUID"))
        self.lResult = QtGui.QLabel(self.centralwidget)
        self.lResult.setGeometry(QtCore.QRect(420, 490, 241, 20))
        self.lResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lResult.setObjectName(_fromUtf8("lResult"))
        self.lFIO = QtGui.QLabel(self.centralwidget)
        self.lFIO.setGeometry(QtCore.QRect(560, 18, 241, 16))
        self.lFIO.setAlignment(QtCore.Qt.AlignCenter)
        self.lFIO.setObjectName(_fromUtf8("lFIO"))
        winMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(winMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        winMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(winMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        winMain.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(winMain)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExport = QtGui.QAction(winMain)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionExit = QtGui.QAction(winMain)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(winMain)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        winMain.setWindowTitle(_translate("winMain", "LogAnalyzer", None))
        self.btnGen.setText(_translate("winMain", "Generate", None))
        item = self.tblParams.horizontalHeaderItem(0)
        item.setText(_translate("winMain", "Num", None))
        item = self.tblParams.horizontalHeaderItem(1)
        item.setText(_translate("winMain", "Param", None))
        item = self.tblParams.horizontalHeaderItem(2)
        item.setText(_translate("winMain", "Value", None))
        item = self.tblRights.horizontalHeaderItem(0)
        item.setText(_translate("winMain", "Num", None))
        item = self.tblRights.horizontalHeaderItem(1)
        item.setText(_translate("winMain", "Right", None))
        item = self.tblRights.horizontalHeaderItem(2)
        item.setText(_translate("winMain", "Value", None))
        item = self.tblCalls.horizontalHeaderItem(0)
        item.setText(_translate("winMain", "Type", None))
        item = self.tblCalls.horizontalHeaderItem(1)
        item.setText(_translate("winMain", "Call", None))
        item = self.tblCalls.horizontalHeaderItem(2)
        item.setText(_translate("winMain", "Comment", None))
        item = self.tblParamCalls.horizontalHeaderItem(0)
        item.setText(_translate("winMain", "SysName", None))
        item = self.tblParamCalls.horizontalHeaderItem(1)
        item.setText(_translate("winMain", "Value", None))
        self.label.setText(_translate("winMain", "UserID", None))
        self.lResult.setText(_translate("winMain", "Result", None))
        self.lFIO.setText(_translate("winMain", "FIO Person", None))
        self.menuFile.setTitle(_translate("winMain", "File", None))
        self.menuAbout.setTitle(_translate("winMain", "About", None))
        self.actionImport.setText(_translate("winMain", "Import", None))
        self.actionExport.setText(_translate("winMain", "Export", None))
        self.actionExit.setText(_translate("winMain", "Exit", None))
