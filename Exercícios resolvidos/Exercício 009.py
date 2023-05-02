# Exemplo 5 do PDF Slides da aula - Parte 5

print('Bem vindo ao programa que mostra o preço do produto dependendo da categoria!')

categoria = int(input('Digite a categoria do produto: '))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('\nCategoria inválida!')
    preco = 0

print(f'\nO preço do produto é de R$ {preco:.2f} reais')
