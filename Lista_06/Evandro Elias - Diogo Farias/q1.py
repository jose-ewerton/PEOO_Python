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
		print("pedido",self.item,"unidades",self.nome)
		
		
class Pedido:
	
	def __init__(self):
		self.lista_pedido = []
		
	def add_pedido(self,itempedido):
		self.lista_pedido.append(itempedido)
		print(itempedido.nome,"adicionado")
	
	def remove_pedido(self,itempedido):
		self.lista_pedido.remove(itempedido)
		print(itempedido.nome,"removido")
		
	def listar(self):
		print("")
		print("Lista:")
		for itempedido in self.lista_pedido:
			print("Nome:",itempedido.nome,"[Codigo]:",itempedido.id,"[preço]: R$",itempedido.valor,"[unidades]:",itempedido.item)
		
	def valor_total(self):
		total = []
		for itempedido in self.lista_pedido:
			valor= itempedido.valor * itempedido.item
			total.append(valor)	
		print("total R$:",sum(total))
		

item = ItemPedido()
px = Pedido()

p1 = Produto('lapis de cor','0',15)
p2 = Produto('Bloco de folhas','01',25)
p3 = Produto('lapiseira','02',3)

item.adicionar(p1,1)
item.adicionar(p2,1)
item.adicionar(p3,1)

px.add_pedido(p1)
px.add_pedido(p2)
px.add_pedido(p3)

px.listar()
px.remove_pedido(p1)
px.listar()
px.valor_total()	
