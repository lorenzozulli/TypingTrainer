import sys

from View.LoginView import LoginView
from PyQt5.QtWidgets import QApplication, QMainWindow

from Controller.ControllerPickle import ControllerPickle
from Controller.ControllerBackup import ControllerBackup

if __name__ == "__main__":
    ControllerPickle = ControllerPickle()
    ControllerBackup = ControllerBackup()

    login = LoginView()
    app = QApplication(sys.argv)
    login = QMainWindow()
    ui = LoginView()
    ui.setupUi(login)
    login.show()

    sys.exit(app.exec_())
    
