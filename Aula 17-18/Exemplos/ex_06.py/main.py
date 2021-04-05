'''
Mudando adicionando novos box para organizar os widgets da página
'''

from kivy.app import App  #cria o app
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout (BoxLayout):
    pass

class mainApp(App): #preciso informar o nome do arquivo kv no inicio do App
    def build(self):
        return MyBoxLayout()

 
mainApp().run()


