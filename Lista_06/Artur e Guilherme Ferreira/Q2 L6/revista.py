class Revista:
	
	def __init__(self,codigo,titulo,tipo, edicao):
		self.__codigo = codigo
		self.__titulo = titulo
		self.__tipo = tipo
		self.__edicao = edicao
		self.__lista_edicoes = []
		
	def add_revista(self,edicao):
		self.__lista_edicoes.append(edicao)
		
	def listar_edicoes(self):
		print("titulo:",self.__titulo)
		print("codigo:",self.__codigo)
		print("tipo:",self.__tipo)
		print("edicao:",self.__edicao)
		print(25*'~')
		for edicao in self.__lista_edicoes:
			print("num. edicao:",edicao._num)
			print("data da edicao:",edicao._data)
			print("numero de artigos:",edicao._numart)
			print("")