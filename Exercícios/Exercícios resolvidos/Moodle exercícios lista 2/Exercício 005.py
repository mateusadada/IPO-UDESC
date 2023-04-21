# Faça um programa que leia duas notas de um aluno e calcule a média. Se a média for maior ou igual a 6
# está em recuperação, se for maior ou igual a 8 está aprovado, caso contrário, está reprovado

print('Bem vindo! Este programa informa a situação final do aluno.')

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2º nota: '))

media = (nota1 + nota2) / 2

if media >= 8:
    print(f'\nO aluno está APROVADO com a média {media:.1f}')
elif media < 6:
    print(f'\nO aluno está REPROVADO com a média {media:.1f}')
else:
    print(f'\nO aluno está em RECUPERAÇÃO com a média {media:1.1f}')
