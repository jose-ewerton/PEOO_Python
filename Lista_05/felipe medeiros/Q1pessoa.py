'''Defina os atributos e métodos das seguintes classes:
Pessoa:'''

class pessoa:
	
	def __init__(self, Nome, Idade, Genero, VM, Saude,PM):
		
		self.nome = nome
		self.idade = idade
		self.genero = genero
		self.vm = vm
		self.pm = pm
		self.saude = Saude	
		
	def base(self):
		
		p = pessoa
			
		p.nome = input("Nome: ")
		p.idade = int(input("Idade: "))
		p.genero = input("Gênero: ")
			
		print("Nome:", p.nome)
		print("Idade:", p.idade)
		print("Gênero:", p.genero)
	
	def açoes(self):
		
		p = pessoa
		
		p.vm = input("Está Acordado ou Dormindo:")
		
		if p.vm == "Acordado" or p.vm =="acordado":
			p.saude = input("Como está a sua saúde:")
			p.pm = input("Está parado ou se movimentando:")
			print(p.nome, "estar", p.vm,",com a saúde",p.saude," e também estar",p.pm)
		elif p.vm == "Dormindo" or p.vm == "dormindo":
			print(p.nome, "está dormindo")

pessoa.base("a")
pessoa.açoes("a")