class Edicao:
    def __init__(self, n_edicao, data, numero_a):
        self.n_edicao = n_edicao
        self.data = data
        self.numero_a = numero_a

class Revista:
    def __init__(self, titulo, codigo, tipo):
       self.titulo = titulo
       self.codigo = codigo
       self.tipo = tipo
       self.edicao = []

    def a_edicao(self, n_edicao, data, numero_a):
       self.edicao.append(Edicao(n_edicao, data, numero_a))

    def listar(self):
        print('Dados da revista')
        print('Titulo:', self.titulo, 'Codigo:', self.codigo, 'Tipo:', self.tipo)
        for edicao in self.edicao:
            print('Dados da edição:')
            print('Numero da edição:', edicao.n_edicao)
            print('Data de lançamento:', edicao.data)
            print('Numero de artigo:', edicao.numero_a)



