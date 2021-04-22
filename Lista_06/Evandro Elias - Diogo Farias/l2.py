class nome:
	
	def __init__(self,codigo,edicao,tipo, titulo):
		self.__codigo = codigo
		self.__titulo = titulo
		self.__tipo = tipo
		self.__edicao = edicao
		self.__lista_edicoes = []
		
	def add_nome(self,edicao):
		self.__lista_edicoes.append(edicao)
		
	def listar_edicoes(self):
		print("title:",self.__titulo,"cod:",self.__codigo,"tipo:",self.__tipo,"edicao:",self.__edicao)
		for edicao in self.__lista_edicoes:
			print("num. edicao:",edicao._num)
			print("data da edicao:",edicao._data)
			print("numero de artigos:",edicao._numart)
		

class Edic:
	
	def __init__(self,num,data,numart):
		self._num = num
		self._data = data
		self._numart = numart

nome1 = nome('veja','988','??','???',)
edic1 = Edic('69','2/3/4','123')

nome1.add_nome(edic1)
nome1.listar_edicoes()
