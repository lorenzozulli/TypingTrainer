# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LandingPageAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from View.GestioneUtentiView import GestioneUtentiView
from View.GestioneTestView import GestioneTestView
from Model import Admin

from Controller import ControllerAutenticazione


class LandingPageAdminView(object):
    def setupUi(self, MainWindow, currentUtilizzatore):
        self.currentUtilizzatore = currentUtilizzatore

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.adminLabel = QtWidgets.QLabel(self.centralwidget)
        self.adminLabel.setGeometry(QtCore.QRect(140, 190, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.adminLabel.setFont(font)
        self.adminLabel.setObjectName("adminLabel")

        self.gestioneUtentiButton = QtWidgets.QPushButton(self.centralwidget)
        self.gestioneUtentiButton.setGeometry(QtCore.QRect(440, 210, 150, 30))
        self.gestioneUtentiButton.setObjectName("gestioneUtentiButton")
        self.gestioneUtentiButton.clicked.connect(self.goGestioneUtentiView)

        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(440, 260, 150, 30))
        self.logOutButton.setObjectName("logOutButton")
        self.logOutButton.clicked.connect(self.actionLogOut)

        self.gestioneTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.gestioneTestButton.setGeometry(QtCore.QRect(440, 160, 150, 30))
        self.gestioneTestButton.setObjectName("gestioneTestButton")
        self.gestioneTestButton.clicked.connect(self.goGestioneTestView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adminLabel.setText(_translate("MainWindow", "Admin"))
        self.gestioneUtentiButton.setText(_translate("MainWindow", "Gestione Utenti"))
        self.logOutButton.setText(_translate("MainWindow", "Log Out"))
        self.gestioneTestButton.setText(_translate("MainWindow", "Gestione Test"))

    def goGestioneUtentiView(self):
        try:
            self.gestioneUtenti = QtWidgets.QMainWindow()
            ui = GestioneUtentiView()
            ui.setupUi(self.gestioneUtenti)
            self.gestioneUtenti.show()
            ui.actionVisualizzaListaUtenti()
        except Exception as errore:
            print(errore)
    def goGestioneTestView(self):
        print('clicked')
        self.gestioneTest = QtWidgets.QMainWindow()
        self.ui = GestioneTestView()
        self.ui.setupUi(self.gestioneTest)
        self.gestioneTest.show()

    def actionLogOut(self):
        self.controllerAutenticazione = ControllerAutenticazione()
        self.controllerAutenticazione.logOut()

