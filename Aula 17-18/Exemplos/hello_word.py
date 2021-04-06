

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App): #Herança
    def build(self): #método da classe
        return Button(text='Hello World') #criando um objeto

TestApp().run() #o run() eu estou herdando da classe App
