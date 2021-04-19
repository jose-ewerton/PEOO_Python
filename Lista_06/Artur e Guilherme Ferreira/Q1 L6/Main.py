from produto import Produto
from produto import ItemPedido
from pedido import Pedido

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