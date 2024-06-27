import os
import pickle    


from Model.Admin import Admin
from Model.Test import Test

from datetime import date

class ControllerPickle(object):
    # Serve questo costruttore in quanto, se non esistono i file di listaUtilizzatori e/o listaTest,
    # vengono creati automaticamente dal sistema.
    # Inoltre crea automaticamente la cartella di Backup qualora non presente
    def __init__(self):
        if not os.path.isfile(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle')): 
            admin = Admin()
            admin.setIdentifier(0)
            admin.setUsername("Administrator")
            admin.setPassword("Administrator00")
            admin.setIsAdmin(True)
            admin.loadAdmin()
        if not os.path.isfile(os.path.join('BaseDiDati', 'listaTest.pickle')): 
            test = Test()
            test.setIdentifier(0)
            test.setNome("Test1")
            test.setContenutoTest(["modificami","come","preferisci","sono","solamente","un","template"])
            test.setDataCreazione(date.today())
            test.loadTest()
        if not os.path.isdir(os.path.join('BaseDiDati', 'Backup')):
            os.mkdir(os.path.join('BaseDiDati', 'Backup'))
        
    def caricaListaUtilizzatori(self):
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), "rb") as f:
            self.listaUtilizzatori = pickle.load(f)
    
    def salvaListaUtilizzatori(self):
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), "wb") as f:
            pickle.dump(self.listaUtilizzatori, f, pickle.HIGHEST_PROTOCOL)

    def caricaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), "rb") as f:
            self.listaTest = pickle.load(f)

    def salvaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), "wb") as f:
            pickle.dump(self.listaTest, f, pickle.HIGHEST_PROTOCOL)


