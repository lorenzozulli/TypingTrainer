# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificaUtenteView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Controller.ControllerUtente import ControllerUtente


class ModificaUtenteView(object):
    def setupUi(self, MainWindow, utenteDaModificare):
        self.utenteDaModificare = utenteDaModificare

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.ModificaButton = QtWidgets.QPushButton(self.centralwidget)
        self.ModificaButton.setGeometry(QtCore.QRect(320, 490, 150, 30))
        self.ModificaButton.setObjectName("ModificaButton")
        self.ModificaButton.clicked.connect(self.actionModificaUtente)

        self.UsernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(150, 390, 491, 30))
        self.UsernameInput.setObjectName("UsernameInput")

        self.EmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(150, 440, 491, 30))
        self.EmailInput.setObjectName("emailInput")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(150, 240, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ModificaButton.setText(_translate("MainWindow", "Modifica"))
        self.UsernameInput.setText(_translate("MainWindow", self.utenteDaModificare.getUsername()))
        self.EmailInput.setText(_translate("MainWindow", self.utenteDaModificare.getEmail()))
        self.label1.setText(_translate("MainWindow", "Modifica le credenziali!"))

    def actionModificaUtente(self):
        self.controllaCampoUsernameNonVuoto()
        self.controllaCampoEmailNonVuoto()

        self.controllerUtente = ControllerUtente()
        self.modified = self.controllerUtente.modificaUtente(self.utenteDaModificare.getIdentifier(), self.UsernameInput.text(), self.EmailInput.text())

        self.controllaUtenteModificatoConSuccesso()
    
    def controllaCampoUsernameNonVuoto(self):
        if self.UsernameInput.text() == "":
            UsernameVuoto = QMessageBox()
            UsernameVuoto.setWindowTitle("Errore!")
            UsernameVuoto.setText("Nessun Username inserito!")
            UsernameVuoto.exec_()
            return

    def controllaCampoEmailNonVuoto(self):
        if self.EmailInput.text() == "":
            EmailVuoto = QMessageBox()
            EmailVuoto.setWindowTitle("Errore!")
            EmailVuoto.setText("Nessuna Email inserita!")
            EmailVuoto.exec_()
            return

    def controllaUtenteModificatoConSuccesso(self):
        if self.modified==True:
            modificaOK = QMessageBox()
            modificaOK.setWindowTitle("OK")
            modificaOK.setText("Modifica effettuata con successo!")
            modificaOK.exec_()
        else:
            modificaNonOK = QMessageBox()
            modificaNonOK.setWindowTitle("Errore!")
            modificaNonOK.setText("Modifica non effettuata!")
            modificaNonOK.exec_() 

