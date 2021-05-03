class Produto:
    def __init__(self, cod, descricao, valor):
        self.cod = cod
        self.descricao = descricao
        self.valor = valor

    def produto(self, produto, descricao, valor):
        self.cod = produto
        self.descricao = descricao
        self.valor = valor

    def exibir_produto(self):
        return f"Código: {self.cod} \nDescrição: {self.descricao} \nValor:R$ {self.valor}"


class ItemProduto:
    def __init__(self):
        self.qtd = []
        self.produto = []

    def adicionar_produto(self, qtd, produto):
        self.qtd.append(qtd)
        self.produto.append(produto)

    def exibir_itemproduto(self):
        for prod in self.produto:
            print(prod.cod)         

class Pedido:
    def __init__(self):
        self.item = ItemProduto()

    def adicionar_item(self, produto, qtd):
        self.item.adicionar_produto(qtd,produto)
        self.produtos=produto

    def remover_item(self, num=0):
        if num == 0:
            print("Para deletar, você precisa fornecer o código")
        else:    
            for x,y in enumerate (self.item.produto):
                if num == y.cod:
                    del self.item.produto[x]
                    del self.item.qtd[x]

    def listar_produtos(self):
        for prod in self.item.produto:
            print(f"Código: {prod.cod} Descrição: {prod.descricao} Valor: {prod.valor}")
        print("")

    def obter_valor_total(self):
        s = 0
        self.qtd = self.item.qtd

        for x,y in enumerate (self.item.produto):
            s += self.item.qtd[x] * y.valor

        print(f"Soma: R$ {s}")  
          