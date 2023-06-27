# Escreva uma função que retorne o maior de dois números. Exemplo de valores esperados:
# maior(5,6) = 6
# maior(2,1) = 2
# maior(7,7) = 7

def maior_2_numeros(a, b):
    if a > b:
        return f'O maior número é {a}'
    elif a < b:
        return f'O maior número é {b}'
    else:
        return f'Os dois números ({a}) são iguais'


print('Bem vindo ao programa que exibe qual número é maior entre dois!')

numero_1 = int(input('1º número: '))
numero_2 = int(input('2º número: '))

print(f'\n{maior_2_numeros(numero_1, numero_2)}')
