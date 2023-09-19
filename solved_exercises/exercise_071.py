# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
# Exemplo de valores esperados: múltiplo(8,4) = True

def multiplo(a, b):
    return a % b == 0


print('Bem vindo ao programa que informa se um número é múltiplo do outro!')
numero_1 = int(input('1º número: '))
numero_2 = int(input('2º número: '))

print(f'\nO {numero_1} é múltiplo do {numero_2}? {multiplo(numero_1, numero_2)}')
