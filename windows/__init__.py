#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from windows.MenuPrincipal import MenuPrincipal
from windows.Login import Login


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
