# Crie uma lista de palavras e crie uma lista com as palavras que têm mais de 5 caracteres.

print('Bem-vindo ao programa que cria uma lista de palavras com mais de 5 caracteres de outra lista!')

lista = ['casa', 'bola', 'tesoura', 'mansão', 'tecnologia', 'universidade', 'arte', 'design', 'moldura']
nova_lista = []

for e in lista:
    if len(e) > 5:
        nova_lista.append(e)

print(f'\nLista: {lista}'
      f'\nNova lista: {nova_lista}')
