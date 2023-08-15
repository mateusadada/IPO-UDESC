# Crie uma função que receba uma quantidade x de números e adicione-os a uma lista, em seguida imprima a média
# desses números caso o número adicionado seja a string 'fim'.

def adicao_numeros_lista():
    lista_numeros = []
    while True:
        numero = input('Digite um número (fim p/ encerrar): ')
        if numero == 'fim':
            break
        else:
            lista_numeros.append(int(numero))
    return media(lista_numeros)


def media(lista):
    total = 0
    for i in lista:
        total += i
    return total / (len(lista))


print('Bem-vindo ao programa de cálculo da média!')
print(f'\nA média é {adicao_numeros_lista():.2f}')
