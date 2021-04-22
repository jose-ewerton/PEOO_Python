"""
Formulário de cadastro de espécies por categoria, mesmas funçoes de cadastro de produtos mais, adicionando-os a sua categoria (3 integrantes)

id do animal, peso, alimentação, sexo
categoria (mamífero)  - listar somente a da classe da categoria e listagem geral
"""

print(22*"-", "Catalogo de especies", 23*"-")

class Animal:
	def __init__(self, categoria = str, sexo = str, alimentacao = str, peso = float, id = int, nome = str): #inicializador
		
		self.__categoria = categoria
		self.__sexo = sexo
		self.__alimentacao = alimentacao
		self.__peso = peso
		self.__id = id
		self.__nome = nome
	
	@property
	def categoria(self):
		return self.__categoria
				
	@categoria.setter
	def categoria(self, entrada):
		self.__categoria = str(entrada.lower())
		
		
	@property
	def sexo(self):
		return self.__sexo
		
	@sexo.setter
	def sexo(self, entrada):
		self.__sexo = str(entrada.lower())
		
	
	@property
	def alimentacao(self):
		return self.__alimentacao
		
	@alimentacao.setter
	def alimentacao(self, entrada):
		self.__alimentacao = str(entrada.lower())
	
	
	@property
	def peso(self):
		return self.__peso
	
	@peso.setter
	def peso(self, entrada):
		if isinstance(entrada, str):
			entrada = float(entrada.replace("kg", ""))
		
		self.__peso = entrada
		
		
	@property
	def id(self):
		return self.__id
	
	@id.setter
	def id(self, entrada):
		self.__id = int(entrada)

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, entrada):
		self.__nome = str(entrada.lower())



class Categorias:
	def __init__(self): #inicializador
		self.peixes = []
		self.mamiferos = []
		self.aves = []
		self.anfibios = []
		self.repteis = []
	
	
	def adc_peixe(self, animal):
		if animal.categoria == "peixe":
			self.peixes.append(animal)
					
		else:
			pass
			
	def listar_peixe(self):
		for peixe in self.peixes:
			print("")
			print(30 * "-", "Peixes",  29 * "-")
			print(f"categoria: {peixe.categoria}\nnome: {peixe.nome}\nid: {peixe.id}\nsexo: {peixe.sexo}\nalimentacao: {peixe.alimentacao}\npeso: {peixe.peso}kg")
			
	
	def adc_mamifero(self, animal):
		if animal.categoria == "mamifero":
			self.mamiferos.append(animal)
							
		else:
			pass
			
	def listar_mamifero(self):
		for mamifero in self.mamiferos:
			print("")
			print(28 * "-", "Mamifero",  29 * "-")
			print(f"categoria: {mamifero.categoria}\nnome: {mamifero.nome}\nid: {mamifero.id}\nsexo: {mamifero.sexo}\nalimentacao: {mamifero.alimentacao}\npeso: {mamifero.peso}kg")
								
	def adc_ave(self, animal):
		if animal.categoria == "ave":
			self.aves.append(animal)
				
		else:
			pass
	
	def listar_ave(self):
		for ave in self.aves:
			print("")
			print(30 * "-", "Aves", 31 * "-")
			print(f"categoria: {ave.categoria}\nnome: {ave.nome}\nid: {ave.id}\nsexo: {ave.sexo}\nalimentacao: {ave.alimentacao}\npeso: {ave.peso}kg")
				
				
	def adc_anfibio(self, animal):
		if animal.categoria == "anfibio":
			self.anfibios.append(animal)
				
		else:
			pass
	
	def listar_anfibio(self):
		for anfibio in self.anfibios:
			print("")
			print(28 * "-", "Anfibios", 28 * "-")
			print(f"categoria: {anfibio.categoria}\nnome: {anfibio.nome}\nid: {anfibio.id}\nsexo: {anfibio.sexo}\nalimentacao: {anfibio.alimentacao}\npeso: {anfibio.peso}kg")
				
				
	def adc_reptil(self, animal):
		if animal.categoria == "reptil":
			self.repteis.append(animal)
				
		else:
			pass
	
	def listar_reptil(self):
		for reptil in self.repteis:
			print("")
			print(28 * "-", "Repteis", 28 * "-")
			print(f"categoria: {reptil.categoria}\nnome: {reptil.nome}\nid: {reptil.id}\nsexo: {reptil.sexo}\nalimentacao: {reptil.alimentacao}\npeso: {reptil.peso}kg")


	def del_animal(self, animal):
		if animal.categoria == "peixe":
			self.peixes.remove(animal)
			print("foi removido")
		
		if animal.categoria == "mamifero":
			self.mamiferos.remove(animal)
			print("foi removido")
		
		if animal.categoria == "ave":
			self.aves.remove(animal)
			print("foi removido")
		
		if animal.categoria == "anfibio":
			self.anfibios.remove(animal)
			print("foi removido")
		
		if animal.categoria == "reptil":
			self.repteis.remove(animal)
			print("foi removido")

class Catalogo:
	def __init__(self):
		self.listagem = []
	
	
	def adc_catalogo(self, animal):
		badc = animal.categoria
		self.listagem.append(animal)
		print("#")
		print(f"{badc} adicionado ao catalogo geral")
		print("#")
				
'''bixo1 = Animal("peixe", "femea", "algas", "3kg", 1030)
bixo2 = Animal("mamifero", "baitola", "mel", 65, 69420)
bixo3 = Animal("ave", "maxo", "peixes", 5, 696969)

catalogo = Catalogo()
catalogo.adc_catalogo(bixo1)
catalogo.adc_catalogo(bixo2)
catalogo.adc_catalogo(bixo3)
#catalogo.del_animal(bixo1)

listagem = Categorias()

listagem.adc_peixe(bixo1)
listagem.adc_peixe(bixo2)
listagem.adc_peixe(bixo3)
listagem.adc_mamifero(bixo1)
listagem.adc_mamifero(bixo2)
listagem.adc_mamifero(bixo3)
listagem.adc_ave(bixo1)
listagem.adc_ave(bixo2)
listagem.adc_ave(bixo3)
listagem.adc_anfibio(bixo1)
listagem.adc_anfibio(bixo2)
listagem.adc_anfibio(bixo3)
listagem.adc_reptil(bixo1)
listagem.adc_reptil(bixo2)
listagem.adc_reptil(bixo3)

listagem.del_animal(bixo1)
listagem.del_animal(bixo2)
listagem.del_animal(bixo3)

listagem.listar_peixe()
listagem.listar_mamifero()
listagem.listar_ave()
listagem.listar_anfibio()
listagem.listar_reptil()
'''

