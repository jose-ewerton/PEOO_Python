class Pessoa:
    def __init__(self,_nome,idade,peso,altura,_sexo):
        self._nome = _nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self._sexo = _sexo
        self.estado = None

    def detalhar_pessoa(self):
        print(f"Nome: {self._nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\nSexo: {self._sexo}")

    def andar(self):
        print(f"{self._nome} está andando")
        self.estado = "andando"
    
    def comer(self):
        print(f"{self._nome} está comendo")
        self.estado = "comendo"

    def falar(self):
        print(f"{self._nome} está falando")
        self.estado = "falando"

    def correr(self):
        print(f"{self._nome} está correndo")
        self.estado = "correndo"

    def sentar(self):
        print(f"{self._nome} está sentado")
        self.estado = "sentado"

    def completar_ano(self):
        self.idade += 1
        print(f"Parabéns {self._nome} você acabou de completar {self.idade} anos!")
    
    def aumentar_peso(self,kgs):
        print(f"{self._nome} engordou {kgs}kg")
        self.peso += kgs

    def diminuir_peso(self,kgsa):
        if kgsa >= self.peso:
            print("Se essa pessoa perder esse peso, fica invisivel sdkskj")
        else:
            print(f"{self._nome} emagreceu {kgsa}kg")
            self.peso -= kgsa

    def aumentar_altura(self,alt):
        print(f"{self.altura} cresceu {alt}m")
        self.altura += alt

    def diminuir_altura(self,alta):
        if alta >= self.altura:
            print("Se essa pessoa perder essa altura, vira smurf sdkskj")
        else:
            print(f"{self.altura} diminuiu {alta}m")
            self.altura -= alta

if __name__ == "__main__":
    p1 = Pessoa("Luis",18,80,1.85,"Masculino")
    p1.detalhar_pessoa()
    p1.comer()
    p1.completar_ano()
    p1.correr()
    p1.diminuir_peso(15)
    p1.detalhar_pessoa()
    del(p1)
    p1.detalhar_pessoa()