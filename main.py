import sys

from View.LoginView import LoginView
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    login = LoginView()
    app = QApplication(sys.argv)
    login = QMainWindow()
    ui = LoginView()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())