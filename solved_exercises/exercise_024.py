# Faça um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no período.

print('Bem vindo ao programa de cálculo de juros ganhos na poupança em 12 meses!')

saldo = float(input('Quanto é o depósito inicial? R$ '))
taxa_juros = float(input('Qual é a taxa de juros em porcentagem? '))/100

i = 1
juros = 0

print()

while i <= 12:
    juros += saldo * taxa_juros
    saldo += saldo * taxa_juros
    print(f'{i}º mês: R$ {saldo:.2f} reais')
    i += 1

print(f'\nGanho total com juros no período: R$ {juros:.2f} reais')
