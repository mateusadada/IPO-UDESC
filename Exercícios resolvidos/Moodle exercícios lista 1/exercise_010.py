# Digite uma frase e imprima a quantidade de vogais presentes na frase.

print('Bem-vindo ao programa que informa a quantidade de vogais de um texto!')

texto = input('Digite uma frase: ')

letras = 'aeiouAEIOU'  # caracteres para procurar e somar
quantidade_total = len(letras)
i = 0
soma_total = 0

while i < quantidade_total:
    soma_total += texto.count(letras[i])
    i += 1

print(f'\nA quantidade de vogais na frase é {soma_total}')
