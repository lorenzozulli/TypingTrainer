import json

class ControllerTest(object):
    '''
    def aggiungiTest():
        #TODO: fare questa funzione
    
    def eliminaTest(id):
        #TODO: fare questa funzione
    
    def modificaTest(id):
        #TODO: fare questa funzione

    def iniziaTest():
        #TODO: fare questa funzione
    
    def interrompiTest():
        #TODO: fare questa funzione
    
    def salvaListaTest():
        #TODO: fare questa funzione
    
    def visualizzaListaTest():
        #TODO: fare questa funzione
    '''
    def caricaListaTest(self):
        with open('listaTest.json') as f:
            self.listaTest = json.load(f)