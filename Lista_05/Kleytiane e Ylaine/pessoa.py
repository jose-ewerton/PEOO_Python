class Pessoa:
    def _init_(self):
        self.cor = None
        self.altura = None
        self.peso = None
    
    def respirar(self):
        print('A pessoa está respirando!')
        
    def movimentar(self):
        print('A pessoa está movimentar!')
        
    def falando(self):
        print('A pessoa está falando!')

if (__name__ == "__main__"): # isso serve para testar a classe
    p = Pessoa()
    p.cor = "Preto"
    p.altura = "1.50m"
    p.peso = "40kg"
    print(p.cor,p.altura,p.peso)
    p.respirar()
    p.movimentar()
    p.falando()