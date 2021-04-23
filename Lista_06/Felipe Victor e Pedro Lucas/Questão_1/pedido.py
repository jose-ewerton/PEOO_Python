class Pedido:
    def __init__(self):
        self.lista_pedido = []

    def adc_pedido(self, item_pedido):
        self.lista_pedido.append(item_pedido)
        print(item_pedido.nome, "foi adicionado a lista")

    def remover_pedido(self, item_pedido):
        self.lista_pedido.remove(item_pedido)
        print(item_pedido.nome, "foi removido da lista")

    def listar_produtos(self):
        print("Lista de Produtos:")
        for item_pedido in self.lista_pedido:
            print("Nome:", item_pedido.nome, "Codigo:", item_pedido.cod, "Valor(unidade): R$", item_pedido.preço,
                   "quantidade:", item_pedido.item)

    def valor_total(self):
        total = []
        for item_pedido in self.lista_pedido:
            valor = item_pedido.preço * item_pedido.item
            total.append(valor)
        print("O valor total é de R$", sum(total))