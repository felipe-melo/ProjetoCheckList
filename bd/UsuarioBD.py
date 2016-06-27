#!/usr/bin/python3
# -*- coding: utf-8 -*-

from entity.Gerente import Gerente
from entity.Avaliador import Avaliador

class UsuarioBD():


    usuarios = []
    admin = Gerente("admin", "123456")
    usuarios.append(admin)

    @staticmethod
    def logar(login, password):
        for usuario in UsuarioBD.usuarios:
            if usuario.matricula == login and usuario.senha == password:
                return usuario
        raise Exception("Login ou senha inválidos.")


    @staticmethod
    def salvarUsuario(login, password, tipo):
        for usuario in UsuarioBD.usuarios:
            if usuario.matricula == login:
                raise Exception("Usuário já cadastrado.")
        if tipo == "Avaliador":
            usuario = Avaliador(login, password)
        else:
            usuario = Gerente(login, password)

        UsuarioBD.usuarios.append(usuario)
