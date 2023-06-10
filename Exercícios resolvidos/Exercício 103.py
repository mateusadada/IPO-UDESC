# Altere o exercício anterior para criar uma lista de objetos do tipo Pessoa, defina seus atributos e imprima os mesmos
# na tela.

class Pessoa:
    nome = None
    idade = None

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


banco_de_dados = []

print('Bem vindo ao programa que exibe nomes e as idades de n pessoas!')

while True:
    nome = input('\nInforme um nome (fim p/ sair): ')

    if nome == 'fim':
        break

    idade = int(input('Idade: '))

    objeto = Pessoa()
    objeto.set_nome(nome)
    objeto.set_idade(idade)
    banco_de_dados.append(objeto)

print(f'\n*** EXIBINDO TODOS OS {len(banco_de_dados)} NOMES E IDADES ***\n')

for i, e in enumerate(banco_de_dados):
    print(f'{i + 1}º: {e.get_nome()} tem {e.get_idade()} anos')
