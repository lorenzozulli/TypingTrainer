# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\iniziaTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from View.VisualizzaStatisticheView import VisualizzaStatisticheView

class IniziaTestView(object):

    def setupUi(self, MainWindow, currentUtilizzatore, testSelezionato):
        self.currentUtilizzatore = currentUtilizzatore
        self.testSelezionato = testSelezionato
        self.timeCounter = 0.0
        self.running = False
        self.errorCounter = 0
        self.correctCounter = 0
        self.lunghezza = 0
        self.ended = False 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimerLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimerLabel.setGeometry(QtCore.QRect(325, 100, 600, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.TimerLabel.setFont(font)
        self.TimerLabel.setObjectName("TimerLabel")

        self.TestDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.TestDisplayLabel.setGeometry(QtCore.QRect(70, 120, 650, 400))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TestDisplayLabel.setFont(font)
        self.TestDisplayLabel.setObjectName("TestDisplayLabel")
        self.TestDisplayLabel.setWordWrap(True)

        self.WordInputLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.WordInputLineEdit.setGeometry(QtCore.QRect(90, 600, 600, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.WordInputLineEdit.setFont(font)
        self.WordInputLineEdit.setObjectName("WordInputLineEdit")
        self.WordInputLineEdit.setFocusPolicy(Qt.StrongFocus)
        self.WordInputLineEdit.textChanged.connect(self.start)

        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(310, 660, 150, 30))
        self.ResetButton.setObjectName("PauseButton")
        self.ResetButton.clicked.connect(self.reset)

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
        self.TimerLabel.setText(_translate("MainWindow", str(self.timeCounter)))
        self.TestDisplayLabel.setText(_translate("MainWindow", ''))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.WordInputLineEdit.setPlaceholderText(_translate("MainWindow", "Inizia a scrivere per avviare il test!"))

    def actionRenderizzaTest(self):
        self.testRandomizzato = self.testSelezionato.shuffleTest()
        self.TestDisplayLabel.setText(self.testRandomizzato)
    
    def start(self):
        if not self.running:
            self.running = True
            self.ended = False

            self.timer = QTimer()
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.timeThread)
            self.timer.start()
        
        if not self.testRandomizzato.startswith(self.WordInputLineEdit.text()):
            if self.lunghezza <= len(self.WordInputLineEdit.text()):
                self.WordInputLineEdit.setStyleSheet('color: red;')
                formatted_text = f'<span style="color: red;">{self.testRandomizzato[:len(self.WordInputLineEdit.text())]}</span>{self.testRandomizzato[len(self.WordInputLineEdit.text()):]}'
                self.TestDisplayLabel.setText(formatted_text)
                self.errorCounter = self.errorCounter + 1
        else:
            self.WordInputLineEdit.setStyleSheet('color: black;')
            formatted_text = f'<span style="color: green;">{self.testRandomizzato[:len(self.WordInputLineEdit.text())]}</span>{self.testRandomizzato[len(self.WordInputLineEdit.text()):]}'
            self.TestDisplayLabel.setText(formatted_text)
            self.correctCounter = self.correctCounter + 1

        self.lunghezza = len(self.WordInputLineEdit.text())

        if self.WordInputLineEdit.text() == self.testRandomizzato:
            self.running = False
            self.ended = True
            self.timer.stop()
            self.TestDisplayLabel.setStyleSheet('color: green;')
            self.WordInputLineEdit.setStyleSheet('color: green;')
            self.goToVisualizzaStatisticheView()
                        
    def timeThread(self):
        if self.timeCounter < 999:
            self.timeCounter = self.timeCounter + 0.1
            self.TimerLabel.setText(str(round(self.timeCounter, 1)))
        else:
            self.reset()

    def reset(self):
        if self.running or self.ended:
            self.WordInputLineEdit.clear()
            self.running = False
            self.ended = False
            self.timer.stop()
            self.timeCounter = 0.0
            self.errorCounter = 0
            self.correctCounter = 0
            self.TimerLabel.setText(str(self.timeCounter))
            self.TestDisplayLabel.setStyleSheet('color: black;')

    def goToVisualizzaStatisticheView(self):
        self.visualizzaStatisticheView = QtWidgets.QMainWindow()
        self.ui = VisualizzaStatisticheView()
        self.ui.setupUi(self.visualizzaStatisticheView, self.currentUtilizzatore, self.errorCounter, self.testSelezionato, self.timeCounter, self.correctCounter)
        self.ui.actionCalcolaAndAggiornaTotaleTestEseguiti()
        self.ui.actionCalcolaAndAggiornaMediaNumeroParolePerMinuto()
        self.ui.actionCacolaAndAggiornaPrecisioneMedia()
        self.ui.actionCalcolaAndAggiornaMediaErroriPerTest()
        self.visualizzaStatisticheView.show()