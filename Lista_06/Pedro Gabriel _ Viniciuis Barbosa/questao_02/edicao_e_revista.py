class Edicao:

    def __init__(self, num, data, num_artg):
        self._num = num  #Número da Edição
        self._data = data
        self._num_artg = num_artg  #Número do Artigo


class Revista:

    def __init__(self, codigo, titulo, tipo, edicao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__tipo = tipo
        self.__edicao = edicao
        self.__lista_edicoes = []

    def adc_revista(self, edicao):
        self.__lista_edicoes.append(edicao)

    def listar_edicoes(self):
        print("Título:", self.__titulo)
        print("Código:", self.__codigo)
        print("Tipo:", self.__tipo)
        print("Edição:", self.__edicao)
        print(10 * '---')
        for edicao in self.__lista_edicoes:
            print("Número da edição: ", edicao._num)
            print("Data da edicao: ", edicao._data)
            print("Número de artigos: ", edicao._num_artg)
            print("")