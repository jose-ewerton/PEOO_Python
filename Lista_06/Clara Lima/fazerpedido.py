from produto import Produto, ItemPedido

i = ItemPedido()

produto1 = Produto('Laranja',123,1.50)
produto2 = Produto('Abacaxi',456, 2.00)
produto3 = Produto('Limão', 789, 3.00)
produto4 = Produto('Morango',321, 4.00)

i.adicionar_produto(produto1,2)
i.adicionar_produto(produto2,3)
i.adicionar_produto(produto3,1)
produto4= i.adicionar_produto(produto4,4)
