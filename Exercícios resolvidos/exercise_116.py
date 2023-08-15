# Classe Conta Corrente: Crie uma classe para implementar uma conta-corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque.
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. Faça um programa que
# realiza depósitos e saques diversos, informando o saldo a cada operação.

class ContaCorrente:
    numero_da_conta = None
    nome_do_correntista = None
    saldo = 0

    def __init__(self, numero, nome, saldo):
        self.numero_da_conta = numero
        self.nome_do_correntista = nome
        self.saldo = saldo

    def set_nome_do_correntista(self, nome):
        self.nome_do_correntista = nome

    def set_deposito(self, valor):
        self.saldo += valor

    def set_saque(self, valor):
        if self.saldo < valor:
            return print('Não é possível sacar devido não ter saldo suficiente!')
        else:
            self.saldo -= valor

    def get_saldo(self):
        return self.saldo

    def get_nome(self):
        return self.nome_do_correntista


def menu():
    while True:
        print('*** Escolha uma opção ***'
              '\n1 - Alterar o nome'
              '\n2 - Depósito'
              '\n3 - Saque'
              '\n9 - Encerrar')
        escolha = int(input('Opção: '))

        if escolha == 1:
            print(f'\nNome atual: {cliente1.get_nome()}')

            novo_nome = input('Novo: ')

            cliente1.set_nome_do_correntista(novo_nome)

            print(f'Nome atualizado: {cliente1.get_nome()}')

            input()

        elif escolha == 2:
            print(f'\nSaldo: R$ {cliente1.get_saldo():.2f}')

            valor = float(input('Valor para depositar: R$ '))

            cliente1.set_deposito(valor)

            print(f'Saldo atual: R$ {cliente1.get_saldo():.2f}')

            input()

        elif escolha == 3:
            print(f'\nSaldo: R$ {cliente1.get_saldo():.2f}')

            valor = float(input('Valor para sacar: R$ '))

            cliente1.set_saque(valor)

            print(f'Saldo atual: R$ {cliente1.get_saldo():.2f}')

            input()

        elif escolha == 9:
            print('\nFinalizando o programa... Até a próxima!')
            break
        else:
            print('\nNúmero inválido. Tente novamente!\n')


print('Bem vindo ao programa de depósitos e saques de uma conta-corrente!')

conta = int(input('Número da conta: '))
nome = input('Nome do cliente: ')
valor_inicial = float(input('Saldo inicial: R$ '))

cliente1 = ContaCorrente(conta, nome, valor_inicial)

print('\nCliente cadastrado com sucesso!\n')

menu()
