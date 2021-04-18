
from Produto import Produto, ItemPedido, Pedido


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
