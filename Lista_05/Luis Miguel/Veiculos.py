class Veiculo:
	def __init__(self, marca, modelo, ano, cor):
		self.__marca = marca
		self.__modelo = modelo
		self.__ano = ano
		self.__cor = cor
	
	
	@property 
	def marca(self):
		return self.__marca
		
	@property
	def modelo(self):
		return self.__modelo
		
	@property
	def ano(self):
		return self.__ano
		
	@property
	def cor(self):
		return self.__cor
	
	def tipodeveiculo(self, tipo):
		self.tipo = tipo
		print(f"o veiculo eh do tipo {tipo}")
		
	def veiculofunfa(self, estado):
		"""
		qual o estado do veiculo entre 0 a 10
		"""
		self.estado = estado
		
		if self.estado >= 7:
		   print("vamo dar um rolê")
		if 3 < self. estado <7:
		   print("tomara que nao de prego")
		if self.estado < 3:
		   print("lixo ambulante")
	    	
		
		
carro = Veiculo("fiat", "uno", 2008, "amarelo")
print(carro.marca, carro.modelo, carro.ano, carro.cor)
carro.tipodeveiculo("carro")
carro.veiculofunfa(5)
