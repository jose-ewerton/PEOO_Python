"""
3.	Crie um diagrama de classes que represente uma classe Pessoa com os atributos privados identificador, nome e CPF, e uma classe Endereço com os atributos número da casa, rua, cidade, estado e pais. Nesse caso uma pessoa deve “agregar” um ou vários endereços. Implemente métodos para representar esse relacionamento.

•	Cardinalidades:

o	Uma Pessoa agrega um ou vários endereços (1 para muitos).
"""

class Pessoa:
	def __init__(self, rg, nome, cpf):
		self.__rg = rg
		self.__nome = nome
		self.__cpf = cpf
		self.lista = []
		
		
	@property
	def rg(self):
	   return self.__rg
	  
	 
	@property
	def nome(self):
	   return self.__nome
	
	@property
	def cpf(self):
	   return self.__cpf
    
    				
	def inserir_endereco(self, endereco):
	  self.lista.append(endereco)
	
	def listar_enderecos(self):
	  for endereco in self.lista:
	    print(endereco.numero, endereco.rua, endereco.cidade, endereco.estado, endereco.pais)
		
		

class Endereco:
	def __init__(self, numero, rua, cidade, estado, pais):
		self.numero = numero
		self.rua = rua 
		self.cidade = cidade
		self.estado = estado
		self.pais = pais


gente = Pessoa(69420, "luis", 704)
print(gente.nome, gente.rg, gente.cpf)
p1= Endereco(294, "cap jose", "cm", "RN", "Brazil")
p2= Endereco(294, "cap jose", "cm", "PB", "Brazil")
p3= Endereco(294, "cap jose", "cm", "SP", "Brazil")
gente.inserir_endereco(p1)
gente.inserir_endereco(p2)
gente.inserir_endereco(p3)
gente.listar_enderecos()
