from Model.Utilizzatore import Utilizzatore

class Utente(Utilizzatore):
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
        self.email = email

    def setStatistiche(self, statistiche):
        self.statistiche = statistiche