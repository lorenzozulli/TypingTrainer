import unittest

from Controller.ControllerAutenticazione import ControllerAutenticazione
from Controller.ControllerPickle import ControllerPickle

class MyTestCase(unittest.TestCase):
    def testCaricaLista(self):
        controllerPickle = ControllerPickle()
        self.assertTrue(controllerPickle.caricaListaUtilizzatori())

    def testLogin(self):
        controllerAutenticazione = ControllerAutenticazione()

        self.assertEqual(controllerAutenticazione.logIn("UtenteTest", "PasswordTest00"), "Utente")
        self.assertEqual(controllerAutenticazione.logIn("Administrator", "Administrator00"), "Admin")
        self.assertEqual(controllerAutenticazione.logIn("UtenteTest", "passErrata"), "PasswordErrata")
        self.assertEqual(controllerAutenticazione.logIn("nomeErrato", "PasswordTest00"), "UsernameNonTrovato")

if __name__ == '__main__':
    unittest.main()