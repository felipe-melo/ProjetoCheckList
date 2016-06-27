from PyQt5.QtWidgets import (QToolTip, QDialog, QRadioButton, QDesktopWidget, QGridLayout, QLabel,
                             QButtonGroup, QTextEdit, QPushButton)

from PyQt5.QtGui import *
from bd.CheckListBD import CheckListBD


class Checklist(QDialog):


    def __init__(self, parent, nome):
        super(Checklist, self).__init__(parent)
        self._parent = parent
        self.nome = nome
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        i = 1

        self.check = None

        for checklist in CheckListBD.checkList:

            if checklist.nome == self.nome:
                self.check = checklist
                break

        nomeLabel = QLabel(self.check.nome + " - " + self.check.tipo)
        self.grid.addWidget(nomeLabel, 0, 1)
        i = 0

        for p in self.check.perguntas:
            perg = QLabel(p.enunciado)
            i += 1
            self.grid.addWidget(perg, i, 1)
            i += 1
            gridOps = QButtonGroup(self)

            op1 = QRadioButton("Feito")
            gridOps.addButton(op1)
            op2 = QRadioButton("Não Feito")
            gridOps.addButton(op2)
            op3 = QRadioButton("não se aplica")
            gridOps.addButton(op3)

            self.grid.addWidget(op1, i, 0)
            self.grid.addWidget(op2, i, 1)
            self.grid.addWidget(op3, i, 2)

            op1.clicked.connect(p.feito)
            op2.clicked.connect(p.Nfeito)
            op3.clicked.connect(p.Naplica)

            i += 1

            obs = QTextEdit(self)
            obs.setPlaceholderText("Observações")
            obs.setLineWrapMode(2)

            self.grid.addWidget(obs, i, 1)

        btConfi = QPushButton('Confirmar', self)
        btConfi.clicked.connect(self.confirmar)

        self.grid.addWidget(btConfi, i + 1, 1)

        self.setLayout(self.grid)

        self.setGeometry(300, 300, 350, 300)
        self.center()
        self.setWindowTitle('CheckList')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):
        self._parent.show()
        event.accept()

    def confirmar(self):
        self.check.finalizado = True
        self.close()
        self._parent.show()



