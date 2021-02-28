class Conta:
    def	__init__(self,numero,titular,saldo,limite): #classe construtora
        print("inicializando uma conta")
        self.numero	=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite

    def deposita(self, valor):
        self.saldo+=valor
        print(self.saldo)