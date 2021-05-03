#Classe Pedido: Remover,Listar, Obter_valor_total
from item_pedido import ItemPedido
from produto import Produto

#ADICIONAR_PRODUTO
class Pedido:
  def __init__(self):
        self.valor_total = 0.0
        self.lista_pedidos = []
        
  def adicionar_item(self, produto,quantidade):
      i = ItemPedido()
      self.lista_pedidos.append(i.adicionar_produto(produto,quantidade))
      self.valor_total += (produto.valor * quantidade)
      print(f'Valor total R$ {self.valor_total}')
      #self.valor_total = self.valor_total + (produto.valor * quantidade)

  #REMOVER_PRODUTO
  def remover_item(self):
      for item in self.lista_pedidos:
          print(item.quantidade)
                
            
'''


  #VALOR_TOTAL
          def Obter_valor_total(self,valor_total,calculo):
            self.valor_total= None
            self.calculo= quandidade * self.__valor          

'''


  