from PyQt5.QtWidgets import (QToolTip, QDialog, QLabel, QMessageBox,
    QPushButton, QDesktopWidget, QLineEdit, QGridLayout)

from PyQt5.QtGui import *

from bd.PerguntaBD import PerguntaBD


class NovaPergunta(QDialog):


    def __init__(self, parent):
        super(NovaPergunta, self).__init__(parent)
        self._parent = parent
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        btNewChecklist = QPushButton('Criar', self)
        btNewChecklist.clicked.connect(self.salvarChecklist)

        nomeLabel = QLabel('Nome')

        self._nome = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(nomeLabel, 1, 0)
        grid.addWidget(self._nome, 1, 1)

        grid.addWidget(btNewChecklist, 3, 1)

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
            PerguntaBD.salvarPergunta(self._nome.text())
            QMessageBox.information(self, 'Message', "Pergunta salva com sucesso.")
            self.close()
        except Exception as e:
            QMessageBox.warning(self, 'Message', str(e))
