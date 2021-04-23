from produto import Produto
from produto import ItemPedido
from pedido import Pedido

item = ItemPedido()
pedido = Pedido()

p1 = Produto('banana','00',2.5)
p2 = Produto('mandioca','01',5.5)
p3 = Produto('pepino','02',3)
p4 = Produto('mamadeira', '03',1)

item.adicionar(p1,12)
item.adicionar(p2,5)
item.adicionar(p3,3)
item.adicionar(p4,1)

pedido.adc_pedido(p1)
pedido.adc_pedido(p2)
pedido.adc_pedido(p3)
pedido.adc_pedido(p4)

pedido.listar_produtos()
pedido.remover_pedido(p3)
pedido.listar_produtos()
pedido.valor_total()