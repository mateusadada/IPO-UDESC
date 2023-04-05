# Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimir 10, 9, 8, ..., 1, 0 e FOGO! na tela

import time

x = 10

while x >= 0:
    print(x)
    time.sleep(1)
    x -= 1

print('FOGO!!!')
