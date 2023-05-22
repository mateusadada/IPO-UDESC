# Modifique a função acima (exercício 003) recebendo as 4 notas e o peso de cada nota.

def media(a, a1, b, b1, c, c1, d, d1):
    return (a * a1 + b * b1 + c * c1 + d * d1) / (a1 + b1 + c1 + d1)


print('Bem vindo ao programa de cálculo da média ponderada de quatro notas de uma disciplina!')

notas = []
peso_notas = []

for i in range(4):
    nota = float(input(f'\n{i + 1}º nota: '))
    notas.append(nota)
    peso = int(input(f'{i + 1}º peso: '))
    peso_notas.append(peso)

print(f'\nA média das notas é {media(notas[0], peso_notas[0], notas[1], peso_notas[1], notas[2], peso_notas[2], notas[3], peso_notas[3]):.2f}')
