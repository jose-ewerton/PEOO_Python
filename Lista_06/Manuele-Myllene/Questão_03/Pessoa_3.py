from Endereco import Endereco
	#Crie um diagrama de classes que represente uma classe Pessoa com os atributos privados identificador, 
    #nome e CPF, e uma classe Endereço com os atributos número da casa, rua, cidade, estado e pais. Nesse caso 
    #uma pessoa deve “agregar” um ou vários endereços. Implemente métodos para representar esse relacionamento.
	#Cardinalidades:
	#Uma Pessoa agrega um ou vários endereços (1 para muitos).

#class_  indetificação
# nome, cpf


class Pessoa:
    enderecos =[]
    def __init__(self, nome, cpf,*ender):
        self.nome = nome
        self.cpf = cpf
        for endereco in ender: 
            self.enderecos.append(endereco)
        
    

    def detalhar_pessoa(self): 
        print("...............Mostrando informações da pessoa...............")
        print("Nome: {0}".format(self.nome))
        print("Cpf: {0}".format(self.cpf))
        for endereco in self.enderecos:
            print("=-"*30)
            print(f'Nº_da casa:{endereco.n_casa}')
            print(f'Cidade:{endereco.cidade}')
            print(f'Estado:{endereco.estado}')
       
         



      



    


 
