from PyQt5.QtWidgets import (QToolTip, QDialog, QLabel, QMessageBox, QCheckBox,
    QPushButton, QDesktopWidget, QLineEdit, QGridLayout, QComboBox)

from PyQt5.QtGui import *

from bd.CheckListBD import CheckListBD
from bd.PerguntaBD import PerguntaBD
from entity.Pergunta import Pergunta


class NovoCheckList(QDialog):


    def __init__(self, parent):
        super(NovoCheckList, self).__init__(parent)
        self._parent = parent
        self.list = [
            self.tr("Produto"),
            self.tr("Etapa")
        ]
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        btNewChecklist = QPushButton('Criar', self)
        btNewChecklist.clicked.connect(self.salvarChecklist)

        nomeLabel = QLabel('Nome')
        tipoLabel = QLabel('Tipo')

        self._nome = QLineEdit()
        self._tipo = QComboBox()

        self._tipo.addItems(self.list)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(nomeLabel, 1, 0)
        grid.addWidget(self._nome, 1, 1)

        grid.addWidget(tipoLabel, 2, 0)
        grid.addWidget(self._tipo, 2, 1)

        self.questions = []
        i = 2

        for p in PerguntaBD.perguntas:
            check = QCheckBox(p.enunciado)
            self.questions.append(check)
            i += 1
            grid.addWidget(check, i, 1)

        grid.addWidget(btNewChecklist, i+1, 1)

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

    def salvarChecklist(self):
        try:
            ps = []
            for c in self.questions:
                if c.isChecked():
                    ps.append(Pergunta(c.text()))
            CheckListBD.salvarCheckList(self._nome.text(), self._tipo.currentText(), ps)
            QMessageBox.information(self, 'Message', "Checklist salvo com sucesso.")
            self.close()
        except Exception as e:
            QMessageBox.warning(self, 'Message', str(e))
