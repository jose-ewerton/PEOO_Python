
#atributos e métodos para a classe CARRO.
class Veiculo():
    def __init__( self, tipo, marca, cor):
        self.tipo = tipo
        self.marca = marca
        self.cor = cor


    def detalhar_veiculo(self):
        print("Tipo: {0}".format(self.tipo))
        print("Marca: {0}".format(self.marca))
        print("Cor: {0}".format(self.cor))


v = Veiculo("carro","Volkswagen","Amarelo")
v.detalhar_veiculo()