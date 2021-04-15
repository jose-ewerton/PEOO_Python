from kivy.app import App  
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from reserva import Reserva
from kivy.properties import ObjectProperty


class Painel(FloatLayout):  
    layout = ObjectProperty(None)        
    label1 = ObjectProperty(None)
    label2 = ObjectProperty(None)
    label3 = ObjectProperty(None)
    label4 = ObjectProperty(None)
    label5 = ObjectProperty(None)
    textinput1 = ObjectProperty(None)
    textinput2 = ObjectProperty(None)
    textinput3 = ObjectProperty(None)
    textinput4 = ObjectProperty(None)

    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    lista = ObjectProperty(None)

    reservas = Reserva()

    def limpar_widget(self):
        self.lista.opacity = 0  
        self.label2.opacity = 0
        self.label3.opacity = 0
        self.label4.opacity = 0
        self.textinput2.opacity = 0
        self.textinput3.opacity = 0
        self.textinput4.opacity = 0 
        self.label5.opacity = 0
        self.btn1.opacity = 0
        self.btn2.opacity = 0

    def inserir(self):
        self.limpar_widget()
        #construindo o formulário de adicionar reserva
        self.label2.opacity = 1
        self.label3.opacity = 1
        self.label4.opacity = 1
        self.textinput2.opacity = 1
        self.textinput3.opacity = 1
        self.textinput4.opacity = 1  
        self.label5.opacity = 1
        self.btn1.opacity = 1 
        self.label5.text = 'Preencha todos os campos' 
        self.enviar()

    def enviar(self):
        if (self.textinput2.text == "" or self.textinput3.text == "" or self.textinput4.text == ""):
            self.label5.text = 'Preencha todos os campos'
        else:
            self.label5.text = self.reservas.adicionar_reserva(self.textinput2.text,self.textinput3.text,self.textinput4.text)
            self.textinput2.text = ""
            self.textinput3.text = ""
            self.textinput4.text = ""

    def listar(self):
        self.limpar_widget() 
        self.lista.opacity = 1
        self.lista.text = self.reservas.listar_reservas()
    
    def deletar(self):
        self.limpar_widget() 
        self.btn2.opacity = 1

    def excluir(self):
        pass

    def atualizar(self):
        self.limpar_widget() 

class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()