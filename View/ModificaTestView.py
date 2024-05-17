# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificaTestView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.ControllerTest import ControllerTest
from PyQt5.QtWidgets import *


class ModificaTestView(object):
    def setupUi(self, MainWindow, testDaModificare):
        self.testDaModificare = testDaModificare

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ModificaButton = QtWidgets.QPushButton(self.centralwidget)
        self.ModificaButton.setGeometry(QtCore.QRect(310, 590, 150, 30))
        self.ModificaButton.setObjectName("ModificaButton")

        self.NomeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NomeInput.setGeometry(QtCore.QRect(150, 390, 491, 30))
        self.NomeInput.setObjectName("NomeInput")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(130, 230, 631, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setObjectName("label1")

        self.contenutoTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.contenutoTextEdit.setGeometry(QtCore.QRect(150, 440, 491, 131))
        self.contenutoTextEdit.setObjectName("contenutoTextEdit")

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
        self.NomeInput.setText(_translate("MainWindow", self.testDaModificare.getNome()))
        self.label1.setText(_translate("MainWindow", "Modifica il test!"))
        self.contenutoTextEdit.setPlainText(_translate("MainWindow", self.testDaModificare.getContenutoTest()))

    def actionModificaTest(self):
        self.controllaCampoNomeNonVuoto()
        self.controllaCampoContenutoNonvuoto()

        self.controllerTest = ControllerTest()
        self.modified = self.controllerTest.modificaTest(self.testDaModificare.getidentifier(), self.NomeInput.text(), self.contenutoTextEdit.toPlainText())

        self.controllaTestModificatoConSuccesso()
    
    def controllaCampoNomeNonVuoto(self):
        if self.NomeInput.text() == "":
            NomeVuoto = QMessageBox()
            NomeVuoto.setWindowTitle("Errore!")
            NomeVuoto.setText("Nessun Nome inserito!")
            NomeVuoto.exec_()
            return

    def controllaCampoContenutoNonVuoto(self):
        if self.contenutoTextEdit.toPlaintext() == "":
            ContenutoVuoto = QMessageBox()
            ContenutoVuoto.setWindowTitle("Errore!")
            ContenutoVuoto.setText("Nessun Contenuto inserito!")
            ContenutoVuoto.exec_()
            return
    
    def controllaTestModificatoConSuccesso(self):
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