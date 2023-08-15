# Criar um cadastro dos alunos de IPOO, contendo nome e 4 notas. Imprimir nome e média semestral de cada aluno.
# ao final, imprimir quantidade de alunos e média de notas da turma.

def main():
    print('Bem vindo ao programa de cálculo da média semestral e da turma de 4 notas!')

    while True:
        nome = input('\nInforme um nome (fim p/ sair): ')

        if nome == 'fim':
            break

        nota_1 = float(input('1º nota: '))
        nota_2 = float(input('2º nota: '))
        nota_3 = float(input('3º nota: '))
        nota_4 = float(input('4º nota: '))

        cadastrar_aluno_e_notas(nome, nota_1, nota_2, nota_3, nota_4)

    if len(lista_aluno_e_notas) < 1:
        print('\nErro! Não foi informado nenhum nome')
    else:
        impressao_media_semestral(lista_aluno_e_notas)
        impressao_media_total(lista_aluno_e_notas)


def cadastrar_aluno_e_notas(nome, nota1, nota2, nota3, nota4):
    aluno = nome, nota1, nota2, nota3, nota4
    lista_aluno_e_notas.append(aluno)


def impressao_media_semestral(lista):
    print('\n*** NOMES E MÉDIA SEMESTRAL ***')
    for i, aluno in enumerate(lista):
        print(f'{i + 1}º: {aluno[0]} -> Média semestral: {(aluno[1] + aluno[2] + aluno[3] + aluno[4]) / 4:.2f}')


def impressao_media_total(lista):
    total = 0

    print(f'\nQuantidade de alunos: {len(lista)}')

    for aluno in lista:
        total += (aluno[1] + aluno[2] + aluno[3] + aluno[4]) / 4

    print(f'Média da turma: {total / len(lista):.2f}')


lista_aluno_e_notas = []
main()
