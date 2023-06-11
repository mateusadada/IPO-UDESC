# Exemplo de pesquisa em uma lista.

def procurar(number):
    for i, e in enumerate(lista):
        if e == number:
            return f'\nFoi encontrado o número {e} na posição {i + 1}'
    else:
        return f'\nNão foi encontrado o número {number} na lista'


lista = list(range(1, 200, 17))

print('Bem vindo ao programa que procura um número em uma lista a partir de uma função!'
      f'\nLista: {lista}')
numero = int(input('Digite um número: '))

print(procurar(numero))
