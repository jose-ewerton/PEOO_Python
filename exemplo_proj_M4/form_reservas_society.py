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
    textinput1 = ObjectProperty(None)
    textinput2 = ObjectProperty(None)
    textinput3 = ObjectProperty(None)
    textinput4 = ObjectProperty(None)
    def adicionar(self):
        self.label1.opacity = 1
        self.label2.opacity = 1
        self.label3.opacity = 1
        self.label4.opacity = 1
        self.textinput1.opacity = 1
        self.textinput2.opacity = 1
        self.textinput3.opacity = 1
        self.textinput4.opacity = 1

        if (self.textinput1.text == ""):
            print("Teste do vazio")
        else:
            print(f'Text é: {self.textinput1.text}')

class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()