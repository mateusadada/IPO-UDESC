# Faça um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte quantos meses para pagar a dívida. Imprima o novo valor da dívida incluindo os juros

saldo = float(input('Quanto é o valor inicial da dívida? R$ '))
juro_mensal = float(input('Quanto é o juro ao mês (%)? '))/100
meses_para_pagar = int(input('Quantos meses para pagar a dívida? '))

print('\n*** DÍVIDA ATUALIZADA COM JUROS ***')

i = 1
juros = 0

while i <= meses_para_pagar:
    juros += saldo * juro_mensal
    saldo += saldo * juro_mensal
    print(f'{i}º mês: R$ {saldo:.2f} reais')
    i += 1

print(f'\nTotal de juros: R$ {juros:.2f} reais')
