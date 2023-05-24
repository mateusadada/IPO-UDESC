# Exemplo de parâmetros opcionais

def barra_1():
    return '*' * 40


def barra_2(n = 40, caractere = '-'):
    return caractere * n


print('Bem vindo ao programa que exibe dois estilos de barras a partir de funções!')

print(f'\nEstilo 1: {barra_1()}')
print(f'Estilo 2: {barra_2()}')
print(f'Estilo 3: {barra_2(20, "/")}')
