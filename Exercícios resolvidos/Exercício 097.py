# Adicione ao exemplo anterior os atributos tamanho e marca à classe TV. Crie dois objetos TV e atribua tamanhos e
# marcas diferentes. Depois, imprima o valor desses atributos para confirmar a independência dos valores de
# cada instância (objeto).

class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None


print('Bem vindo ao programa usando o método construtor!')

tv_do_quarto = TV()
tv_do_quarto.tamanho = 50
tv_do_quarto.marca = 'Samsung'
print(f'TV DO QUARTO está ligada? {tv_do_quarto.ligada}'
      f'\nCanal: {tv_do_quarto.canal}'
      f'\nTamanho: {tv_do_quarto.tamanho}"'
      f'\nMarca: {tv_do_quarto.marca}')

tv_da_sala = TV()
tv_da_sala.ligada = True
tv_da_sala.canal = 4
tv_da_sala.tamanho = 42
tv_da_sala.marca = 'LG'
print(f'\nTV DA SALA está ligada: {tv_da_sala.ligada}'
      f'\nCanal: {tv_da_sala.canal}'
      f'\nTamanho: {tv_da_sala.tamanho}"'
      f'\nMarca: {tv_da_sala.marca}')
