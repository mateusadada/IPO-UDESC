# Crie uma classe Pessoa, com os atributos nome e idade e métodos para atribuir conteúdo aos atributos e para ler os
# mesmos.

class Pessoa:

    def __init__(self, nome=' ', idade=' '):
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
