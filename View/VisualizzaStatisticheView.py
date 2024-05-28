# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\visualizzaStatistiche.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.ControllerStatistiche import ControllerStatistiche


class VisualizzaStatisticheView(object):
    def setupUi(self, MainWindow, currentUtilizzatore, errorCounter, testEseguito, tempoDiEsecuzione, caratteriCorretti):
        self.currentUtilizzatore = currentUtilizzatore
        self.errorCounter = errorCounter
        self.testEseguito = testEseguito
        self.tempoDiEsecuzione = tempoDiEsecuzione
        self.caratteriCorretti = caratteriCorretti

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.averageWordsPerMinuteLabel = QtWidgets.QLabel(self.centralwidget)
        self.averageWordsPerMinuteLabel.setGeometry(QtCore.QRect(40, 220, 600, 70))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.averageWordsPerMinuteLabel.setFont(font)
        self.averageWordsPerMinuteLabel.setObjectName("averageWordsPerMinuteLabel")
        self.PrecisioneMediaLabel = QtWidgets.QLabel(self.centralwidget)
        self.PrecisioneMediaLabel.setGeometry(QtCore.QRect(40, 310, 600, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PrecisioneMediaLabel.setFont(font)
        self.PrecisioneMediaLabel.setObjectName("PrecisioneMediaLabel")

        self.NumeroErroriLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumeroErroriLabel.setGeometry(QtCore.QRect(40, 410, 600, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NumeroErroriLabel.setFont(font)
        self.NumeroErroriLabel.setObjectName("NumeroErroriLabel")

        self.Titolo = QtWidgets.QLabel(self.centralwidget)
        self.Titolo.setGeometry(QtCore.QRect(190, 80, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Titolo.setFont(font)
        self.Titolo.setObjectName("Titolo")

        self.RiprovaButton = QtWidgets.QPushButton(self.centralwidget)
        self.RiprovaButton.setGeometry(QtCore.QRect(130, 520, 150, 30))
        self.RiprovaButton.setObjectName("RiprovaButton")

        self.TornaAllaHomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.TornaAllaHomeButton.setGeometry(QtCore.QRect(480, 520, 150, 30))
        self.TornaAllaHomeButton.setObjectName("TornaAllaHomeButton")

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
        self.averageWordsPerMinuteLabel.setText(_translate("MainWindow", "Parole digitate al minuto (media): "))
        self.PrecisioneMediaLabel.setText(_translate("MainWindow", "Precisione media: "))
        self.NumeroErroriLabel.setText(_translate("MainWindow", f"Numero errori eseguiti: {self.errorCounter}"))
        self.Titolo.setText(_translate("MainWindow", "Test completato, congratulazioni!"))
        self.RiprovaButton.setText(_translate("MainWindow", "Riprova"))
        self.TornaAllaHomeButton.setText(_translate("MainWindow", "Torna alla home"))
    
    def actionCalcolaAndAggiornaMediaNumeroParolePerMinuto(self):
        controllerStatistiche = ControllerStatistiche()
        self.media = controllerStatistiche.calcolaNumeroParolePerMinutoTest(len(self.testEseguito.contenutoTest), self.tempoDiEsecuzione)
        self.averageWordsPerMinuteLabel.setText(f"Parole digitate al minuto (media): {self.media}")
        controllerStatistiche.aggiornaMediaNumeroParolePerMinuto(self.currentUtilizzatore)

    def actionCacolaAndAggiornaPrecisioneMedia(self):
        controllerStatistiche = ControllerStatistiche()
        self.precisione = controllerStatistiche.calcolaPrecisionePercentualeTest(self.caratteriCorretti, self.errorCounter)
        self.PrecisioneMediaLabel.setText(f"Precisione media: {self.precisione}%")
        controllerStatistiche.aggiornaMediaPrecisionePercentuale(self.currentUtilizzatore)
    
    def actionCalcolaAndAggiornaTotaleTestEseguiti(self):
        controllerStatistiche = ControllerStatistiche()
        controllerStatistiche.calcolaTotaleTestEseguiti(self.currentUtilizzatore)

