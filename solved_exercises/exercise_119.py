# Encapsulamento. A classe Cliente é simples, apenas com os atributos nome e telefone (salvar como clientes.py
# (Exercício119.py), incluindo getters e setters).

class Cliente:
    __nome = None
    __telefone = None

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def set_nome(self, nome):
        self.__nome = nome

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone
