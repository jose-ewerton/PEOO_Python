
class Endereco:
    def __init__(self, n_casa, rua, cidade, estado, pais):
        self.n_casa = n_casa
        self.rua = rua 
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
    
    def endereco_detalar(self):
        print("...............Informações de Endereço...............")
        print("Nº_casa: {0}".format(self.n_casa))
        print("Rua: {0}".format(self.rua))
        print("Cidade: {0}".format(self.cidade))
        print("Estado: {0}".format(self.estado))
        print("País: {0}".format(self.pais))
        
        
    

