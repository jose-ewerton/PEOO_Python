from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from terminal import Produto,Novo,Listagem

'''
ObjectProperty está sendo usado para fazer o intermedio entre os ids no arquivo kv e com as variaveis existentes nesse arquivo;

Funções:
	
	add - Função usada para chamar a função Add do arquivo terminal e que serve para ser chamada atraves do widget badicionar;
	atualizar - Função usada para chamar a função Atualizar do arquivo terminal e que serve para ser chamada atraves do widget batualizar;
	remove - Função usada para chamar a função Remove do arquivo terminal e que serve para swr chamada atraves do widget bremove;
	listar - Função usada para chamar a função Listar do arquivo terminal e q serve para ser chamada atraves do widget blistar
'''

class Projeto(FloatLayout):
	layout = ObjectProperty(None)
	lnome = ObjectProperty(None)
	lvalor = ObjectProperty(None)
	lcod = ObjectProperty(None)
	lchave = ObjectProperty(None)
	ltitulo = ObjectProperty(None)
	llista = ObjectProperty(None)
			
	blistar = ObjectProperty(None)
	badicionar = ObjectProperty(None)
	bremove = ObjectProperty(None)
	batualizar = ObjectProperty(None)
		
	txtnome = ObjectProperty(None)
	txtvalor = ObjectProperty(None)
	txtcod = ObjectProperty(None)
	txtchave = ObjectProperty(None)
		
	produto = Produto()
	novo = Novo()
	Lista = Listagem()
	indicador = 0
		
	def add(self):
		
		if self.txtnome.text == '' or self.txtvalor.text == '' or self.txtcod.text == '':
			self.llista.text = 'Dados invalidos'
		else:
			self.indicador += 1
			self.produto = Produto(nome = self.txtnome.text,id = self.txtcod.text,preco = float(self.txtvalor.text))
			self.Lista.Add(self.produto)
			self.llista.text = f'Chave:{self.indicador}   Nome:{self.produto.nome}   Valor:R${self.produto.preco}   Id:{self.produto.id}'
			print(self.produto)
		
		self.txtnome.text = ''
		self.txtvalor.text = ''
		self.txtcod.text = ''
		self.txtchave.text = ''
		
	def atualizar(self):
		
		if self.txtnome.text == '' or self.txtvalor.text == '' or self.txtcod.text == '' or self.txtchave.text == '':
			self.llista.text = 'Dados incompletos, refaça ter sucesso'
		else:
			i = int(self.txtchave.text) - 1
			self.novo = Novo(nome = self.txtnome.text,id = self.txtcod.text,preco = float(self.txtvalor.text))
			self.Lista.Atualizar(self.produto,self.novo,i)
			self.llista.text = f'Chave:{self.indicador}   Nome:{self.novo.nome}   Valor:R${self.novo.preco}   Id:{self.novo.id}'
		self.txtnome.text = ''
		self.txtvalor.text = ''
		self.txtcod.text = ''
		self.txtchave.text = ''
		self.llista.text = f'A chave {self.indicador} teve seus dados atualizados para {self.novo.nome}'						
		
	def remove(self):
		if self.txtchave.text == '':
			self.llista.text = 'Chave não encontrada'
			self.txtchave.text = ''
		else:
			self.indicador -= 1
			i = int(self.txtchave.text) - 1
			self.Lista.Remove(i)
			self.txtnome.text = ''
			self.txtvalor.text = ''
			self.txtcod.text = ''
			self.txtchave.text = ''
			self.llista.text = f'Um produto foi removido da lista atual'
		
	def listar(self):
		self.txtnome.text = ''
		self.txtvalor.text = ''
		self.txtcod.text = ''
		self.txtchave.text = ''
		
		self.llista.text = self.Lista.Listar()
		
	
class main(App):
	def build(self):
		return Projeto()
		
main().run()