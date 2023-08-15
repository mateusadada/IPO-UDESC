# Crie uma função que receba uma lista como parâmetro e retorne a mesma lista na ordem inversa.

def ordem_inversa(lista):
    lista.reverse()
    return lista


numeros = []

print('Bem-vindo ao programa que exibe a ordem inversa de uma lista!')

while True:
    numero = int(input('Digite um número (0 p/ sair): '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

print(f'\nLista: {numeros}'
      f'\nA ordem inversa é {ordem_inversa(numeros)}')
