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
	  print(f"o individuo {self.nome} foi adcionado,\nCpf: {self.cpf},\nRg: {self.rg}")
	
	def listar_enderecos(self):
	  for endereco in self.lista:
	    print("")
	    print(f"enderecos de {self.nome}: ")
	    print("")
	    print(f"Numero : {endereco.numero},\nRua: {endereco.rua},\nCidade: {endereco.cidade},\nEstado: {endereco.estado},\npais: {endereco.pais}")
		
		

class Endereco:
	def __init__(self, numero, rua, cidade, estado, pais):
		self.numero = numero
		self.rua = rua 
		self.cidade = cidade
		self.estado = estado
		self.pais = pais
