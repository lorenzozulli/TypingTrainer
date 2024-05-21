# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizzaProfiloView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Controller.ControllerAutenticazione import ControllerAutenticazione
from Controller.ControllerPickle import ControllerPickle
from View.ModificaProfiloView import ModificaProfiloView

class VisualizzaProfiloView(object):
    def setupUi(self, MainWindow, currentUtilizzatore):
        self.currentUtilizzatore = currentUtilizzatore

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(140, 190, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")

        self.modificaProfiloButton = QtWidgets.QPushButton(self.centralwidget)
        self.modificaProfiloButton.setGeometry(QtCore.QRect(440, 210, 150, 30))
        self.modificaProfiloButton.setObjectName("modificaProfiloButton")
        self.modificaProfiloButton.clicked.connect(self.goToModificaProfiloView)

        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(440, 260, 150, 30))
        self.logOutButton.setObjectName("logOutButton")
        self.logOutButton.clicked.connect(self.actionLogOut)

        self.joinedInLabel = QtWidgets.QLabel(self.centralwidget)
        self.joinedInLabel.setGeometry(QtCore.QRect(150, 270, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.joinedInLabel.setFont(font)
        self.joinedInLabel.setObjectName("joinedInLabel")

        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(230, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")

        self.labelTotaleTestEseguiti = QtWidgets.QLabel(self.centralwidget)
        self.labelTotaleTestEseguiti.setGeometry(QtCore.QRect(20, 320, 350, 62))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelTotaleTestEseguiti.setFont(font)
        self.labelTotaleTestEseguiti.setObjectName("labelTotaleTestEseguiti")

        self.labelPrecisioneMedia = QtWidgets.QLabel(self.centralwidget)
        self.labelPrecisioneMedia.setGeometry(QtCore.QRect(20, 415, 350, 62))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelPrecisioneMedia.setFont(font)
        self.labelPrecisioneMedia.setObjectName("labelPrecisioneMedia")

        self.labelMediaWPM = QtWidgets.QLabel(self.centralwidget)
        self.labelMediaWPM.setGeometry(QtCore.QRect(20, 510, 350, 62))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelMediaWPM.setFont(font)
        self.labelMediaWPM.setObjectName("labelMediaWPM")

        self.labelMediaErroriPerTest = QtWidgets.QLabel(self.centralwidget)
        self.labelMediaErroriPerTest.setGeometry(QtCore.QRect(20, 605, 350, 62))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelMediaErroriPerTest.setFont(font)
        self.labelMediaErroriPerTest.setObjectName("labelMediaErroriPerTest")

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
        self.usernameLabel.setText(_translate("MainWindow", str(self.currentUtilizzatore.getUsername())))
        self.modificaProfiloButton.setText(_translate("MainWindow", "Modifica Profilo"))
        self.logOutButton.setText(_translate("MainWindow", "Log Out"))
        self.joinedInLabel.setText(_translate("MainWindow", "Joined in,"))
        self.dateLabel.setText(_translate("MainWindow", str(self.currentUtilizzatore.getDataCreazione())))
        self.labelTotaleTestEseguiti.setText(_translate("MainWindow", f"Totale Test Eseguiti: {str(self.currentUtilizzatore.getTotaleTestEseguiti())}"))
        self.labelPrecisioneMedia.setText(_translate("MainWindow", f"Precisione Media (%): {str(self.currentUtilizzatore.getMediaPrecisionePercentuale())}"))
        self.labelMediaWPM.setText(_translate("MainWindow", f"Media WPM: {str(self.currentUtilizzatore.getMediaNumeroParolePerMinuto())}"))
        self.labelMediaErroriPerTest.setText(_translate("MainWindow", f"Media errori per test: {str(self.currentUtilizzatore.getMediaErroriPerTest())}"))

    def goToModificaProfiloView(self):
        self.modificaProfilo = QtWidgets.QMainWindow()
        self.ui = ModificaProfiloView()
        self.ui.setupUi(self.modificaProfilo, self.currentUtilizzatore)
        self.modificaProfilo.show()
        
        self.ui.ModificaButton.clicked.connect(self.aggiornaPagina)
        
    def actionLogOut(self):
        self.controllerAutenticazione = ControllerAutenticazione()
        self.controllerAutenticazione.logOut()
    
    def aggiornaPagina(self):
        self.usernameLabel.setText(self.currentUtilizzatore.getUsername())