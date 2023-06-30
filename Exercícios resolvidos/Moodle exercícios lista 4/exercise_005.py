# Faça uma função chamada calculaPreco, que recebe 2 parâmetros ('valor' da compra e 'desconto' em percentual).
# A função deve retornar o preço final do produto.

def calculaPreco(valor_inicial, desconto_percentual):
    preco_final = valor_inicial - (valor_inicial * desconto_percentual / 100)
    return preco_final


print('Bem-vindo ao programa de cálculo de desconto de um produto!')

preco = float(input('Valor da compra: R$ '))
desconto = float(input('Desconto (%): '))

print(f'\nO valor do produto com desconto de {desconto}% é R$ {calculaPreco(preco, desconto):.2f} reais')
