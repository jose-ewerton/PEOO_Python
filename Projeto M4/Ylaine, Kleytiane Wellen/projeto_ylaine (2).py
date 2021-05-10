class Produto:
    def __init__(self, cod=0, nome=None, marca=None, preco=None):
        self.cod = cod
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.lista_produtos = []

    def adicionar(self):
        self.cod += 1
        self.nome = input(' Digite o nome de um produto: ')
        self.marca = input(' Digite a marca do produto: ')
        self.preco = input(' Digite o preço do produto: ')


        self.lista_produtos.append(Produto(self.cod, self.nome, self.marca, self.preco))


    def listar(self):
        for produto in self.lista_produtos:
            print(produto.cod, produto.nome, produto.marca, produto.preco)


    def deletar(self):
        r = int(input("Digite o codigo do produto para deletar: "))
        f = False
        for produto in self.lista_produtos:
            if (produto.cod == r): # produto.cod == r
                self.lista_produtos.remove(produto)
                print(f'Deletando do produto: {produto.nome}')

    def atualizar(self):  # vale 1 ponto
        r = input("Digite o nome para atualizar: ")
        foi = False
        for item in self.lista_produtos:
            if (item.nome == r):
                print(f'Atualizando o nome {item.nome}')
                nomenovo = input("Digite novo nome: ")
                item.nome = nomenovo
                foi = True
        if not foi:
            print("Valor inválido")



if (__name__ == '__main__'):
    p = Produto()
    p.adicionar()
    p.adicionar()
    p.listar()
    p.deletar()
    p.listar()
    p.atualizar()
    p.listar()
