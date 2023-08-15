# Ler e armazenar num vetor 5 números float fornecidos pelo usuário e calcular a média dos valores.

print('Bem-vindo ao programa de cálculo da média de cinco números!')

numeros = []
soma = 0

for e in range(0, 5):
    numeros.append(float(input(f'Digite um número ({e + 1}/5): ')))
    soma += numeros[e]

media = soma / 5

print(f'\nLista: {numeros}'
      f'\nA média dos valores informados é {media:.2f}')
