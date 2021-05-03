from produto_e_pedido import Produto
from produto_e_pedido import ItemPedido
from produto_e_pedido import Pedido

item = ItemPedido()
pedido = Pedido()

p1 = Produto('Headset Gamer Razer Kraken X Lite','71671',269)
p2 = Produto('Cadeira Gamer Razer Tarok Pro','71672',1.929)
p3 = Produto('Mouse Gamer Razer Deathadder V2','71673',299)

item.adc(p1,4)
item.adc(p2,4)
item.adc(p3,4)

pedido.add_pedido(p1)
pedido.add_pedido(p2)
pedido.add_pedido(p3)

pedido.listar()
pedido.remove_pedido(p2)
pedido.listar()
pedido.valor_total()