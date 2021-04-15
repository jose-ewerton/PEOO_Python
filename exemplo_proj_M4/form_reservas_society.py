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

    btn = ObjectProperty(None)
    lista = ObjectProperty(None)

    reservas = Reserva()

    def adicionar(self):
        self.lista.opacity = 0
        #self.label1.opacity = 1
        self.label2.opacity = 1
        self.label3.opacity = 1
        self.label4.opacity = 1
        #self.textinput1.opacity = 1
        self.textinput2.opacity = 1
        self.textinput3.opacity = 1
        self.textinput4.opacity = 1  
        self.enviar()    

    def enviar(self):
        print('teste')
        if (self.textinput2.text == "" or self.textinput3.text == "" or self.textinput4.text == ""):
            self.label5.opacity = 1
            self.btn.opacity = 1
            self.label5.text = 'Preencha todos os campos'
        else:
            self.label5.text = self.reservas.adicionar_reserva(self.textinput2.text,self.textinput3.text,self.textinput4.text)
            self.textinput2.text = ""
            self.textinput3.text = ""
            self.textinput4.text = ""
            
    def listar(self):
        self.label2.opacity = 0
        self.label3.opacity = 0
        self.label4.opacity = 0
        self.textinput2.opacity = 0
        self.textinput3.opacity = 0
        self.textinput4.opacity = 0 
        self.label5.opacity = 0
        self.btn.opacity = 0

        self.lista.opacity = 1
        self.lista.text = self.reservas.listar_reservas()

class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()