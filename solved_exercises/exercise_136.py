# No exemplo do Banco X, para atrair novos clientes, o banco começou a oferecer contas especiais. Uma conta especial
# permite que se possa sacar mais dinheiro que o saldo disponível na conta, até um determinado limite. As operações de
# depósito, extrato e resumo são as mesmas de uma conta normal. Para tal, pode-se criar uma classe ContaEspecial
# herdando o comportamento da classe Conta (Exercício122).

from Exercício122 import Conta


class ContaEspecial(Conta):
    __limite = None

    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.__limite = limite

    def saque(self, valor):
        if self._saldo + self.__limite >= valor:
            self._saldo -= valor
            self._operacoes.append((['Saque: R$ ', valor]))
