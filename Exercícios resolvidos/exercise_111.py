# Assessores e modificadores.

class Cliente:
    def __init__(self, nome=None, telefone=None):
        self.__nome = nome
        self.__telefone = telefone

    def __set_nome(self, nome):
        self.__nome = nome

    def __set_telefone(self, telefone):
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone


print('Bem vindo ao programa que exibe o nome e o telefone de um cliente!')

cliente1 = Cliente()

print(f'\n*** Antes de ser criado ***'
      f'\nNome: {cliente1.get_nome()}'
      f'\nTelefone: {cliente1.get_telefone()}')

nome_cliente = input('\nDigite um nome: ')
telefone_cliente = input('Telefone: ')

cliente1._Cliente__set_nome(nome_cliente)
cliente1._Cliente__set_telefone(telefone_cliente)

print(f'\n*** Depois de ser alterado ***'
      f'\nNome: {cliente1.get_nome()}'
      f'\nTelefone: {cliente1.get_telefone()}')
