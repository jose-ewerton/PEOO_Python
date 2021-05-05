from edicao import Edicao

class Revista:

    def __init__(self, codigo, titulo, tipo, edicao):
        self.codigo = codigo
        self.titulo = titulo
        self.tipo = tipo
        self.edicoes = [edicao]
  
    def add_edicao(self,n_edicao,d_edicao,n_artigos):
            self.edicoes.append(Edicao(n_edicao, d_edicao, n_artigos))
        
    
    def exibir_revista(self):
        print("----------MOSTRANDO INFORMAÇÕES DA REVISTA----------")
        print("Código: {0}".format(self.codigo))
        print("Título: {0}".format(self.titulo))
        print("Tipo: {0}".format(self.tipo))
        for edicao in self.edicoes:
            edicao.info_edicao()