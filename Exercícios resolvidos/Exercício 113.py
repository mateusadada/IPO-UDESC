# Classe Quadrado: Crie uma classe que modele um quadrado:
#   Atributos: Tamanho do lado
#   Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, lado=456):
        self.__tamanho_lado = lado

    def __set_tamanho_lado(self, lado):
        self.__tamanho_lado = lado

    def get_tamanho_lado(self):
        return self.__tamanho_lado

    def __calcular_area(self):
        return pow(self.__tamanho_lado, 2)


teste = Quadrado()

print('Bem vindo ao programa de cálculo da área de um quadrado!'
      f'\nValor inicial do lado do quadrado: {teste.get_tamanho_lado()}'
      f'\nÁrea: {teste._Quadrado__calcular_area()}m²')

novo_lado = int(input('\nDigite um novo lado: '))

teste._Quadrado__set_tamanho_lado(novo_lado)

print(f'\nNovo lado informado: {teste.get_tamanho_lado()}'
      f'\nÁrea: {teste._Quadrado__calcular_area()}m²')
