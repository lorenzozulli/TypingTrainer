import unittest
from Model import Utente 

class TestUtente(unittest.TestCase):
    def setUp(self):
        self.utente_normale = Utente.Utente()
        self.utente_normale.setIdentifier(0)
        self.utente_normale.setUsername('username1')
        self.utente_normale.setPassword('pass1')
        self.utente_normale.setEmail('utentenormale@gmail.com')
        self.utente_normale.setIsAdmin(False)

        self.miaListaUtilizzatori = [
            self.utente_normale
        ]

    def modificaProfilo(self, utenteDaModificare, nuovoUsername, nuovaEmail):
        try:
            for utente in self.miaListaUtilizzatori:
                if utenteDaModificare.getIdentifier() == utente.getIdentifier():
                    utente.setUsername(nuovoUsername)
                    utente.setEmail(nuovaEmail)
            return True
        except Exception:
            return False

    def testModificaProfilo(self):
        result = self.modificaProfilo(self.utente_normale, 'usernameMod', 'emailmodificata@gmail.com')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()