#!/usr/bin/python3
# -*- coding: utf-8 -*-

from entity.Pergunta import Pergunta

class PerguntaBD():

    perguntas = []

    perguntas.append(Pergunta("Pergunta 1"))
    perguntas.append(Pergunta("Pergunta 2"))
    perguntas.append(Pergunta("Pergunta 3"))
    perguntas.append(Pergunta("Pergunta 4"))
    perguntas.append(Pergunta("Pergunta 5"))
    perguntas.append(Pergunta("Pergunta 6"))
    perguntas.append(Pergunta("Pergunta 7"))
    perguntas.append(Pergunta("Pergunta 8"))

    @staticmethod
    def salvarPergunta(enunciado):
        for pergunta in PerguntaBD.perguntas:
            if pergunta.enunciado == enunciado:
                raise Exception("Pergunta já cadastrado.")
        pergunta = Pergunta(enunciado)
        PerguntaBD.perguntas.append(pergunta)
