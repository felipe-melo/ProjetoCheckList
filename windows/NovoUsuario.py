from bd.UsuarioBD import UsuarioBD

from PyQt5.QtWidgets import (QToolTip, QDialog, QLabel, QMessageBox,
    QPushButton, QDesktopWidget, QLineEdit, QGridLayout, QComboBox)

from PyQt5.QtGui import *


class NovoUsuario(QDialog):


    def __init__(self, parent):
        super(NovoUsuario, self).__init__(parent)
        self._parent = parent
        self.list = [
            self.tr("Avaliador"),
            self.tr("Gerente")
        ]
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        btNewUser = QPushButton('Criar', self)
        btNewUser.clicked.connect(self.salvarUsuario)

        matLabel = QLabel('Matricula')
        passLabel = QLabel('Senha')
        tipoLabel = QLabel('Tipo')

        self._login = QLineEdit()
        self._password = QLineEdit()
        self._password.setEchoMode(QLineEdit.Password)
        self._tipo = QComboBox()

        self._tipo.addItems(self.list)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(matLabel, 1, 0)
        grid.addWidget(self._login, 1, 1)

        grid.addWidget(passLabel, 2, 0)
        grid.addWidget(self._password, 2, 1)

        grid.addWidget(tipoLabel, 3, 0)
        grid.addWidget(self._tipo, 3, 1)

        grid.addWidget(btNewUser, 4, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.center()
        self.setWindowTitle('Novo Usuário')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):
        self._parent.show()
        event.accept()

    def salvarUsuario(self):
        try:
            UsuarioBD.salvarUsuario(self._login.text(), self._password.text(), self._tipo.currentText())
            QMessageBox.information(self, 'Message', "Usuário salvo com sucesso.")
            self.close()
        except Exception as e:
            QMessageBox.warning(self, 'Message', str(e))
