from Controller.ControllerPickle import ControllerPickle
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    def eliminaUtente(self, identifier):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            listaUtilizzatori.remove(listaUtilizzatori[identifier])

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False
    
    def modificaUtente(self, identifier, nuovoUsername, nuovaEmail):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            listaUtilizzatori[identifier].setUsername(nuovoUsername)
            listaUtilizzatori[identifier].setEmail(nuovaEmail)

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False

    def modificaProfilo(self, identifier, nuovoUsername, nuovaEmail, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            listaUtilizzatori[identifier].setUsername(nuovoUsername)
            listaUtilizzatori[identifier].setEmail(nuovaEmail)
            listaUtilizzatori[identifier].setPassword(nuovaPassword)
            
            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False

        