# Crie uma lista de números e calcule a diferença entre o maior e o menor valor.

print('Bem vindo ao programa de cálculo da diferença entre o maior e o menor valor!')

lista = [4, 8, -54, 254, 21, -98, 54, 2, 74, 65, -42]
maior = lista[0]
menor = lista[0]

print(f'Lista: {lista}')

for e in lista:
    if e > maior:
        maior = e
    if e < menor:
        menor = e

diferenca = maior - menor

print(f'\nMaior: {maior}'
      f'\nMenor: {menor}'
      f'\nDiferença entre os dois: {diferenca}')
