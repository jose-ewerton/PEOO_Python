class Animal:
      def __init__(self, raca, nome, idade, peso, sexo, porte, cor, perigo):
    self.raca = raca
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.sexo = sexo
    self.porte = porte
    self.cor = cor

  def entradas(self):
    a = Animal
    a.nome = str(input("qual o nome?:"))
    a.raca = str(input("qual a raca?:"))
    a.idade = float(input("qual a idade do bixo?:"))
    a.peso = float(input("qual o peso?:"))
    a.sexo = str(input("eh maxo, femea ou baitola?:"))
    a.cor = str(input("qual a cor?:"))
    
    print(f"o nome do bixo eh {a.nome}")
    print(f"{a.nome} eh {a.raca}")
    print(f"{a.nome} tem {a.idade} anos")
    print(f"{a.nome} tem {a.peso}kg")
    print(f"{a.nome} eh {a.cor}")
    
  def perigo(self):
    """
    forneca o porte como: pequeno, medio e grande.
    forneca sendo perigo entre 1 a 10.
    """
    a = Animal
    a.porte = str(input("qual o porte?:"))
    a.perigo = float(input("forneca o nivel de perigo:"))
    if a.porte == 'pequeno' and a.perigo <= 3:
      print("essa poha faz nada")
    if a.porte == 'pequeno' and 4>= a.perigo <= 6:
      print("uma ratasana")
    if a.porte == 'pequeno' and a.perigo >6:
      print("capeta pequeno")
      
    if a.porte == 'medio' and a.perigo <= 3:
      print("que brincalhão")
    if a.porte == 'medio' and 4>= a.perigo <= 6:
      print("bixo do mato")
    if a.porte == 'medio' and a.perigo >6:
      print("nao faca movimentos bruscos")
    
    if a.porte == 'grande' and a.perigo <= 3:
      print("grandão")
    if a.porte == 'grande' and 4>= a.perigo <= 6:
      print("muito cuidado nessa hora")
    if a.porte == 'grande' and a.perigo >6:
      print("CORRE PIRANHA CORRE!")


Animal.entradas("a")
Animal.perigo("a")
