class Produto:
	
	def __init__(self,nome,id,valor):
		self.nome = nome
		self.id = id
		self.valor = valor
		self.item = None
class ItemPedido:
	
	def __init__(self):
		self.item = None
		self.nome = None
		self.id = None
		self.valor = None
		
	def adicionar(self,produto,item):
		self.nome = produto.nome
		self.id = produto.id
		self.valor = produto.valor
		produto.item = item
		self.item = produto.item
		print("Foi pedido",self.item,"itens do produto",self.nome)