from Model.Utente import Utente
from Controller.ControllerPickle import ControllerPickle

class ControllerStatistiche(object):
    def aggiornaMediaErroriPerTest(self, utilizzatoreDaAggiornare, valore):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for utente in listaUtilizzatori:
            if utilizzatoreDaAggiornare.getIdentifier() == utente.getIdentifier():
                vecchiaMedia = utente.getMediaErroriPerTest()
                totaleTest = utente.getTotaleTestEseguiti()
                print(vecchiaMedia)
                print(totaleTest)

                nuovaMedia = round(((((totaleTest-1) * vecchiaMedia)+valore)/totaleTest),2)
                utilizzatoreDaAggiornare.setMediaErroriPerTest(nuovaMedia)
                utente.setMediaErroriPerTest(nuovaMedia)

        controllerPickle.salvaListaUtilizzatori()

    def aggiornaMediaPrecisionePercentuale(self, utilizzatoreDaAggiornare, valore):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for utente in listaUtilizzatori:
            if utilizzatoreDaAggiornare.getIdentifier() == utente.getIdentifier():
                vecchiaMedia = utente.getMediaPrecisionePercentuale()
                totaleTest = utente.getTotaleTestEseguiti()
                print(vecchiaMedia)
                print(totaleTest)

                nuovaMedia = round(((((totaleTest-1) * vecchiaMedia)+valore)/totaleTest),2)
                utilizzatoreDaAggiornare.setMediaPrecisionePercentuale(nuovaMedia)
                utente.setMediaPrecisionePercentuale(nuovaMedia)


        controllerPickle.salvaListaUtilizzatori()

    def aggiornaMediaNumeroParolePerMinuto(self, utilizzatoreDaAggiornare, valore):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for utente in listaUtilizzatori:
            if utilizzatoreDaAggiornare.getIdentifier() == utente.getIdentifier():
                vecchiaMedia = utente.getMediaNumeroParolePerMinuto()
                totaleTest = utente.getTotaleTestEseguiti()
                print(vecchiaMedia)
                print(totaleTest)

                nuovaMedia = round(((((totaleTest-1) * vecchiaMedia)+valore)/totaleTest),2)

                utilizzatoreDaAggiornare.setMediaNumeroParolePerMinuto(nuovaMedia)
                utente.setMediaNumeroParolePerMinuto(nuovaMedia)

        controllerPickle.salvaListaUtilizzatori()

    def calcolaMediaErroriPerTest():
        pass
        
    def calcolaNumeroParolePerMinutoTest(self, numeroParole, tempoDiEsecuzione):
        wpm = round(numeroParole/(tempoDiEsecuzione/60), 2)
        return wpm
        
    def calcolaPrecisionePercentualeTest(self, lunghezzaTesto, numeroErrori):
        accuracy = round(((lunghezzaTesto - numeroErrori)/lunghezzaTesto)*100, 2)
        return accuracy
        
    def calcolaTotaleTestEseguiti(self, utilizzatoreDaAggiornare):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for utente in listaUtilizzatori:
            if utilizzatoreDaAggiornare.getIdentifier() == utente.getIdentifier():
                count = utilizzatoreDaAggiornare.getTotaleTestEseguiti()
                count = count + 1 
                utilizzatoreDaAggiornare.setTotaleTestEseguiti(count)
                utente.setTotaleTestEseguiti(count)

        controllerPickle.salvaListaUtilizzatori()
        
    