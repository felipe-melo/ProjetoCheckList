from abc import ABC


class Usuario(ABC):

    def __init__(self, matricula, senha):
        self.matricula = matricula
        self.senha = senha
