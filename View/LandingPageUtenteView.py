# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LandingPageUtenteView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from View.VisualizzaProfiloView import VisualizzaProfiloView
from View.IniziaTestView import IniziaTestView
from Controller.ControllerPickle import ControllerPickle
from PyQt5.QtCore import *

class LandingPageUtenteView(object):
    def setupUi(self, MainWindow, currentUtilizzatore):
        self.currentUtilizzatore = currentUtilizzatore

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 10, 351, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setAcceptDrops(False)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 731, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,200)

        self.searchBarInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBarInput.setGeometry(QtCore.QRect(20, 170, 500, 30))
        self.searchBarInput.setObjectName("searchBarInput")
        self.searchBarInput.textChanged.connect(self.searchTest)

        self.profiloButton = QtWidgets.QToolButton(self.centralwidget)
        self.profiloButton.setGeometry(QtCore.QRect(650, 30, 101, 71))
        self.profiloButton.setObjectName("profiloButton")
        self.profiloButton.clicked.connect(self.goToVisualizzaProfiloView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Benvenuto in Typing Trainer!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data Creazione"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Seleziona"))
        self.searchBarInput.setText(_translate("MainWindow", ""))
        self.searchBarInput.setPlaceholderText(_translate("MainWindow", "Inserisci ID, Nome oppure Data di Creazione"))
        self.profiloButton.setText(_translate("MainWindow", "Vai a profilo"))
    
    def goToVisualizzaProfiloView(self):
        self.visualizzaProfilo = QtWidgets.QMainWindow()
        self.ui = VisualizzaProfiloView()
        self.ui.setupUi(self.visualizzaProfilo, self.currentUtilizzatore)
        self.visualizzaProfilo.show()

    def actionVisualizzaListaTest(self):
        try:
            self.loadListaTest()
        except Exception as e:
            print(e)

    def loadListaTest(self):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()
        listaTest = controllerPickle.listaTest

        row = 0
        self.tableWidget.setRowCount(len(listaTest))
        for i in listaTest:
            identifierColumn = QtWidgets.QTableWidgetItem(str(i.getIdentifier()))
            identifierColumn.setFlags(identifierColumn.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 0, identifierColumn)

            nomeColumn = QtWidgets.QTableWidgetItem(i.getNome()) 
            nomeColumn.setFlags(nomeColumn.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 1, nomeColumn)

            dataCreazioneColumn = QtWidgets.QTableWidgetItem(str(i.getDataCreazione())) 
            dataCreazioneColumn.setFlags(dataCreazioneColumn.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 2, dataCreazioneColumn)
            
            self.selezionaColumn = QtWidgets.QPushButton("Seleziona")
            self.selezionaColumn.clicked.connect(lambda _, test=i: self.goToIniziaTestView(test))
            self.tableWidget.setCellWidget(row, 3, self.selezionaColumn)

            row = row+1

    def goToIniziaTestView(self, testSelezionato):
        self.iniziaTestView = QtWidgets.QMainWindow()
        self.ui = IniziaTestView()
        self.ui.setupUi(self.iniziaTestView, self.currentUtilizzatore, testSelezionato)
        self.iniziaTestView.show()

        self.ui.actionRenderizzaTest()

    def searchTest(self, query):
        items = self.tableWidget.findItems(query, Qt.MatchContains)
        if items:
            item = items[0]
            self.tableWidget.setCurrentItem(item)
        