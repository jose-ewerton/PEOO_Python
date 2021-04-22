class Veiculo():
    tipo = None
    marca = None
    cor = None

    def detalhar_veiculo(self):
        print("Tipo: {0}".format(self.tipo))
        print("Marca: {0}".format(self.marca))
        print("Cor: {0}".format(self.cor))



from veiculo import Veiculo
v = Veiculo()
v.tipo = "Carro"
v.marca = "Kwid"
v.cor = "Preto"
v.detalhar_veiculo()