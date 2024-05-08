# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistrazioneView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Controller.ControllerAutenticazione import ControllerAutenticazione
from View import LandingPageUtenteView

class RegistrazioneView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.RegistrazioneButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegistrazioneButton.setGeometry(QtCore.QRect(320, 490, 150, 30))
        self.RegistrazioneButton.setObjectName("RegistrazioneButton")
        self.RegistrazioneButton.clicked.connect(self.goProceduraRegistrazione)

        self.UsernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(150, 390, 491, 30))
        self.UsernameInput.setObjectName("UsernameInput")

        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(150, 440, 491, 30))
        self.PasswordInput.setObjectName("PasswordInput")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(140, 200, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setObjectName("label1")
        self.EmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(150, 340, 491, 30))
        self.EmailInput.setObjectName("EmailInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RegistrazioneButton.setText(_translate("MainWindow", "Registrazione"))
        self.UsernameInput.setText(_translate("MainWindow", ""))
        self.PasswordInput.setText(_translate("MainWindow", ""))
        self.UsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label1.setText(_translate("MainWindow", "Crea le tue Credenziali!"))
        self.EmailInput.setText(_translate("MainWindow", ""))
        self.EmailInput.setPlaceholderText(_translate("MainWindow", "Email"))

    def goProceduraRegistrazione(self):
        if self.UsernameInput.text() == "":
            usernameVuoto = QMessageBox()
            usernameVuoto.setWindowTitle("Errore!")
            usernameVuoto.setText("Nessun username inserito!")
            usernameVuoto.exec_()
            return
        if self.PasswordInput.text() == "":
            passwordVuoto = QMessageBox()
            passwordVuoto.setWindowTitle("Errore!")
            passwordVuoto.setText("Nessuna password inserita!")
            passwordVuoto.exec_()
            return 
        if self.EmailInput.text() == "":
            passwordVuoto = QMessageBox()
            passwordVuoto.setWindowTitle("Errore!")
            passwordVuoto.setText("Nessuna email inserita!")
            passwordVuoto.exec_()
            return 
        self.controllerAutenticazione = ControllerAutenticazione()
        registered = self.controllerAutenticazione.registrazione(self.UsernameInput.text(), self.PasswordInput.text(), self.EmailInput.text())
        if registered==True:
            registrazioneOK = QMessageBox()
            registrazioneOK.setWindowTitle("OK")
            registrazioneOK.setText("Registrazione effettuata con successo!")
            registrazioneOK.exec_()
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Registrazione non effettuata!")
            registrazioneNonOK.exec_()
            