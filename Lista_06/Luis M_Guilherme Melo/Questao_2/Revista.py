class Revista:
    def __init__(self, codigo, titulo, tipo, edicao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__tipo = tipo
        self.__edicao = edicao
        self.lista = []
    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edicao(self):
        return self.__edicao

    def inserir_edicao1(self, numedit, datadeedit, numartg):
        self.lista.append(Edicao(numedit, datadeedit, numartg))

    def mostrar_edicao1(self):
        for edicao in self.lista:

            print("Número de edição: ", edicao.numedit)
            print("Data de edição: ", edicao.datadeedit)
            print("Número de artigos: ",  edicao.numartg)

    def detalhar_revista(self):
        print(25 * "-")
        print("REVISTA")
        print("Codigo: {0}" .format(self.codigo))
        print("Titulo = {0}".format(self.titulo))
        print("Tipo = {0}".format(self.tipo))
        print("Edição = {0}".format(self.edicao))
        print(25 * "-")

class Edicao:

    def __init__(self, numedit, datadeedit, numartg):
        self.__numedit = numedit
        self.__datadeedit = datadeedit
        self.__numartg = numartg

    @property
    def numedit(self):
        return self.__numedit
    
    @property
    def datadeedit(self):
        return self.__datadeedit
    
    @property
    def numartg(self):
        return self.__numartg
