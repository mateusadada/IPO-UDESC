# Classe Pessoa: Crie uma classe que modele uma pessoa:
#   Atributos: nome, idade, peso e altura
#   Métodos: Envelhecer, engordar, crescer. Obs: Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela
#   menor que 21 anos, ela deve crescer 0,5 cm ao ano. A pessoa engorda 0,5 kg por ano. Faça uma projeção para X anos,
#   informando o novo peso e/ou altura.

class Pessoa:
    nome = None
    idade = None
    peso = None
    altura = None

    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def projecao(self, anos):
        self.peso += anos * 0.5

        while (self.idade + 1) < 21:
            self.altura += 0.5
            self.idade += 1

    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura


print('Bem vindo ao programa que faz a projeção do peso e da altura de uma pessoa!')

nome = input('Digite o nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura (cm): '))

pessoa1 = Pessoa(nome, peso, idade, altura)

projecao_anos = int(input('\nProjeção para quantos anos? '))

print(f'\nPeso: {pessoa1.get_peso()}'
      f'\nAltura: {pessoa1.get_altura()} cm')

pessoa1.projecao(projecao_anos)

print(f'\nPeso futuro: {pessoa1.get_peso()}'
      f'\nAltura futura: {pessoa1.get_altura()} cm')
