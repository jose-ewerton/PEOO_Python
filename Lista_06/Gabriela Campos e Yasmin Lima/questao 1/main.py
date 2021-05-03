from pedido import Pedido, Produto

produto1=Produto(012,"mamão",10.5)
produto2=Produto(043,"morango",7.0)
produto3=Produto(018,"ovos",15.0)


pedido=Pedido()
pedido.adicionar_item(produto1,1)
pedido.adicionar_item(produto2,1)
pedido.adicionar_item(produto3,1)
pedido.listar_produtos()

pedido.remover_item()
pedido.listar_produtos()

pedido.obter_valor_total() 
