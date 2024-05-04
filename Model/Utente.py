from Model.Utilizzatore import Utilizzatore


class Utente(Utilizzatore):
    def __init__(self):
        self.dataOraCreazione = ""
        self.email = ""
        self.statistiche = ""

    def getDataOraCreazione(self):
        return self.dataOraCreazione

    def getEmail(self):
        return self.email

    def getStatistiche(self):
        return self.statistiche
    
    def setDataOraCreazione(self, dataOraCreazione):
        self.dataOraCreazione = dataOraCreazione
    
    def setEmail(self, email):
        self.email = email

    def setStatistiche(self, statistiche):
        self.statistiche = statistiche