from entity.Usuario import Usuario
from entity.Checklist import Checklist


class Gerente(Usuario):


    def mudarSenha(self, senha):
        self.senha = senha


    def criarChecklist(self, nome, tipo):
        checklist = Checklist(nome, tipo)
