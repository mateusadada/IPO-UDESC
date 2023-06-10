# Crie uma lista de números e crie uma lista com os números pares.

print('Bem vindo ao programa que cria uma nova lista com números pares de outra lista!')

lista = list(range(1, 150, 7))
lista_pares = []

for e in lista:
    if e % 2 == 0:
        lista_pares.append(e)

print(f'\nLista: {lista}'
      f'\nLista dos pares: {lista_pares}')
