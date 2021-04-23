class Produto:
    def __init__(self, cod, nome, preço):
        self.cod = cod
        self.nome = nome
        self.preço = preço


class Item:
    def __init__(self, cod, nome, preço):
        self.cod = cod
        self.nome = nome
        self.preço = preço


class Item_Adicionado:
    def __init__(self):
        self.lista_produtos = []

    def add_produto(self, produto):
        self.lista_produtos.append(produto)
        print(f'{produto.nome} foi adicionado')

    def listar_produto(self):
        for produto in self.lista_produtos:
            print(f'Produto: {produto.nome}\n'
                  f'Preço: {produto.preço}\n'
                  f'Codigo: {produto.cod}')

    def remover_produto(self, produto):
        self.lista_produtos.remove(produto)
        print (f'{produto.nome} o foi removido com exito')

    def atualizar(self, produto, item):
        self.lista_produtos.remove(produto)
        self.lista_produtos.append(item)
        print(f'O produto {produto.nome} foi atualizado para {item.nome}')


p = Produto(1, "banana", 2.5)
p1 = Produto(5, "Vinho", 30)
p2 = Produto(6, "Amendoin", 15)
p3 = Produto(2, "Cachaça", 13)
p4 = Produto(1, "Papel", 5)
i = Item_Adicionado()
i.add_produto(p)
i.add_produto(p1)
i.add_produto(p2)
i.add_produto(p3)
i.add_produto(p4)
i.listar_produto()
i.remover_produto(p4)
i.listar_produto()
it = Item(10, "carne", 50)
i.atualizar(p, it)
i.listar_produto()