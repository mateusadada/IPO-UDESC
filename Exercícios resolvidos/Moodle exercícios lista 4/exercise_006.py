# Crie uma função que receba uma lista como parâmetro e retorne o valor máximo da lista.

def valor_maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


numeros = []

print('Bem vindo ao programa que retorna o valor máximo de uma lista!')

while True:
    numero = int(input('Digite um número (0 p/ sair): '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

print(f'\nLista: {numeros}'
      f'\nO valor máximo é {valor_maximo(numeros)}')
