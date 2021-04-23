class Produto:
    def __init__(self, nome, cod, preço):
        self.nome = nome
        self.cod = cod
        self.preço = preço
        self.item = None


class ItemPedido:
    def __init__(self):
        self.item = None
        self.nome = None
        self.cod = None
        self.preço = None

    def adicionar(self, produto, item):
        self.nome = produto.nome
        self.cod = produto.cod
        self.preço = produto.preço
        produto.item = item
        self.item = produto.item
        print ("Foi pedido", self.item, "itens do produto", self.nome)