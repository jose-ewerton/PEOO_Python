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
    
    				
	def inserir_end(self, end):
	  self.lista.append(end)
	
	def listar_enderecos(self):
	  for end in self.lista:
	    print(end.numerodacasa, end.rua, end.cidade, end.estado, end.pais)
		
		

class Ende:
	def __init__(self, numerodacasa, rua, cidade, estado, pais):
		self.numerodacasa = numerodacasa
		self.rua = rua 
		self.cidade = cidade
		self.estado = estado
		self.pais = pais


p = Pessoa(76, "shadow", 24)
print(p.nome, p.rg, p.cpf)
e1= Ende(294, "curralinho", "natal", "MG", "Brazil")
e2= Ende(294, "curralinho", "?", "baixa do rato", "Brazil")
e3= Ende(294, "curralinho", "natal", "RJ", "Brazil")
p.inserir_end(e1)
p.inserir_end(e2)
p.inserir_end(e3)
p.listar_enderecos()
