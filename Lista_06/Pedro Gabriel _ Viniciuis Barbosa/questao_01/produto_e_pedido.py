class Produto:

    def __init__(self, nome, id, valor):
        self.nome = nome
        self.id = id
        self.valor = valor
        self.item = None


class ItemPedido:

    def __init__(self):
        self.item = None
        self.nome = None
        self.id = None
        self.valor = None

    def adc(self, produto, item):
        self.nome = produto.nome
        self.id = produto.id
        self.valor = produto.valor
        produto.item = item
        self.item = produto.item
        print("Você pediu", self.item, "itens do produto:", self.nome)


class Pedido:

    def __init__(self):
        self.lista_pedido = []

    def add_pedido(self, itempedido):
        self.lista_pedido.append(itempedido)
        print(itempedido.nome, "foi adicionado ao carrinho")

    def remove_pedido(self, itempedido):
        self.lista_pedido.remove(itempedido)
        print(itempedido.nome, "foi removido ao carrinho")

    def listar(self):
        print("")
        print("Lista de Produtos:")
        for itempedido in self.lista_pedido:
            print("Nome:", itempedido.nome,"-", "Codigo:", itempedido.id,"-", "Valor(unidade): R$", itempedido.valor, "-",
                  "Quantidade:", itempedido.item)

    def valor_total(self):
        total = []
        for itempedido in self.lista_pedido:
            valor = itempedido.valor * itempedido.item
            total.append(valor)
        print("O valor total é de R$", sum(total))


