# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LandingPageUtenteView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from View import VisualizzaProfiloView


class LandingPageUtenteView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IniziaTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.IniziaTestButton.setGeometry(QtCore.QRect(320, 730, 150, 30))
        self.IniziaTestButton.setObjectName("IniziaTestButton")
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.cercaButton = QtWidgets.QPushButton(self.centralwidget)
        self.cercaButton.setGeometry(QtCore.QRect(380, 170, 75, 30))
        self.cercaButton.setObjectName("cercaButton")
        self.searchBarInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBarInput.setGeometry(QtCore.QRect(20, 170, 350, 30))
        self.searchBarInput.setObjectName("searchBarInput")
        self.profiloButton = QtWidgets.QToolButton(self.centralwidget)
        self.profiloButton.setGeometry(QtCore.QRect(650, 30, 101, 71))
        self.profiloButton.setObjectName("profiloButton")
        self.profiloButton.clicked.connect(self.goVisualizzaProfilo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IniziaTestButton.setText(_translate("MainWindow", "Inizia Test"))
        self.label1.setText(_translate("MainWindow", "Benvenuto in Typing Trainer!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data Creazione"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Seleziona"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Numeri"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Punteggiatura"))
        self.cercaButton.setText(_translate("MainWindow", "Cerca"))
        self.searchBarInput.setText(_translate("MainWindow", ""))
        self.searchBarInput.setPlaceholderText(_translate("MainWindow", "Inserisci ID oppure Nome"))
        self.profiloButton.setText(_translate("MainWindow", "Vai a profilo"))
    
    def goVisualizzaProfilo(self):
        self.visualizzaProfilo = QtWidgets.QMainWindow()
        VisualizzaProfiloView().setupUi(self.visualizzaProfilo)
        self.visualizzaProfilo.show()
