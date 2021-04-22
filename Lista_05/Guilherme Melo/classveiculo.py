class Veiculo:

    def __init__(self):
        self.Marca = None
        self.Modelo = None
        self.Anofab = None
        self.Estado = None

    def detalhar_veiculo(self):
        print(25*"-")
        print("Marca = {0}." .format(self.Marca))
        print("Nodelo = {0}." .format(self.Modelo))
        print("Ano de fabricação = {0}." .format(self.Anofab))
        print("Estado = {0}." .format(self.Estado))

