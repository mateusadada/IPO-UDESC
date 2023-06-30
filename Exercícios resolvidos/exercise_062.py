# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 3, -2, -4].
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

print('Bem-vindo ao programa que exibe a menor, a maior e a temperatura média!')

temperaturas = [-10, -8, 0, 1, 2, 3, -2, -4]
menor = temperaturas[0]
maior = temperaturas[0]
soma = 0

for e in temperaturas:
    if e < menor:
        menor = e
    if e > maior:
        maior = e
    soma += e

temperatura_media = soma / len(temperaturas)

print(f'Temperaturas: {temperaturas}'
      f'\n\nMenor: {menor}'
      f'\nMaior: {maior}'
      f'\nMédia: {temperatura_media}')
