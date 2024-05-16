# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AggiungiTestView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controller.ControllerTest import ControllerTest


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
        self.NomeTestInput.setGeometry(QtCore.QRect(150, 350, 491, 30))
        self.NomeTestInput.setObjectName("UsernameInput")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(130, 230, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(135, 365, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setAcceptDrops(False)
        self.label2.setObjectName("label2")

        self.contenutoTextInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.contenutoTextInput.setGeometry(QtCore.QRect(150, 440, 491, 131))
        self.contenutoTextInput.setObjectName("contenutoTextInput")

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
        self.NomeTestInput.setText(_translate("MainWindow", ""))
        self.NomeTestInput.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.label1.setText(_translate("MainWindow", "Aggiungi il nuovo Test!"))
        self.contenutoTextInput.setPlainText(_translate("MainWindow", ""))
        self.label2.setText(_translate("MainWindow", "Ricordati di separare ogni parola con il carattere ,"))


    def actionAggiungiTest(self):
        self.controllaCampoNomeTestNonVuoto()
        self.controllaCampoContenutoTestNonVuoto()
        
        self.controllerTest = ControllerTest()
        self.added = self.controllerTest.aggiungiTest(self.NomeTestInput.text(), self.contenutoTextInput.text())

        self.controllaAggiuntaTestConSuccesso()
        
    def controllaCampoNomeTestNonVuoto(self):
        if self.NomeTestInput.text() == "":
            NomeTestVuoto = QMessageBox()
            NomeTestVuoto.setWindowTitle("Errore!")
            NomeTestVuoto.setText("Nessun nome inserito!")
            NomeTestVuoto.exec_()

    def controllaCampoContenutoTestNonVuoto(self):
        if self.contenutoTextInput.text() == "":
            contenutoTestVuoto = QMessageBox()
            contenutoTestVuoto.setWindowTitle("Errore!")
            contenutoTestVuoto.setText("Nessun contenuto inserito!")
            contenutoTestVuoto.exec_()
        
    def controllaAggiuntaTestConSuccesso(self):
        if self.added==True:
            registrazioneOK = QMessageBox()
            registrazioneOK.setWindowTitle("OK")
            registrazioneOK.setText("Test aggiunto con successo!")
            registrazioneOK.exec_()
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Test non aggiunto!")
            registrazioneNonOK.exec_()

