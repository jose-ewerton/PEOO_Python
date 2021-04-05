'''
Mudando adicionando novos box para organizar os widgets da página
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
        box1 = BoxLayout ()
        box2 = BoxLayout (orientation = 'vertical')  #muda a orientação para vertical
        box3 = BoxLayout(orientation = 'vertical')
        #Observe que o box sempre divide a tela pelo numero de componentes igual
        box1.add_widget(label)
        box1.add_widget(textinput)
        box2.add_widget(button)
        box3.add_widget(box1)
        box3.add_widget(box2) 
        return box3   #detalhes a partir daqui fica confuso de se trabalhar com tantas box, uma opção poderia ser o grid, mas também seria um pouco ilegível, solução usar o Kivy Lang para marcação dos widgets da página
MinhaClasse().run()


