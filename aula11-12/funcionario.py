class Funcionario:
    '''
    public eu tenho acesso fora da classe
    _ protected eu tenho acesso também, mas é aconselhavel não alterar
    __ private eu tenho acesso, mais não devo alterar de jeito nenhum
    '''
    
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__horas_trabalhadas = 0
        self.__valor_por_hora = None

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_por_hora

    def incrementar_horas(self,horas):
        self.__horas_trabalhadas += horas
    
    #métodos Getter e Setter são métodos acessores de atributos da classe
    #implementar o método Getter
    @property   #Getter
    def nome(self):
        return self.__nome

    @nome.setter   #Setter
    def nome(self,nome):
        self.__nome = nome

    @property   #Getter
    def cpf(self):
        return self.__cpf

    @cpf.setter   #Setter
    def cpf(self,cpf):
        self.__cpf = cpf


    @property   #Getter
    def valor_por_hora(self):
        return self.__valor_por_hora

    @valor_por_hora.setter   #Setter
    def valor_por_hora(self,valor_por_hora):
        self.__valor_por_hora = valor_por_hora

    @property   #Getter
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
