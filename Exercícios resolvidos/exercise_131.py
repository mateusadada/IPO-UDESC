# Faça um programa que crie um cadastro de alunos com 2 notas. Ao final, imprime o nome e a média de cada aluno
# OBS: crie uma função para cadastrar aluno e outra para imprimir a listagem (nome + média).

def main():
    cadastrar_aluno_e_notas()
    exibir_nome_e_media()


def cadastrar_aluno_e_notas():
    while True:
        nome = input('\nDigite um nome (fim p/ encerrar): ')

        if nome == 'fim':
            break

        nota_1 = float(input('1º nota: '))
        nota_2 = float(input('2º nota: '))

        aluno = nome, nota_1, nota_2

        lista_alunos_e_notas.append(aluno)


def exibir_nome_e_media():
    print(f'\n*** EXIBINDO OS {len(lista_alunos_e_notas)} ALUNOS E SUAS MÉDIAS ***')

    for i, aluno in enumerate(lista_alunos_e_notas):
        print(f'{i + 1}º: {aluno[0]} -> Média {(aluno[1] + aluno[2]) / 2:.2f}')


lista_alunos_e_notas = []

print('Bem vindo ao programa de cadastro de aluno e impressão da mesma a partir de funções (tuplas)!')

main()
