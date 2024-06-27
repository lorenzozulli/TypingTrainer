import unittest

from Controller.ControllerPickle import ControllerPickle
from Controller.ControllerUtente import ControllerUtente
from Controller.ControllerTest import ControllerTest
from Model import Utilizzatore, Utente, Admin

class TestAdministrator(unittest.TestCase):
    '''
    def setUp(self):
        utente1 = Utente.Utente()
        utente1.setIdentifier(1)

        utente2 = Utente.Utente()
        utente2.setIdentifier(2)

        self.listaUtilizzatori = [
            utente1,
            utente2
        ]
    def testEliminaUtente(self):
        controllerUtente = ControllerUtente()
        controllerUtente.eliminaUtente(1)
        self.assertEqual(len(self.listaUtilizzatori), 1)
    def testModificaUtente(self):
        pass
    def testAggiungiTest(self):
        pass
    def testEliminaTest(self):
        pass
    def testModificaTest(self):
        pass

if __name__ == '__main__':
    unittest.main()

'''