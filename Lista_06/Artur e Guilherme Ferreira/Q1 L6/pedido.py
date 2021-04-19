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