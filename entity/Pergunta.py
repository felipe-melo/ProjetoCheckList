from entity.Resposta import Resposta



class Pergunta():

    def __init__(self, enunciado):
        self.enunciado = enunciado
        self.resposta = None
        self.obs = ""

    def feito(self):
        self.resposta = Resposta.Feito

    def Nfeito(self):
        self.resposta = Resposta.N_Realizado

    def Naplica(self):
        self.resposta = Resposta.N_Aplica
