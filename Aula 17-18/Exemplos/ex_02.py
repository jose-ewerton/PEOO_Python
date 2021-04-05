'''
Adicionar vários widgets ao meu Layout

'''

from kivy.app import App  #cria o app
from kivy.uix.button import Button  # widget 1
from kivy.uix.label import Label  # widget 2
from kivy.uix.boxlayout import BoxLayout #cria um box e eu consigo botar mais de um widget na tela

class MinhaClasse(App):
    def build(self):
        label = Label (text = 'Olá mundo')
        button = Button (text = "Botão")

        label.font_size = 50
        button.font_size = 50

        box = BoxLayout ()
        box.add_widget(label)
        box.add_widget(button) 
        return box
MinhaClasse().run()


