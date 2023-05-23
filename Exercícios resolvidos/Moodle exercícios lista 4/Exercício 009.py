# Faça uma função chamada 'procura' que recebe 2 argumentos: uma 'lista' com nomes de alunos e um 'nome' a procurar,
# retornando 'True' se o nome foi encontrado ou 'False' caso não encontre.

def procurar_nome(lista, nome):
    for i in lista:
        if i == nome:
            return f'True! O nome {nome} está na lista!'
    else:
        return f'False! O nome {nome} NÃO está na lista!'


lista_nomes = ['Mateus', 'Julia', 'Livia', 'Ana', 'João', 'Cristiane', 'Paulo']

print('Bem vindo ao programa que verifica se um nome está em uma lista!'
      f'\nLista: {lista_nomes}')

nome_a_procurar = input('\nProcurar qual nome? ')

print(procurar_nome(lista_nomes, nome_a_procurar))
