import pickle
import os

from datetime import datetime
from PyQt5.QtWidgets import *
from Controller.ControllerPickle import ControllerPickle

class ControllerBackup(object):
    def effettuaBackup(self):
        try:
            now = datetime.now()
            formattedNow = now.strftime('%Y-%m-%d_%H-%M-%S')

            self.backupDatiUtenti(formattedNow)
            self.backupDatiTest(formattedNow)

            BackupOK = QMessageBox()
            BackupOK.setWindowTitle("OK!")
            BackupOK.setText('Backup effettuato correttamente!')
            BackupOK.exec_()
        except Exception:
            BackupNonOK = QMessageBox()
            BackupNonOK.setWindowTitle("Errore!")
            BackupNonOK.setText('Backup Non effettuato correttamente!')
            BackupNonOK.exec_()
    
    def backupDatiUtenti(self, formattedNow):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        with open(os.path.join('BaseDiDati','Backup',f'{formattedNow}_listaUtilizzatori.pickle'), "wb") as f:
            pickle.dump(listaUtilizzatori, f, pickle.HIGHEST_PROTOCOL)
        
    def backupDatiTest(self, formattedNow):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()
        listaTest = controllerPickle.listaTest

        with open(os.path.join('BaseDiDati','Backup',f'{formattedNow}_listaTest.pickle'), "wb") as f:
            pickle.dump(listaTest, f, pickle.HIGHEST_PROTOCOL)