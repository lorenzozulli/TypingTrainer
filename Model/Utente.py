from Model.Utilizzatore import Utilizzatore
from Model.Statistiche import Statistiche
from PyQt5.QtWidgets import *

class Utente(Utilizzatore, Statistiche):
    def __init__(self):
        self.dataCreazione = ""
        self.email = ""
        self.statistiche = ""

    def getDataCreazione(self):
        return self.dataCreazione

    def getEmail(self):
        return self.email

    def getStatistiche(self):
        return self.statistiche
    
    def setDataCreazione(self, dataCreazione):
        self.dataCreazione = dataCreazione
    
    def setEmail(self, email):
        if email.__contains__('@'):
            self.email = email
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("La email non contiene il carattere @!")
            registrazioneNonOK.exec_()
            raise Exception
    
    def setStatistiche(self, statistiche):
        self.statistiche = statistiche