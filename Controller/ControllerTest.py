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

            nuovoTest = Test()
            identifierCandidato = len(listaTest)

            for self.i in listaTest:
                nuovoTest.setIdentifier(self.controllaIdentificatoreUnivoco(identifierCandidato))
                nuovoTest.setNome(self.controllaNomeUnivoco(nome))
                nuovoTest.setContenutoTest(self.assegnaContenutoTest(contenuto))

            nuovoTest.setDataCreazione(date.today())

            listaTest.append(nuovoTest)
            controllerPickle.salvaListaTest()
            return True
        except Exception:
            return False
    
    def controllaIdentificatoreUnivoco(self, identifierCandidato):
        if not(identifierCandidato == self.i.getIdentifier()):
            return identifierCandidato
        else:
            return identifierCandidato+1
    
    def controllaNomeUnivoco(self, nome):
        if not (nome == self.i.getNome()):
            return nome
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Nome già esistente!")
            registrazioneNonOK.exec_()
            raise Exception

    def assegnaContenutoTest(self, contenuto):
            words = contenuto.split(",")
            lunghezzaCaratteri = len([carattere for parola in words for carattere in parola])
            if lunghezzaCaratteri > 350:
                AggiuntaNonOK = QMessageBox()
                AggiuntaNonOK.setWindowTitle("Errore!")
                AggiuntaNonOK.setText('Hai inserito più di 350 caratteri!')
                AggiuntaNonOK.exec_()
                raise Exception
            elif len(words) < 5:
                AggiuntaNonOK = QMessageBox()
                AggiuntaNonOK.setWindowTitle("Errore!")
                AggiuntaNonOK.setText('Hai inserito meno di 5 parole!')
                AggiuntaNonOK.exec_()
                raise Exception
            else:
                return words

    def eliminaTest(self, identifier):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaTest()
            listaTest = controllerPickle.listaTest

            for i in listaTest:
                if identifier == i.getIdentifier():
                    listaTest.remove(i)

            controllerPickle.salvaListaTest()
            return True
        except Exception:
            return False
    
    def modificaTest(self, testDaModificare, nuovoNome, nuovoContenuto):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaTest()
            listaTest = controllerPickle.listaTest

            self.controllaNomeTestModificabile(nuovoNome, listaTest, testDaModificare)
            
            for test in listaTest:
                if testDaModificare.getIdentifier() == test.getIdentifier():
                    test.setNome(nuovoNome)
            test.setContenutoTest(self.assegnaContenutoTest(nuovoContenuto))

            controllerPickle.salvaListaTest()
            return True
        except Exception:
            return False
        
    def controllaNomeTestModificabile(self, nuovoNome, listaTest, testDaModificare):
        if any(test.getNome() == nuovoNome for test in listaTest if test.getNome() != testDaModificare.getNome()):
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Nome già esistente!")
            registrazioneNonOK.exec_()
            raise Exception