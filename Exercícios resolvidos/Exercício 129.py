# Criando lista de 'tuplas' a partir do nome e de duas notas

lista_alunos_e_notas = []

print('Bem vindo ao programa que armazena o nome e duas notas de um aluno em uma tupla!')

while True:
    nome = input('\nDigite um nome (fim p/ sair): ')

    if nome == 'fim':
        break

    nota_1 = float(input('1º nota: '))
    nota_2 = float(input('2º nota: '))

    aluno = nome, nota_1, nota_2

    lista_alunos_e_notas.append(aluno)

print(f'\n*** EXIBINDO TODOS OS {len(lista_alunos_e_notas)} ALUNOS E AS SUAS NOTAS ***')

for i, aluno in enumerate(lista_alunos_e_notas):
    print(f'{i + 1}º: {aluno}')
