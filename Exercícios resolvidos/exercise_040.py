# Faça um programa de adição de elementos à lista com append.

print('Bem-vindo ao programa que adiciona números a uma lista!')

lista = []

while True:
    numero = int(input('Digite um número (0 p/ sair): '))

    if numero == 0:
        break

    lista.append(numero)

print(f'\nA lista contém {len(lista)} número(s)'
      f'\nElemento(s): {lista}')
