class Revista:
    def __init__(self, cod, titulo, tipo, edicao):
        self.__cod = cod
        self.__titulo = titulo
        self.__tipo = tipo
        self.__edicao = edicao
        self.__lista_edicoes = []

    def adc_revista(self, edicao):
        self.__lista_edicoes.append (edicao)

    def listar(self):
        print("titulo:", self.__titulo)
        print("codigo:", self.__cod)
        print("tipo:", self.__tipo)
        print("edicao:", self.__edicao)
        for edicao in self.__lista_edicoes:
            print("num. edicao:", edicao._número)
            print("data da edicao:", edicao._data)
            print("numero de artigos:", edicao._número_artigo)
