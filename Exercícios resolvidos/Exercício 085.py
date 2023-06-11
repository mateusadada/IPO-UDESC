# Exemplo de parâmetros opcionais.

def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    else:
        return s


print('Bem vindo ao programa de exemplo utilizando parâmetros opcionais em uma função!')

soma(2, 3)
soma(3, 4, True)
soma(5, 8, False)
