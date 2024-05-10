from Controller import ControllerPickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    '''
    def eliminaUtente(id):
        #TODO: fare questa funzione
    
    def modificaUtente(id):
        #TODO: fare questa funzione
    '''
    def visualizzaListaUtenti(self):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtenti()

        listaUtilizzatori = controllerPickle.listaUtilizzatori

        row = 0
        self.tableWidget.setRowCount(len(listaUtilizzatori))
        for i in listaUtilizzatori:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i.id)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i.username))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i.dataOraCreazione)))
            '''
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem())
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem())
            '''
            row = row+1