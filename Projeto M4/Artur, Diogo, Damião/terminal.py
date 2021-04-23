class Produto:
	'''
	Bem Vindo!
	
	nome = atributo responsavel pelo nome;
	id = atributo responsavel pela numeração do produto;
	preco = atributo responsavel pelo valor do produto.
	
	nome.setter = Responsavel para que não atribua valores int ou float ao atributo nome;
	id.setter = Responsavel para que não atribua valores str ou float ao atributo id;
	preco.setter = Responsavel para que não atribua valores str ao atributo preco.
	'''
	
	def __init__(self,nome = None,id = None,preco = 0):
		self.nome = nome
		self.id = id
		self.preco = preco

	@property
	def id(self):
		return self._id
	
	@id.setter
	def id(self, codigo):
		if codigo == None:
			pass
		elif len(codigo) == 5:
			pass
		else:
			codigo = 'erro'
		self._id = codigo
	
	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self,name):
		if isinstance(name,str):
			pass
		else:
			name = 'erro'
		self._nome = name
	
	@property
	def preco(self):
		return self._preco
	
	@preco.setter
	def preco(self,valor):
		if isinstance(valor,str):
			valor = 'erro'
		else:
			pass
		self._preco = valor

class Novo:	
	'''
	nome = atributo responsavel pela atualização do atributo produto.nome;
	id = atributo responsavel pela atualização do atributo produto.id;
	preco = atributo responsavel pela atualização do atributo produto.preco
	
	Os setter dessa classe possuem a mesma finalidade dos setter da classe Produto.
	'''

	def __init__(self,nome = None,id = None,preco = 0):
		self.nome = nome
		self.id = id
		self.preco = preco
		
	@property
	def id(self):
		return self._id
	
	@id.setter
	def id(self, codigo):
		if codigo == None:
			pass
		elif len(codigo) == 5:
			pass
		else:
			codigo = 'erro'
		self._id = codigo
	
	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self,name):
		if isinstance(name,str):
			pass
		else:
			name = 'erro'
		self._nome = name
	
	@property
	def preco(self):
		return self._preco
	
	@preco.setter
	def preco(self,valor):
		if isinstance(valor,str):
			valor = 'erro'
		else:
			pass
		self._preco = valor

class Listagem:
	'''
	_lista = atributo responsavel pelo armazenamento dos dados da classe Produto e da classe Novo, o " _ " serve como encapsulamento de proteção.
	
	Add = metodo responsavel pela adição de novos dados da classe produto dentro do atributo lista;
	Remove = metodo responsavel pela remoção de determinado dado ja existente dentro do atributo lista;
	Atualizar = metodo responsavel pela atualização de dados no atributo lista, ele irá remover determinado dado da classe Produto e inserir um novo dado da classe Novo;
	Listar = metodo responsavel de mostrar os valores atuais dentro do atributo lista.
	'''
	
	def __init__(self):
		self._lista = []
		
	def Add (self,produto):
		self._lista.append(produto)
		print(produto.nome,"foi adicionado")
		print('')
	
	def Remove(self,i):
		del self._lista[i]
	
	def Atualizar(self,produto,novo, i = 0):
		del self._lista[i]
		self._lista.insert(i,novo)
		print(produto.nome,"foi atualiado para",novo.nome)
		print('')
		
	def Listar(self):
		print('Lista Atual:')
		if len(self._lista) != 0:
			vazio = ""
			for produto in self._lista:
				print("Nome:",produto.nome,"Codigo:",produto.id,"Valor: R$",produto.preco)
				vazio += f'Nome:{produto.nome}     Codigo:{produto.id}     Valor: R${produto.preco}\n'
			return vazio
		else:
			return "Sem Produtos"
			
