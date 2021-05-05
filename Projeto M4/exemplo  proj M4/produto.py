class Produto:
    def __init__(self,nome = None): # vale 1 ponto
        self.cont = 0
        self.nome  = nome
        self.lista = []

    def adicionar(self): # vale 1 ponto
        self.cont += 0
        nome = input("digite um nome ")
        self.lista.append(Produto(nome))

    def listar(self): # vale 1 ponto
        for item in self.lista:
            print(item.nome)

    def deletar(self): # vale 1 ponto
        r = input("Digite um nome para deletar: ")
        foi = False
        for item in self.lista:   
            if (item.nome == r): #produto.cod == r
                print(f'Deletando o nome {item.nome}')
                self.lista.remove(item)
                foi = True
        if not foi:
            print("Valor inválido")

        

    def atualizar(self): # vale 1 ponto
        r = input("Digite o nome para atualizar: ")
        foi = False
        for item in self.lista:   
            if (item.nome == r):
                print(f'Atualizando o nome {item.nome}')
                nomenovo = input("Digite novo nome: ")
                item.nome = nomenovo       
                foi = True
        if not foi:
            print("Valor inválido")

if (__name__ == '__main__'):
    i= 0
    while (i < 3):
        p = Produto()
        print('----------ADD-------------')
        p.adicionar()
        print('----------ADD-------------')
        p.adicionar()
        print('----------LIS-------------')
        p.listar()
        print('----------DEL-------------')
        p.deletar()
        print('----------LIS-------------')
        p.listar()
        print('----------ATT-------------')
        p.atualizar()
        print('----------LIS-------------')
        p.listar()
        i+= 1

