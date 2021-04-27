class Veiculo:
    def __init__(self,__tipo_de_veiculo,__modelo,__ano,__fabricante,_cor,km_rodados=0):
        self.__tipo_de_veiculo = __tipo_de_veiculo
        self.__modelo = __modelo
        self.__ano = __ano
        self.__fabricante = __fabricante
        self._cor = _cor
        self.km_rodados = km_rodados
        self.estado = None

    def detalhar_veiculo(self):
        print(f"O veiculo: {self.__tipo_de_veiculo}\nModelo: {self.__modelo}\nAno: {self.__ano}\nFabricante: {self.__fabricante}\nCor: {self._cor}\nKm rodados: {self.km_rodados}")

    def acelerar(self):
        print(f"{self.__modelo} está acelerando")
        self.estado = "acelerando"
    
    def freiar(self):
        print(f"{self.__modelo} está freiando")
        self.estado = "freiando"

    def parar(self):
        print(f"{self.__modelo} está parado")
        self.estado = "parado"
    
    def mostrar_estado(self):
        print (self.estado)
    
    def aumentar_km_rodados(self, kms):
        self.km_rodados += kms

    def mostrar_km_rodados(self):
        print(f"O veiculo já rodou {self.km_rodados}km")

if __name__=='__main__':
    a = Veiculo("Carro","Fusca",1982,"Volks","Branco",)
    a.detalhar_veiculo()
    a.acelerar()
    a.mostrar_km_rodados()
    a.aumentar_km_rodados(500)
    a.mostrar_km_rodados()
