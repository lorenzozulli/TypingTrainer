import unittest

from Controller.ControllerAutenticazione import ControllerAutenticazione
from Controller.ControllerPickle import ControllerPickle
from Model import Utilizzatore, Utente, Admin

class MyTestCase(unittest.TestCase):
    def testCaricaListaUtilizzatori(self):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori
        self.assertIsNotNone(listaUtilizzatori)

    def testLogin(self):
        controllerAutenticazione = ControllerAutenticazione()

        self.assertIsNotNone(controllerAutenticazione.logIn("Administrator", "Administrator00"))
        self.assertIsNotNone(controllerAutenticazione.logIn("UtenteTest", "PasswordTest00"))
        self.assertEqual(controllerAutenticazione.logIn("UtenteTest", "passErrata"), ("PasswordErrata", "errore"))
        self.assertEqual(controllerAutenticazione.logIn("nomeErrato", "PasswordTest00"), ("UsernameNonTrovato", "errore"))

if __name__ == '__main__':
    unittest.main()
