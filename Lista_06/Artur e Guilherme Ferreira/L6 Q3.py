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
		

class Endereco:
	
	def __init__(self,numero,rua,cidade,estado,pais):
		self._numero = numero
		self._rua = rua
		self._cidade = cidade
		self._estado = estado
		self._pais = pais

pessoa1 = Pessoa('Artur','00000','000111')
endereco1 = Endereco('555','rua x','cidade x','estado x','país x')
endereco2 = Endereco('556','rua y','cidade y','estado y','país y')

pessoa1.add_endereco(endereco1)
pessoa1.add_endereco(endereco2)

pessoa2 = Pessoa('Presidente','00001','000222')
endereco3 = Endereco('655','rua z','cidade z','estado z','país z')
endereco4 = Endereco('656','rua y','cidade w','estado w','país w')

pessoa2.add_endereco(endereco3)
pessoa2.add_endereco(endereco4)

pessoa1.listar_endereco()
pessoa2.listar_endereco()