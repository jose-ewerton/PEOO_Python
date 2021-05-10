#adicionar #listar #deletar #atualizar

class Produto:
    def __init__(self, nome = None, marca = None, preço = None, cod = None):
        self.nome = nome
        self.marca = marca
        self.preço = preço
        self.cod = cod
        self.lista_produtos = []
    
    def adicionar(self, nome, marca, preço, cod):
        self.nome += 1
        self.lista_produtos.append(Produto(self.nome, marca, preço, cod))
        print(self.nome, marca, preço, cod)
        return f'Produto adicionado!'

    def listar(self):
        if len(self.lista_produtos) != 0:
            texto = ""
            for item in self.lista_produtos:
                print(item.nome,item.marca,item.preço,item.cod)
                texto += f' Nome: {item.nome}, Marca: {item.marca}, Preço: {item.preço}, ID do produto: {item.cod}\n'
            return texto 
        else:
            return 'Lista sem produtos'

    def deletar(self,cod):
        cond = 0
        for produto in self.lista_produtos:
            if (cod) == produto.nome:
                cond = 1
                texto = f'Removendo o produto {produto.nome}, {produto.marca}, {produto.preço}, {produto.cod}'
                self.lista_produtos.remove(produto)
                return texto
        if  not cond:
            return f'Não há tal produto {cod}'
    
    def atualizar(self,cod,**kwargs):
        cod = 0
        for n,c in kwargs.items():
            if (n == 'nome do produto'):
                cod = int(c)
                break

        for item in self.lista_produtos:
            if (item.nome == cod):
                for n,c in kwargs.items():
                    if (n == 'marca'):
                        item.marca = c
                        for n,c in kwargs.items():
                            print("Atualizado",n,c)
                    if (n == 'preço'):
                        item.preço = c 
                    if (n == 'ID do produto'):
                        item.cod = c
                self.lista_produtos.insert(item.nome,item)
                self.lista_produtos.remove(item)
                return f'Seus produtos foram atualizados'
           
if (__name__ == '__main__'):
    p = Produto()
    print(p.adicionar('Sorvete','Sterbom', 'R$ 15,00', '006'))
    print(p.adicionar('Leite','Betânia', 'R$ 5,00', '098'))
    print(p.adicionar('Pão integral','Wickbold', 'R$ 8,00', '032'))
    p.listar()
    p.atualizar(nome = 'macarrão', marca = 'Adria', cod = '013', valor = 'R$ 8,00')
    p.listar()
    p.atualizar(nome = 'requeijão', marca = 'Nestle', cod = '056', valor = 'R$ 7,50')
    p.listar()
