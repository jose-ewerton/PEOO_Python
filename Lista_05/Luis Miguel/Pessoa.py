class Pessoa:
    def __init__(self, nome, etnia, altura, peso, saude, sexo):
        self.nome = nome
        self.etnia = etnia
        self.altura = altura
        self.peso = peso
        self.saude = saude
        self.sexo = sexo
 
  def entradas(self):
        """
        forneça a altura em cm e o peso em kg
        """
        e = Pessoa
        e.nome = str(input("nome da pessoa:?"))
        e.etnia = str(input("qual sua etnia?:"))
        e.altura = float(input("qual a altura?:"))
        e.peso = float(input("qual o peso?:"))
        e.sexo = str(input("qual o sexo?:"))
        
        print(f"a pessoa se chama {e.nome}")
        print(f"{e.nome} eh {e.etnia}")
        print(f"{e.nome} tem {e.altura}cm")
        print(f"{e.nome} pesa {e.peso}kg")
        print(f"{e.nome} eh do sexo {e.sexo}")
    
  def estado(self):
    """
    forneca a saude de 1 a 10
    """"
    e = Pessoa
    e.saude = float(input("qual o estado de saude?:"))
    if e.saude <= 3:
      print("leve esta pessoa para o hospital mais proximo agora!")
    if 4 <= e.saude <= 6:
      print("mantenha esta pessoa sobre supervisão")
    if 7 <= e.saude <= 9:
      print("so uma gripezinha")
    if e.saude == 10:
      print("historico de atleta")
    elif 0 < e.saude > 10:
        print("nao sabe ler?")


Pessoa.entradas("a")
Pessoa.estado("a")
