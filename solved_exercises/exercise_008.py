# Exemplo 4 do PDF Slides da aula - Parte 5.

print('Bem vindo ao programa que mostra o preço do produto dependendo da categoria!')

categoria = int(input('Digite a categoria do produto (1 a 5): '))

if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print('\nCategoria inválida')
                    preco = 0

print(f'\nO preço do produto é de R$ {preco:.2f} reais')
