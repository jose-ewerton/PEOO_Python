'''Defina os atributos e métodos das seguintes classes:
Pessoa:'''

class Pessoa:
	
	def __init__(self, nome, idade, genero, VM, Saude,PM):
		
		self.nome = nome
		self.idade = idade
		self.genero = genero
		self.vm = VM
		self.pm = PM
		self.saude = Saude	
		
	def base(self):
		
		p = Pessoa
			
		p.nome = input("Nome: ")
		p.idade = int(input("Idade: "))
		p.genero = input("Gênero: ")
			
		print("Nome:", p.nome)
		print("Idade:", p.idade)
		print("Gênero:", p.genero)
	
	def acoes(self):
		
		p = Pessoa
		
		p.vm = input("Está Acordado ou Dormindo:")
		
		if p.vm == "Acordado" or p.vm =="acordado":
			p.saude = input("Como está a sua saúde:")
			p.pm = input("Está parado ou se movimentando:")
			print(p.nome, "está", p.vm,",com a saúde",p.saude," e também está",p.pm)
		elif p.vm == "Dormindo" or p.vm == "dormindo":
			print(p.nome, "está dormindo")
			
Pessoa.base("a") #chamada do método pela classe
Pessoa.acoes("a")