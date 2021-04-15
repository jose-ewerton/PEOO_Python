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
		
		
class Pedido:
	
	def __init__(self):
		self.lista_pedido = []
		
	def add_pedido(self,itempedido):
		self.lista_pedido.append(itempedido)
		print(itempedido.nome,"foi adicionado a lista")
	
	def remove_pedido(self,itempedido):
		self.lista_pedido.remove(itempedido)
		print(itempedido.nome,"foi removido da lista")
		
	def listar(self):
		print("")
		print("Lista de Produtos:")
		for itempedido in self.lista_pedido:
			print("Nome:",itempedido.nome,"Codigo:",itempedido.id,"Valor(unidade): R$",itempedido.valor,"quantidade:",itempedido.item)
		
	def valor_total(self):
		total = []
		for itempedido in self.lista_pedido:
			valor= itempedido.valor * itempedido.item
			total.append(valor)	
		print("O valor total é de R$",sum(total))
		

item = ItemPedido()
pedido = Pedido()

p1 = Produto('arroz','00000',4)
p2 = Produto('feijao','00001',5.5)
p3 = Produto('farinha','00002',3)

item.adicionar(p1,10)
item.adicionar(p2,10)
item.adicionar(p3,10)

pedido.add_pedido(p1)
pedido.add_pedido(p2)
pedido.add_pedido(p3)

pedido.listar()
pedido.remove_pedido(p1)
pedido.listar()
pedido.valor_total()		