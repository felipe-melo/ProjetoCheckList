import datetime


class Checklist:

    def __init__(self, nome, tipo, perguntas):
        self.nome = nome
        self.tipo = tipo
        self.data = datetime.datetime.now()
        self.finalizado = False
        self.perguntas = perguntas

    def gerarRelatorio(self):
        print("Relatório Gerado")
