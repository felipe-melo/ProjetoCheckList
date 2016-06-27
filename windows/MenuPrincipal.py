from PyQt5.QtWidgets import (QDialog, QToolTip, QDesktopWidget, QPushButton, QGridLayout)
from PyQt5.QtGui import QFont
from entity.Gerente import Gerente
from windows.NovoUsuario import NovoUsuario
from windows.NovoCheckList import NovoCheckList
from windows.NovaPergunta import NovaPergunta
from windows.ListaChecklist import ListaChecklist


class MenuPrincipal(QDialog):

    def __init__(self, parent, usuario):
        super(MenuPrincipal, self).__init__(parent)
        self._parent = parent
        self.usuario = usuario
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        grid = QGridLayout()
        grid.setSpacing(10)

        lin = 1

        if type(self.usuario) == Gerente:
            btNewAccount = QPushButton('Criar conta', self)
            btNewAccount.clicked.connect(self.openNewUser)

            btNewChecklist = QPushButton('Criar checklist', self)
            btNewChecklist.clicked.connect(self.openNewChecklist)

            btNovaPergunta = QPushButton('Criar pergunta', self)
            btNovaPergunta.clicked.connect(self.openNewQuestion)

            grid.addWidget(btNewAccount, lin, 0)
            grid.addWidget(btNewChecklist, lin, 1)

            lin += 1

            grid.addWidget(btNovaPergunta, lin, 1)


        btFillCheckList = QPushButton('Listar checklist', self)
        btFillCheckList.clicked.connect(self.listChecklist)

        grid.addWidget(btFillCheckList, lin, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.center()
        self.setWindowTitle('Menu')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):
        self._parent.show()
        event.accept()


    def openNewUser(self):
        self.hide()
        NovoUsuario(self)

    def openNewChecklist(self):
        self.hide()
        NovoCheckList(self)

    def openNewQuestion(self):
        self.hide()
        NovaPergunta(self)

    def listChecklist(self):
        self.hide()
        ListaChecklist(self)
