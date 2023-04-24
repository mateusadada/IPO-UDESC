# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo): aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# - salários de R$ 1500,00 em diante: aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário após o aumento.

print('Bem vindo! Este programa calcula os reajustes de salários das Organizações Tabajara.')

salario_atual = float(input('Digite o salário atual: R$ '))

if salario_atual <= 280:
    percentual = 0.20
    valor_aumento = salario_atual * percentual
    novo_salario = salario_atual + valor_aumento
elif 280 < salario_atual <= 700:
    percentual = 0.15
    valor_aumento = salario_atual * percentual
    novo_salario = salario_atual + valor_aumento
elif 700 < salario_atual <= 1500:
    percentual = 0.10
    valor_aumento = salario_atual * percentual
    novo_salario = salario_atual + valor_aumento
else:
    percentual = 0.05
    valor_aumento = salario_atual * percentual
    novo_salario = salario_atual + valor_aumento

print(f'\n- O salário antes do reajuste: R$ {salario_atual:.2f} reais'
      f'\n- O percentual de aumento aplicado: {percentual * 100:.0f}%'
      f'\n- O valor do aumento: R$ {valor_aumento:.2f} reais'
      f'\n- Novo salário: R$ {novo_salario:.2f} reais')
