# Exemplo de itens fortemente privados.

class ClasseFortementePrivada:
    __atributo_fortemente_privado = None

    def __init__(self):
        self.__atributo_fortemente_privado = 100

    def __metodo_fortemente_privado(self):
        print('Método fortemente privado')


print('Bem vindo ao programa de exemplo de classe fortemente privada!')

teste = ClasseFortementePrivada()

teste._ClasseFortementePrivada__metodo_fortemente_privado()

print(teste._ClasseFortementePrivada__atributo_fortemente_privado)
