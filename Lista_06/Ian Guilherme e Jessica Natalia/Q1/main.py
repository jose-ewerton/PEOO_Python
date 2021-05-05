from pedido import Pedido, Produto

p1 = Produto(123,"maçã",1.5)
p2 = Produto(456,"banana",4.25)

pedido=Pedido()

pedido.adicionar_item(p1,5)
pedido.adicionar_item(p2,3)

pedido.listar_produtos()

pedido.remover_item(123)

pedido.listar_produtos()

pedido.obter_valor_total() 