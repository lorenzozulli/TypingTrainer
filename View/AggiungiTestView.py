# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AggiungiTestView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class AggiungiTestView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AggiungiTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.AggiungiTestButton.setGeometry(QtCore.QRect(310, 590, 150, 30))
        self.AggiungiTestButton.setObjectName("AggiungiTestButton")
        self.AggiungiTestButton.clicked.connect(self.actionAggiungiTest)
        self.NomeTestInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NomeTestInput.setGeometry(QtCore.QRect(150, 390, 491, 30))
        self.NomeTestInput.setObjectName("UsernameInput")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(130, 230, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setObjectName("label1")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 440, 491, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AggiungiTestButton.setText(_translate("MainWindow", "Aggiungi"))
        self.NomeTestInput.setText(_translate("MainWindow", "Nome"))
        self.label1.setText(_translate("MainWindow", "Aggiungi il nuovo Test!"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Ricordati di separare ogni parola con il carattere ,"))

    def actionAggiungiTest(self):
        if self.NomeTestInput.text() == "":
            NomeTestVuoto = QMessageBox()
            NomeTestVuoto.setWindowTitle("Errore!")
            NomeTestVuoto.setText("Nessun nome inserito!")
            NomeTestVuoto.exec_()
            return
        if self.plainTextEdit.text() == "":
            contenutoTestVuoto = QMessageBox()
            contenutoTestVuoto.setWindowTitle("Errore!")
            contenutoTestVuoto.setText("Nessun contenuto inserito!")
            contenutoTestVuoto.exec_()
            return
        '''
        self.controllerTest = ControllerTest()
        added = self.controllerTest.aggiungiTest(self.NomeTestInput.text(), self.plainTextEdit.text()) 
        '''