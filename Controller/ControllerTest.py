from Model import Test
from Controller import ControllerPickle
class ControllerTest(object):
    def aggiungiTest(self, nome, contenuto):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest

        NuovoTest = Test.Test()
        NuovoTest.setIdentifier(len(listaTest)+1)
        NuovoTest.setNome(nome)
        NuovoTest.setContenuto(contenuto)

        listaTest.append(NuovoTest)
        controllerPickle.salvaListaTest()
    '''
    def eliminaTest(self, identifier):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest
        del listaTest[id]

        controllerPickle.salvaListaTest()
    
    def modificaTest(self, identifier):
        #TODO: fare questa funzione

    def iniziaTest(self):
        #TODO: fare questa funzione
    
    def interrompiTest(self):
        #TODO: fare questa funzione
    
    def visualizzaListaTest(self):
        #TODO: fare questa funzione
    '''