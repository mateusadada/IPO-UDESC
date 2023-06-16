# Encapsulamento. Alterando a classe Conta para adicionar um atributo que é a lista de operações realizadas.

class Conta:
    _saldo = 0
    __clientes = None
    __numero = None

    def __init__(self, clientes, numero, saldo):
        self._saldo = saldo
        self.__clientes = clientes
        self.__numero = numero
        self._operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f'CC Número; {self.__numero} | Saldo: {self._saldo}')

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._operacoes.append(['Saque: ', valor])

    def deposito(self, valor):
        self._saldo += valor
        self._operacoes.append(['Depósito: ', valor])

    def extrato(self):
        print(f'\nExtrato CC Nr: {self.__numero}')

        for e in self._operacoes:
            print("%10s%10.2f" % (e[0], e[1]))

        print(f'Saldo: {self._saldo:10.2f}')
