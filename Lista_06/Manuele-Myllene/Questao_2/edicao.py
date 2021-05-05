'''
Crie um diagrama de classes que represente uma classe Revista com os atributos privados 
código, título, tipo, edição, e uma classe Edição contendo os atributos privados número da 
edição, data da edição e número de artigos. Lembre-se que uma revista “contém” várias
edições e implemente métodos para representar esse relacionamento.
'''

class Edicao:
    def __init__(self, n_edicao, d_edicao, n_artigos):
        self.n_edicao = n_edicao
        self.d_edicao = d_edicao
        self.n_artigos = n_artigos
    
    

    def info_edicao(self):
        print("----------INFORMAÇÕES DA EDIÇÃO----------")
        print("Número da edição: {0}".format(self.n_edicao))
        print("Data da edição: {0}".format(self.d_edicao))
        print("Número de artigos: {0}".format(self.n_artigos))

