# Exemplo de cálculo da média.

def media(numeros):
    total = 0
    for e in numeros:
        total += e
    return total / len(numeros)


lista = list(range(1, 50, 4))

print('Bem-vindo ao programa de cálculo da média de uma lista a partir de uma função!'
      f'\nLista: {lista}'
      f'\n\nMédia dos números: {media(lista):.1f}')
