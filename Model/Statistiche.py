from Model.Utente import Utente


class Statistiche(Utente):
    def __init__(self):
        self.mediaErroriPerTest = ""
        self.mediaNumeroParolePerMinuto = ""
        self.mediaPrecisionePercentuale = ""
        self.totaleTestEseguiti = ""
    
    def getMediaErroriPerTest(self):
        return self.mediaErroriPerTest
    
    def getMediaNumeroParolePerMinuto(self):
        return self.mediaNumeroParolePerMinuto
    
    def getMediaPrecisionePercentuale(self):
        return self.mediaPrecisionePercentuale
    
    def getTotaleTestEseguiti(self):
        return self.totaleTestEseguiti
    
    def setMediaErroriPerTest(self, mediaErroriPerTest):
        self.mediaErroriPerTest = mediaErroriPerTest

    def setMediaNumeroParolePerMinuto(self, mediaNumeroParolePerMinuto):
        self.mediaNumeroParolePerMinuto = mediaNumeroParolePerMinuto

    def setMediaPrecisionePercentuale(self, mediaPrecisionePercentuale):
        self.mediaPrecisionePercentuale = mediaPrecisionePercentuale
    
    def setTotaleTestEseguiti(self, totaleTestEseguiti):
        self.totaleTestEseguiti = totaleTestEseguiti