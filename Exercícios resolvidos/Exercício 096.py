# Método Construtor de um aparelho de tv. Pode-se fazer com a TV, por exemplo, mudança de canal, ligá-la ou desligá-la.

class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 2


print('Bem vindo ao programa usando o método construtor!')

tv_do_quarto = TV()
print(tv_do_quarto.ligada)
print(tv_do_quarto.canal)

tv_da_sala = TV()
tv_da_sala.ligada = True
tv_da_sala.canal = 4
print(tv_da_sala.ligada)
print(tv_da_sala.canal)
