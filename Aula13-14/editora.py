class Editora:
    def __init__(self,cod_editora, razao_social, email, telefone):
        self.__cod_editora = cod_editora
        self.__razao_social = razao_social
        self.__email = email
        self.__telefone = telefone


    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def descricao(self,razao_social):
        self.__razao_social = razao_social
        
