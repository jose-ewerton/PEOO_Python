
#   Classe Item Pedido: Listar_produto, quantidade
from produto import Produto
class ItemPedido:
    def __init__(self):
        self.__lista_produto =[]
        self.__quantidade = 0 

    def adicionar_produto(self, produto, quantidade):
        self.__lista_produto.append(produto)
        self.__quantidade = quantidade
        return self

    


     


  