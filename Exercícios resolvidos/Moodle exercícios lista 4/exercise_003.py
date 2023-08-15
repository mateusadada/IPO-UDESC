# Faça uma função que receba 4 notas de uma disciplina e que retorne a média das notas.

def media(a, b, c, d):
    return (a + b + c + d) / 4


print('Bem vindo ao programa de cálculo da média de quatro notas de uma disciplina!')

lista = []

for i in range(4):
    nota = float(input(f'{i + 1}º nota: '))
    lista.append(nota)

print(f'\nA média das notas é {media(lista[0], lista[1], lista[2], lista[3]):.2f}')
