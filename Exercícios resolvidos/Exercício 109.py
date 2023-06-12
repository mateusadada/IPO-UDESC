# Exemplo de itens fracamente privados.

class ClasseFracamentePrivada:
    _atributo_fracamente_privado = None

    def __init__(self):
        self._atributo_fracamente_privado = 100

    def _metodo_fracamente_privado(self):
        print('Método fracamente privado')


print('Bem vindo ao programa de exemplo de classe fracamente privada!')

teste = ClasseFracamentePrivada()

teste._metodo_fracamente_privado()

print(teste._atributo_fracamente_privado)
