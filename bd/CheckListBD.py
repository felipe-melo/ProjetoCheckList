#!/usr/bin/python3
# -*- coding: utf-8 -*-

from entity.Checklist import Checklist

class CheckListBD():

    checkList = []

    @staticmethod
    def salvarCheckList(nome, tipo, perguntas):
        for checkList in CheckListBD.checkList:
            if checkList.nome == nome:
                raise Exception("CheckList já cadastrado.")
        checkList = Checklist(nome, tipo, perguntas)
        CheckListBD.checkList.append(checkList)
