# Faça um programa para apagar fatias inteiras de uma só vez usando o range.

from time import sleep

lista = list(range(1, 101))

print(f'\nLista: {lista}'
      f'\n\nApagando o número 2 até o 99...')
sleep(4)

del lista[1:98]

print(f'\nLista: {lista}')
