class Produto:
    def __init__(self, codigo:int, descricao:str, valor:float):
        self.codigo=codigo
        self.descricao=descricao
        self.valor=valor
    def produto(self,produto:int,descricao:str,valor:float):
        self.codigo=produto
        self.descricao=descricao
        self.valor=valor

    def exibir(self):
        return "codigo: {} \ndescricao: {} \nvalor:R$ {}".format(self.codigo, self.descricao, self.valor)


class ItemProduto:
    def __init__(self):
        self.quantidade=[]
        self.produto=[]

    def adicionar_produto(self,quantidade:int, produto):
        self.quantidade.append(quantidade)
        self.produto.append(produto)

    def exibir(self):
        for prod in self.produto:
            print(prod.codigo)         

class Pedido:
    def __init__(self):
        self.item=ItemProduto()

    def adicionar_item(self,produto,quantidade):
        self.item.adicionar_produto(quantidade,produto)
        self.produtos=produto

    def remover_item(self):
        numero=int(input("digite o codigo do produto: "))
        for i,p in enumerate (self.item.produto):
            if numero==p.codigo:
                del self.item.produto[i]
                del self.item.quantidade[i]

    def listar_produtos(self):
       print('PRODUTOS')
       for prod in self.item.produto:
           print(" ")
           print("Codigo: {}".format(prod.codigo))
           print("Descricao: {}".format(prod.descricao))
           print("Valor: {}".format(prod.valor))
    def obter_valor_total(self):
        soma=0
        self.quantidade=self.item.quantidade
        for i,p in enumerate (self.item.produto):
            soma+=self.item.quantidade[i] * p.valor
        print("Resultado da soma: R$ {}".format(soma))  
          
