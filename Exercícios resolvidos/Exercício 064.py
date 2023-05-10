# Faça um programa que leia N valores inteiros, e depois apresente-os em ordem crescente.

print('Bem vindo ao programa que exibe uma lista em ordem crescente de números informados!')

lista = []

quantidade = int(input('Informar quantos números? '))

for i in range(quantidade):
    lista.append(int(input(f'{i + 1}º número: ')))

print(f'\nLista: {lista}')

for i in range(0, len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(f'\nLista crescente: {lista}')
