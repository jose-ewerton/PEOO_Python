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

'''    
    def __repr__(self):       #retorna uma string que descreve o ponteiro do objeto por padrão (se o programador não o definir).
            return '{},{}'.format(self.numero, self.titular)

    def __str__(self): #retorna o objeto como string
        return self.__repr__()
'''
if ( __name__ =='__main__'):
    print('Dentro da função!')
    c = Conta(1,2,3,4)
    print(c.__repr__ ())
    print(c.__str__ ())
    print(c)
