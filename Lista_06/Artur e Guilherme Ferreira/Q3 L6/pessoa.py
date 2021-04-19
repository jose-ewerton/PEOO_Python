class Pessoa:
	
	def __init__(self,nome,cpf,rg):
		self.__nome = nome
		self.__cpf = cpf
		self.__rg = rg
		self.__lista_endereco = []
		
	def add_endereco(self,endereco):
		self.__lista_endereco.append(endereco)
		
	def listar_endereco(self):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("Nome:",self.__nome,"CPF:",self.__cpf,"RG:",self.__rg)
		print("~~~~~~~~~~Endereços Anexados~~~~~~~~~~")
		for endereco in self.__lista_endereco:
			print("Rua:",endereco._rua)
			print("Numero da residencia:",endereco._numero)
			print("Cidade:",endereco._cidade)
			print("Estado:",endereco._estado)
			print("País:",endereco._pais)