# Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a
# média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

print('Bem-vindo ao programa de cálculo da média final (ponderada) de um aluno!')

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media_final = (nota1 * 2 + nota2 * 3 + nota3 * 5)/10

print(f'\nA média final ponderada é {media_final:.2f}')
