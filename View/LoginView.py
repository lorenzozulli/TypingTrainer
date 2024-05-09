# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from View.RegistrazioneView import RegistrazioneView
from View.RecuperaPasswordView import RecuperaPasswordView
from View.LandingPageUtenteView import LandingPageUtenteView
from View.LandingPageAdminView import LandingPageAdminView

from Controller.ControllerAutenticazione import ControllerAutenticazione

class LoginView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogInButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInButton.setGeometry(QtCore.QRect(150, 490, 150, 30))
        self.LogInButton.setObjectName("LogInButton")
        self.LogInButton.clicked.connect(self.goLogin)

        self.RegistrazioneButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegistrazioneButton.setGeometry(QtCore.QRect(320, 490, 150, 30))
        self.RegistrazioneButton.setObjectName("RegistrazioneButton")
        self.RegistrazioneButton.clicked.connect(self.goRegistrazione)

        self.RecuperaPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecuperaPasswordButton.setGeometry(QtCore.QRect(490, 490, 150, 30))
        self.RecuperaPasswordButton.setObjectName("RecuperaPasswordButton")
        self.RecuperaPasswordButton.clicked.connect(self.goRecuperaPassword)
        
        self.UsernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(150, 390, 491, 30))
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(150, 440, 491, 30))
        self.PasswordInput.setObjectName("PasswordInput")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(80, 240, 631, 121))
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
        self.LogInButton.setText(_translate("MainWindow", "LogIn"))
        self.RegistrazioneButton.setText(_translate("MainWindow", "Registrazione"))
        self.RecuperaPasswordButton.setText(_translate("MainWindow", "Recupera Password"))
        self.UsernameInput.setText(_translate("MainWindow", ""))
        self.UsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label1.setText(_translate("MainWindow", "Benvenuto in Typing Trainer!"))

    def goRegistrazione(self):
        self.registrazione = QtWidgets.QMainWindow()
        self.ui = RegistrazioneView()
        self.ui.setupUi(self.registrazione)
        self.registrazione.show()

    def goRecuperaPassword(self):
        self.recuperaPassword = QtWidgets.QMainWindow()
        self.ui = RecuperaPasswordView()
        self.ui.setupUi(self.recuperaPassword)
        self.recuperaPassword.show()
    
    def goLogin(self):
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
        
        self.controllerAutenticazione = ControllerAutenticazione()
        loginResult = self.controllerAutenticazione.logIn(self.UsernameInput.text(), self.PasswordInput.text())
        match loginResult[0]:
            case "Admin":
                self.authorizedAdmin = QtWidgets.QMainWindow()
                self.ui = LandingPageAdminView()
                self.ui.setupUi(self.authorizedAdmin, loginResult[1])
                self.authorizedAdmin.show()
            case "Utente":
                self.authorizedUtente = QtWidgets.QMainWindow()
                self.ui = LandingPageUtenteView()
                self.ui.setupUi(self.authorizedUtente, loginResult[1])
                self.authorizedUtente.show()
            case "PasswordErrata":
                popup = QMessageBox()
                popup.setText("Password errata")
                popup.setWindowTitle("Errore!")
                popup.exec_()
            case "UsernameNonTrovato":
                popup = QMessageBox()
                popup.setText("Nome utente non trovato")
                popup.setWindowTitle("Errore!")
                popup.exec_()
