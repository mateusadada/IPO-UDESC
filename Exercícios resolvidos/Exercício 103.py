# Altere o exercício anterior para criar uma lista de objetos do tipo Pessoa, defina seus atributos e imprima os mesmos
# na tela.

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade


# usar uma lista p/ adicionar o nome e a idade
# a variável que vou guardar na lista eu devo puxar a classe, usar a função para definir o nome e a idade e
# daí armazenar na lista
# no fim eu imprimo tudo
