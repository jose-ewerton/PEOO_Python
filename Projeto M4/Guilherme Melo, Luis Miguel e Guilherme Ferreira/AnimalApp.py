from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from animal import Animal, Categorias, Catalogo

class animal(BoxLayout):
    textinput1 = ObjectProperty(None)
    textinput2 = ObjectProperty(None)
    textinput3 = ObjectProperty(None)
    textinput4 = ObjectProperty(None)
    textinput5 = ObjectProperty(None)
    textinput6 = ObjectProperty(None)

    ani = Animal()
    cat = Catalogo()
    listagem = Categorias()
    
    def limpar_widget(self):
        self.textinput1.text = ""
        self.textinput2.text = ""
        self.textinput3.text = ""
        self.textinput4.text = ""
        self.textinput5.text = ""
        self.textinput6.text = ""

    def deletar(self):
        self.limpar_widget()
    
    def listar(self):
        
        self.ani.nome = self.textinput1.text
        self.ani.categoria = self.textinput2.text
        self.ani.alimentacao = self.textinput3.text
        self.ani.id = self.textinput4.text
        self.ani.sexo = self.textinput5.text
        self.ani.peso = self.textinput6.text

        self.listagem.adc_peixe(self.ani)
        self.listagem.listar_peixe()

        self.listagem.adc_mamifero(self.ani)
        self.listagem.listar_mamifero()
    
        self.listagem.adc_ave(self.ani)
        self.listagem.listar_ave()
    
        self.listagem.adc_anfibio(self.ani)
        self.listagem.listar_anfibio()

        self.listagem.adc_reptil(self.ani)
        self.listagem.listar_reptil()
    

        self.limpar_widget()
        
    def adicionar(self):
        self.ani.nome = self.textinput1.text
        self.ani.categoria = self.textinput2.text
        self.ani.alimentacao = self.textinput3.text
        self.ani.id = self.textinput4.text
        self.ani.sexo = self.textinput5.text
        self.ani.peso = self.textinput6.text
        self.cat.adc_catalogo(self.ani)
        

class AnimalApp(App):
    def build(self):
        return animal()
        
AnimalApp().run()

