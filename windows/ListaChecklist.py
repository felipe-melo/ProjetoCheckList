from PyQt5.QtWidgets import (QToolTip, QDialog, QPushButton, QDesktopWidget, QGridLayout)

from PyQt5.QtGui import *
from bd.CheckListBD import CheckListBD
from windows.Checklist import Checklist


class ListaChecklist(QDialog):


    def __init__(self, parent):
        super(ListaChecklist, self).__init__(parent)
        self._parent = parent
        self.initUI()



    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        grid = QGridLayout()
        grid.setSpacing(10)

        i = 1

        for checklist in CheckListBD.checkList:

            if not checklist.finalizado:
                btNewChecklist = QPushButton(checklist.nome, self)
                btNewChecklist.clicked.connect(lambda: self.abrirChecklist(checklist))

                grid.addWidget(btNewChecklist, i, 1)

                i += 1

        self.setLayout(grid)

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

    def abrirChecklist(self, checklist):
        Checklist(self, checklist.nome)
        self.hide()

