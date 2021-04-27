class Produto:
    def __init__(self, descricao =str, codigo =int, preco=float, quantidade= int):
        self.descricao = descricao
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

class ItemPedido:
    def __init__(self):
        self.descricao = None
        self.codigo = None
        self.preco = None
        self.quantidade = None

    def adicionar_produto(self, produto, quantidade):
        self.produto = produto.descricao
        self.codigo = produto.codigo
        self.preco = produto.preco
        produto.quantidade = quantidade
        self.quantidade = produto.quantidade
        print(f" produtos adicionados: {self.quantidade} {self.produto}")


