# Classe Produto,codigo do produto, descrição e valor 
class Produto:
    def __init__(self, codigo, descricao, valor):
        self.__codigo= codigo
        self.__descricao = descricao
        self.__valor= valor
    
    @property   #getter  -pegar ou obter
    def codigo(self):
        return self.__codigo 
    
    @codigo.setter  #setter - inserir
    def codigo(self,codigo):
        self.__codigo = codigo

    @property   #getter  -pegar ou obter
    def descricao(self):
        return self.__descricao
    
    @descricao.setter  #setter - inserir
    def descricao(self,descricao):
        self.__descricao = descricao

    @property   #getter  -pegar ou obter
    def valor(self):
        return self.__valor
    
    @valor.setter  #setter - inserir
    def valor(self,valor):
        self.__valor = valor

    def detalha_produto(self):
        print ("...............Informações do Produto...............")
        print("Codigo do produdo: {0}".format(self.__codigo))
        print("Descrição do produto: {0}".format(self.__descricao))
        print("Valor do pruduto: {0}".format(str(self.__valor)))
        

        

 


