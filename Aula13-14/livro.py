from editora import Editora

class Livro:
    def __init__(self,codigo, descricao, titulo, editora):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__titulo = titulo
        self.__editora = None

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self,editora):
        self.__editora = editora

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao
        