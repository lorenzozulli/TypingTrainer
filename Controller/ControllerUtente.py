from Controller.ControllerPickle import ControllerPickle
from Controller.ControllerAutenticazione import ControllerAutenticazione
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    def eliminaUtente(self, identifier):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            for i in listaUtilizzatori:
                if identifier == i.getIdentifier():
                    listaUtilizzatori.remove(i)

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False
    
    def modificaUtente(self, identifier, nuovoUsername, nuovaEmail):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori
            controllerAutenticazione = ControllerAutenticazione()

            for i in listaUtilizzatori:
                if identifier == i.getIdentifier():
                    i.setUsername(controllerAutenticazione.assegnaUsernameAppropriato(nuovoUsername))
                    i.setEmail(controllerAutenticazione.assegnaEmailAppropriata(nuovaEmail))

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception as e:
            print(e)
            return False

    def modificaProfilo(self, identifier, nuovoUsername, nuovaEmail, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori
            controllerAutenticazione = ControllerAutenticazione()

            for self.i in listaUtilizzatori:
                if identifier == self.i.getIdentifier():
                    self.utenteDaModificare.setUsername(controllerAutenticazione.assegnaUsernameAppropriato(nuovoUsername))
                    self.utenteDaModificare.setEmail(controllerAutenticazione.assegnaEmailAppropriata(nuovaEmail))
                    self.utenteDaModificare.setPassword(controllerAutenticazione.assegnaPasswordAppropriata(nuovaPassword))
            
            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception as e:
            print(e)
            return False

        