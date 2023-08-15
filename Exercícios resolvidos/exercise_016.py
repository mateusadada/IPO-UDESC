# Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimir 10, 9, 8, ..., 1, 0 e DECOLAR na tela.

import time

print('Bem-vindo ao programa que exibe a contagem regressiva do lançamento de um foguete!')

x = 10

while x >= 0:
    time.sleep(1)
    print(x)
    x -= 1

print('\n***DECOLAR***')
