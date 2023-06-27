# Cadastrando strings e procurando por substring.

lista = []
FLAG = 0

print('Bem vindo ao programa que procura um nome em nome completo!')

while True:
    nome = input('Digite um nome (fim p/ sair): ')

    if nome == 'fim':
        break
    else:
        lista.append(nome)

nome_procurar = input('\nProcurar por: ')

for i, e in enumerate(lista):
    if nome_procurar in e:
        print(f'Foi encontrado na posição {i + 1} o nome {e}')
        FLAG += 1

if FLAG < 1:
    print(f'\nNão foi encontrado o nome {nome_procurar}')
