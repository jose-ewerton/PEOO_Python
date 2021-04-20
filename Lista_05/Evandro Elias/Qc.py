class Pessoa:
  def __init__(self, nome, altura, peso, saude, gen):
    self.nome = nome
    self.altura = altura
    self.peso = peso
    self.saude = saude
    self.gen = gen
 
  def informa(self):
    e = Pessoa
    e.nome = str(input("Nome da pessoa:"))
    e.altura = float(input("Altura:"))
    e.peso = float(input("Peso:"))
    e.gen = str(input("Genero:"))
    
    print(f"Nome: {e.nome}")
    print(f"Altura: {e.altura}cm")
    print(f"Peso {e.peso}kg")
    print(f"Genero: {e.gen}")

  def sad(self):
      e = Pessoa
      e.dinheiro = int(input("Como esta sua situação financeira? 1 = ruim  2 = Boa"))
      if e.dinheiro == 1:
          print("Arrume um emprego melhor")
      if e.dinheiro == 2:
          print("Continue trabalhando")

Pessoa.informa("e")
Pessoa.sad("e")
