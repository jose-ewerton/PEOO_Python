from pedidoo import Pedido, Produto

produto1=Produto(342,"abacaxi",12.5)
produto2=Produto(564,"uva",30.0)
produto3=Produto(986,"melancia",9.4)


pedido=Pedido()
pedido.adicionar_item(produto1,1)
pedido.adicionar_item(produto2,1)
pedido.adicionar_item(produto3,1)
pedido.listar_produtos()

pedido.remover_item()
pedido.listar_produtos()

pedido.obter_valor_total() 
