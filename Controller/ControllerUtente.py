from Controller import ControllerPickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    '''
    def eliminaUtente(self, identifier):
        #TODO: fare questa funzione
    
    def modificaUtente(self, identifier):
        #TODO: fare questa funzione
    '''
    def visualizzaListaUtenti(self):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtenti()

        listaUtilizzatori = controllerPickle.listaUtilizzatori
        print(len(listaUtilizzatori))

        row = 0
        self.tableWidget.setRowCount(len(listaUtilizzatori))
        for i in listaUtilizzatori:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i.identifier)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i.getUsername()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i.getDataOraCreazione())))
            row = row+1