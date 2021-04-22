'''
Mudando a orientação da box, adicionando novo componente TextImput
'''

from kivy.app import App  #cria o app
from kivy.uix.button import Button  # widget 1
from kivy.uix.label import Label  # widget 2
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout #cria um box e eu consigo botar mais de um widget na tela

def on_press(btn):
    btn.text = 'Apertado'

def on_release(btn):
    btn.text = 'Solto'

class MinhaClasse(App):
    def build(self):
        label = Label (text = 'Olá mundo', font_size = 50)
        #Construindo um botão e implementando eventos de quando pressionado e quando solto
        button = Button (text = "Botão", 
                        font_size = 50,
                        on_press = on_press,           
                        on_release = on_release,
        ) #os parãmetros do botão podem ser passados na construção do mesmo através do inicializador da classe

        textinput = TextInput ()
        box = BoxLayout (orientation = 'vertical')  #muda a orientação para vertical
        #Observe que o box sempre divide a tela pelo numero de componentes igual
        box.add_widget(label)
        box.add_widget(textinput)
        box.add_widget(button) 
        return box
MinhaClasse().run()


