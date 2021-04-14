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
    def adicionar(self):
        self.label1.opacity = 1
        self.label2.opacity = 1
        self.label3.opacity = 1
        self.label4.opacity = 1
        self.textinput1.opacity = 1
        self.textinput2.opacity = 1
        self.textinput3.opacity = 1
        self.textinput4.opacity = 1
        Painel().enviar()
        if (self.textinput1.text == "" and self.textinput2.text == "" and self.textinput3.text == "" and self.textinput4.text == ""):
            self.label5.opacity = 1
            self.label5.text = 'Ainda existem campos vazios que devem ser preenchidos'
            #print("Ainda existem campos vazios que devem ser preenchidos")
        else:
            print(f'Texto é: {self.textinput1.text}')
            self.label1.text = self.textinput1.text
    def enviar(self):
        print('teste')

class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()