# Classe Produto,codigo do produto, descrição e valor 
class Produto:
    def __init__(self, codigo, descricao, valor):
        self.__codigo= codigo
        self.__descricao = descricao
        self.__valor= valor


    def detalha_produto(self):
        print ("...............Informações do Produto...............")
        print("Codigo do produdo: {0}".format(self.__codigo))
        print("Descrição do produto: {0}".format(self.__descricao))
        print("Valor do pruduto: {0}".format(self.__valor))
        

        

 


