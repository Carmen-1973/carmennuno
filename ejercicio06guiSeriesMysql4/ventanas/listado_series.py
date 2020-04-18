# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listado_series.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Yataghan")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 0);")
        self.label.setObjectName("label")
        self.listado_series = QtWidgets.QTextEdit(self.centralwidget)
        self.listado_series.setGeometry(QtCore.QRect(30, 120, 731, 441))
        font = QtGui.QFont()
        font.setFamily("Yataghan")
        font.setPointSize(12)
        self.listado_series.setFont(font)
        self.listado_series.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.listado_series.setObjectName("listado_series")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listado de Series"))
        self.label.setText(_translate("MainWindow", "LISTADO DE SERIES:"))
