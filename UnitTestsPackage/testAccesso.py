import unittest
from Controller.ControllerPickle import ControllerPickle
from Model import Utente

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.utente_normale = Utente.Utente()
        self.utente_normale.setUsername('username1')
        self.utente_normale.setPassword('pass1')
        self.utente_normale.setIsAdmin(False)

        self.utente_admin = Utente.Utente()
        self.utente_admin.setUsername('administrator')
        self.utente_admin.setPassword('adminpass0')
        self.utente_admin.setIsAdmin(True)

        self.utente_sbagliato = Utente.Utente()
        self.utente_sbagliato.setUsername('username2')
        self.utente_sbagliato.setPassword('pass2')
        self.utente_sbagliato.setIsAdmin(False)

        self.miaListaUtilizzatori = [
            self.utente_normale,
            self.utente_admin,
            self.utente_sbagliato
        ]

    def logIn(self, username, password):
        for i in self.miaListaUtilizzatori:
            if username == i.username and password == i.password and i.isAdmin == False:
                return "Utente", i
            elif username == i.username and password == i.password and i.isAdmin == True:
                return "Admin", i
            elif username == i.username:
                return "PasswordErrata", "errore"
        return "UsernameNonTrovato", "errore"

    def test_login_utente(self):
        result = self.logIn('username1', 'pass1')
        self.assertEqual(result, ("Utente", self.utente_normale))

    def test_login_admin(self):
        result = self.logIn('administrator', 'adminpass0')
        self.assertEqual(result, ("Admin", self.utente_admin))

    def test_login_password_errata(self):
        result = self.logIn('username2', 'wrongpass1')
        self.assertEqual(result, ("PasswordErrata", "errore"))

    def test_login_username_non_trovato(self):
        result = self.logIn('nonexistent', 'nopass1')
        self.assertEqual(result, ("UsernameNonTrovato", "errore"))

    def testCaricaListaUtilizzatori(self):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori
        self.assertIsNotNone(listaUtilizzatori)
    
if __name__ == '__main__':
    unittest.main()
