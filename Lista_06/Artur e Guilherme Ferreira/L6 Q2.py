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
		print("titulo:",self.__titulo,"codigo:",self.__codigo,"tipo:",self.__tipo,"edicao:",self.__edicao)
		for edicao in self.__lista_edicoes:
			print("num. edicao:",edicao._num)
			print("data da edicao:",edicao._data)
			print("numero de artigos:",edicao._numart)
		

class Edicao:
	
	def __init__(self,num,data,numart):
		self._num = num
		self._data = data
		self._numart = numart

revista1 = Revista('123','aaa','bbbb','321',)
edicao1 = Edicao('555','12/02/12','345')

revista1.add_revista(edicao1)
revista1.listar_edicoes()
