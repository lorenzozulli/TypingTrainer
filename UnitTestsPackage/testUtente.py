import unittest
import pickle

from Controller.ControllerUtente import ControllerUtente
from Controller.ControllerPickle import ControllerPickle
from Model import Utente 

class TestUtente(unittest.TestCase):
    def testModificaProfilo(self):
        with open('listaUtilizzatori.pickle', "rb") as f:
            listaUtilizzatori = pickle.load(f)

        controllerUtente = ControllerUtente()

        self.assertTrue(controllerUtente.modificaProfilo(self.utenteTest, "Plutone17", "utenteTest@gmail.com", "Marte77"))

if __name__ == '__main__':
    unittest.main()