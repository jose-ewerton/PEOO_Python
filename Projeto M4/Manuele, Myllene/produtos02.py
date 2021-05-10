class Produto:
    def __init__(self,ident=None,nome=None,marca=None,preco=None):
        self.ident = ident
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.lista_produtos = []

    
  
    def listar(self):
        for item in self.lista_produtos:
            print(item.ident,item.nome,item.marca,item.preco)

      
    def adicionar(self,ident,nome,marca,preco):
        self.lista_produtos.append(Produto(ident,nome,marca,preco))

    def deletar(self):
        pass
    def atualizar(self):
        pass
    
