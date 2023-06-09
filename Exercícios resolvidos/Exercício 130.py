# Manipulando as tuplas da lista 'lista_alunos_e_notas' para incluir a média

lista_alunos_e_notas = []

print('Bem vindo ao programa que armazena o nome e duas notas de um aluno em uma tupla e exibe a média!')

while True:
    nome = input('\nDigite um nome (fim p/ sair): ')

    if nome == 'fim':
        break

    nota_1 = float(input('1º nota: '))
    nota_2 = float(input('2º nota: '))

    aluno = nome, nota_1, nota_2

    lista_alunos_e_notas.append(aluno)

print(f'\n*** EXIBINDO TODOS OS {len(lista_alunos_e_notas)} ALUNOS, AS NOTAS E AS MÉDIAS ***')

for i, aluno in enumerate(lista_alunos_e_notas):
    print(f'{i + 1}º: {aluno[0]} -> Média: {(aluno[1] + aluno[2]) / 2:.2f}')
