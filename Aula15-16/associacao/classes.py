class Animais:
    def __init__(self):
        self.__animal = None  
    
    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self,animal):
        self.__animal = animal

# ---------------------------------------------------------- #
class Gato:
    def __init__(self):
        self.__tipo = "Gato"
        self.__emitir_som = "Miauuuu..."

    def som_que_faz(self):  #metodo publico
        return self.__emitir_som  # privado

    def bicho_que_e(self):
        return self.__tipo
# --------------------------------------------------
class Cachorro:
    def __init__(self):
        self.__tipo = "Cachorro"
        self.__emitir_som = "Au au au ..."

    def som_que_faz(self):
        return self.__emitir_som

    def bicho_que_e(self):
        return self.__tipo

# --------------------------------------------------
class Vaca:
    def __init__(self):
        self.__tipo = "Vaca"
        self.__emitir_som = "Muuuuu ..."

    def som_que_faz(self):
        return self.__emitir_som

    def bicho_que_e(self):
        return self.__tipo
