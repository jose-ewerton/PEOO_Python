'''
Como criar o hello word, adicionar um label e um button

'''

from kivy.app import App  #cria o app
from kivy.uix.button import Button  # cria um botão no layout
from kivy.uix.label import Label  #cria um label no layout
from kivy.uix.boxlayout import BoxLayout #cria um box e eu consigo botar mais de um elemento na tela

class MinhaClasse(App):
    def build(self):
        btn =  Button(text= 'Botão')
        #return Label(text = 'Olá mundo!')
        label = Label (text = 'Olá mundo',font_size = 50) #instancia da classe Label
        box = BoxLayout()
        box.add_widget(label)
        box.add_widget(btn)
        return box

        
MinhaClasse().run()


