class Produto:	
	def __init__(self,nome = str, id = int, preco = float):
		self.descricao = nome
		self.id = id
		self.preco = preco
		self.quantidade = None
		
		
class ItemPedido:	
	def __init__(self):
		self.descricao = None
		self.id = None
		self.preco = None
		self.quantidade = None
		
	def adc_produto(self,produto, quantidade):
		self.descricao = produto.descricao
		self.id = produto.id
		self.preco = produto.preco
		produto.quantidade = quantidade
		self.quantidade = produto.quantidade
		print(f"foram {self.quantidade} pedidos  do produto {self.descricao}")
		
		
class Pedido:	
	def __init__(self):
		self.lista_pedido = []
		
	def adc_pedido(self,itempedido):
		self.lista_pedido.append(itempedido)
		
	
	def del_pedido(self,itempedido):
		self.lista_pedido.remove(itempedido)
		print("")
		print(28 * "-", "devolucao", 28* "-")
		print(f"item removido: {itempedido.descricao} ")
		
	def exibir(self):
		print("")
		print(25 * "-", "Lista de Produtos", 25 * "-")
		for itempedido in self.lista_pedido:
			print(f"nome: {itempedido.descricao},codigo: {itempedido.id}, preco: R$ {itempedido.preco}, quantidade: {itempedido.quantidade}")
		
	def vtotal(self):
		print("")
		print(30 * "-", "conta", 30 * "-")
		soma_geral = []
		for precos in self.lista_pedido:
			preco= precos.preco * precos.quantidade
			soma_geral.append(preco)	
		print("valor do pedido: R$",sum(soma_geral))
		

cesta = ItemPedido()
produto1 = Produto('maizena', 69420, 2.50)
produto2 = Produto('ovos', 101010, 14)
produto3 = Produto('refri', 190103, 5.50)
cesta.adc_produto(produto1, 10)
cesta.adc_produto(produto2, 10)
cesta.adc_produto(produto3, 10)

pedido = Pedido()
pedido.adc_pedido(produto1)
pedido.adc_pedido(produto2)
pedido.adc_pedido(produto3)

pedido.exibir()
pedido.del_pedido(produto2)
pedido.vtotal()	
