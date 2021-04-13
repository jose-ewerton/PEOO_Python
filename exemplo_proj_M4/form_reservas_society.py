from kivy.app import App  
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from reserva import Reserva
from kivy.properties import ObjectProperty


class Painel(FloatLayout):  
    layout = ObjectProperty(None) 
    def adicionar(self):
        pass

class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()