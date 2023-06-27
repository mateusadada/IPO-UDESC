# Manipulando listas e tuplas.
# Exemplo: lista contendo vendedores e vendas realizadas, imprimindo relatório de vendas.

print('Bem vindo ao programa de relatório de vendas!')

lista = []
vendas_gerais = 0

cliente_1 = ('João', 213.00, 333.00, 600.00)
cliente_2 = ('Carlos', 1212.00, 20.00, 555.00, 10.00, 654.00, 1592.23, 11.11)

lista.append(cliente_1)
lista.append(cliente_2)

for e in lista:
    print(f'\nNome: {e[0]}'
          f'\nNúmero de vendas: {len(e) - 1}')

    total_cliente = 0
    i = 1

    while i < (len(e)):
        print(f'R$ {e[i]:17.2f} reais')

        total_cliente += e[i]
        vendas_gerais += e[i]
        i += 1

    print('--------------------------')
    print(f'Subtotal: R$ {total_cliente:.2f} reais')

print('\n-------------------------------')
print(f'Vendas gerais: R$ {vendas_gerais:.2f} reais')
print('-------------------------------')
