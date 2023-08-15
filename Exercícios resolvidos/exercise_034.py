print('Bem-vindo ao programa de cálculo da média de notas informadas!')

quantidade = int(input('Digite a quantidade de notas: '))
soma = 0
notas = []

for i in range(0, quantidade):
    notas.append(float(input(f'Informe a {i + 1}º nota: ')))
    soma += notas[i]

print(f'\nA média das {quantidade} notas é {soma / quantidade:.2f}')
