from datetime import date

from Model.Test import Test
from Controller.ControllerPickle import ControllerPickle
from PyQt5.QtWidgets import *

class ControllerTest(object):
    def aggiungiTest(self, nome, contenuto):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaTest()
            listaTest = controllerPickle.listaTest

            self.nuovoTest = Test()
            identifierCandidato = len(listaTest)

            for self.i in listaTest:
                self.assegnaIdentificatoreUnivoco(identifierCandidato)
                self.assegnaNomeAppropriato(nome)

            self.assegnaContenutoTest(contenuto) 
            self.nuovoTest.setDataCreazione(date.today())

            listaTest.append(self.nuovoTest)
            controllerPickle.salvaListaTest()
            return True
        except Exception as e:
            print(e)
            return False
    
    def assegnaIdentificatoreUnivoco(self, identifierCandidato):
        if not(identifierCandidato == self.i.getIdentifier()):
            self.nuovoTest.setIdentifier(identifierCandidato)
        else:
            self.nuovoTest.setIdentifier(identifierCandidato+1)
    
    def assegnaNomeAppropriato(self, nome):
        if not (nome == self.i.getNome()):
            self.nuovoTest.setNome(nome)
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Nome già esistente!")
            registrazioneNonOK.exec_()
            raise Exception

    def assegnaContenutoTest(self, contenuto):
            words = contenuto.split(",")
            self.nuovoTest.setContenutoTest(words)

    def eliminaTest(self, identifier):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaTest()
            listaTest = controllerPickle.listaTest

            for  i in listaTest:
                if identifier == i.getIdentifier():
                    listaTest.remove(i)

            controllerPickle.salvaListaTest()
            return True
        except Exception:
            return False
    
    def modificaTest(self, identifier, nuovoNome, nuovoContenuto):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaTest()
            listaTest = controllerPickle.listaTest

            for self.i in listaTest:
                if identifier == self.i.getIdentifier():
                    self.i.assegnaNomeAppropriato(nuovoNome)
                    self.i.assegnaContenutoTest(nuovoContenuto)
            
            controllerPickle.salvaListaTest()
            return True
        except Exception as e:
            print(e)
            return False
        
'''
    def iniziaTest(self):
        #TODO: fare questa funzione
    
    def interrompiTest(self):
        #TODO: fare questa funzione
    '''