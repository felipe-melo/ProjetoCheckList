from entity.Usuario import Usuario


class Avaliador(Usuario):


    def mudarSenha(self, senha):
        self.senha = senha


    def finalizarAvaliacao(self, checkList):
        checkList.finalizado = True