'''Defina os atributos e métodos das seguintes classes:
Veículos:'''

class carro:
	
	def __init__(self,Marca,Modelo,Ano,Estado,Km_rodados):
		
		self.marca = Marca
		self.modelo = Modelo
		self.ano = Ano
		self.estado = Estado
		self.km.rodados = Km_rodados
		
	def base(self):
		
		a = carro
		
		a.marca = input("Digite a marca do carro:")
		a.modelo = input("Digite o modo do carro:")
		a.ano = input("Digite o ano do carro:")
		
		print('\033[7;97m'+"Marca:", a.marca)
		print("Modelo:", a.modelo)
		print("Ano:", a.ano + '\033[0;0m')
	
	def extra(self):
		
		a = carro
		
		a.estado = input("Digite o estado atual do carro:")
		a.km_rodados = input("Digite quantos km possui o carro atualmente:")
			
		print('\033[7;97m'+"O modelo", a.modelo,", da marca",a.Marca, "está com estado", c.estado, "e com",a.km_rodados,"km rodados."+'\033[0;0m')
			
carro.base(1)
carro.extra(1)