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
        '''
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori
        '''

        self.assertEqual(controllerAutenticazione.logIn("UtenteTest", "PasswordTest00"), ("Utente", Utente.Utente(username = 'UtenteTest', password = 'PasswordTest')))
        self.assertEqual(controllerAutenticazione.logIn("Administrator", "Administrator00"), ("Admin", Admin.Admin(username = 'Administrator', password = 'Administrator00')))
        self.assertEqual(controllerAutenticazione.logIn("UtenteTest", "passErrata"), ("PasswordErrata", "errore"))
        self.assertEqual(controllerAutenticazione.logIn("nomeErrato", "PasswordTest00"), ("UsernameNonTrovato", "errore"))

if __name__ == '__main__':
    unittest.main()
