from bd.UsuarioBD import UsuarioBD

from PyQt5.QtWidgets import (QToolTip, QMessageBox, QLabel, QWidget,
    QPushButton, QDesktopWidget, QLineEdit, QGridLayout)

from windows.MenuPrincipal import MenuPrincipal
from PyQt5.QtGui import *


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        btLogin = QPushButton('Logar', self)
        btLogin.clicked.connect(self.openMain)

        matLabel = QLabel('Matricula')
        passLabel = QLabel('Senha')

        self._login = QLineEdit()
        self._password = QLineEdit()
        self._password.setEchoMode(QLineEdit.Password)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(matLabel, 1, 0)
        grid.addWidget(self._login, 1, 1)

        grid.addWidget(passLabel, 2, 0)
        grid.addWidget(self._password, 2, 1)

        grid.addWidget(btLogin, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.center()
        self.setWindowTitle('Login')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openMain(self):
        try:
            usuario = UsuarioBD.logar(self._login.text(), self._password.text())
            MenuPrincipal(self, usuario)
            self.hide()
        except Exception as e:
            print(str(e))
