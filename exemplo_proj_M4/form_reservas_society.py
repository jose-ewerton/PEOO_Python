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
    btn1 = ObjectProperty(None)
    lista = ObjectProperty(None)

    reservas = Reserva()
    confirm = 0

    def limpar_widget(self):
        self.lista.opacity = 0 
        self.label1.opacity = 0 
        self.label2.opacity = 0
        self.label3.opacity = 0
        self.label4.opacity = 0
        self.textinput1.opacity = 0
        self.textinput2.opacity = 0
        self.textinput3.opacity = 0
        self.textinput4.opacity = 0 
        self.label5.opacity = 0
        self.btn1.opacity = 0
        self.textinput1.text = ""
        self.textinput2.text = ""
        self.textinput3.text = ""
        self.textinput4.text = ""

    def inserir(self):
        self.limpar_widget()
        #construindo o formulário de adicionar reserva
        self.label2.opacity = 1
        self.label3.opacity = 1
        self.label4.opacity = 1
        self.textinput2.opacity = 1
        self.textinput3.opacity = 1
        self.textinput4.opacity = 1  
        self.label5.opacity = 1
        self.btn1.opacity = 1 
        self.btn1.text = "Enviar"
        self.label5.text = 'Preencha todos os campos'
        self.confirm = 1    

    def listar(self):
        self.limpar_widget() 
        self.lista.opacity = 1
        self.lista.text = self.reservas.listar_reservas()
    
    def deletar(self):
        self.limpar_widget()
        self.label1.opacity = 1
        self.textinput1.opacity = 1 
        self.btn1.text = 'Excluir' 
        self.btn1.opacity = 1
        self.confirm = 2

    def atualizar(self):
        self.limpar_widget()
        self.label1.opacity = 1
        self.textinput1.opacity = 1 
        self.btn1.text = 'Confirmar'
        self.btn1.opacity = 1
        self.confirm = 3

    def executar_tarefa(self):
        if (self.confirm == 1):
            if (self.textinput2.text == "" or self.textinput3.text == "" or self.textinput4.text == ""):
                self.label5.text = 'Preencha todos os campos'
            else:
                self.label5.text = self.reservas.adicionar_reserva(self.textinput2.text,self.textinput3.text,self.textinput4.text)
                self.textinput2.text = ""
                self.textinput3.text = ""
                self.textinput4.text = ""
        elif (self.confirm == 2):
            if (self.textinput1.text == ""):
                self.label5.opacity = 1
                self.label5.text = 'Preencha o campo com a chave que deseja deletar'
            else:
                print('teste deletar')
                self.label5.text = self.reservas.deletar_reserva(self.textinput1.text)
                self.label5.opacity = 1
                self.textinput1.text = ""
        elif (self.confirm == 3):
            self.label5.opacity = 1
            if (self.textinput1.text == ""):
                self.label5.text = 'Preencha o campo com a chave correta que deseja atualizar' 
            else:         
                r = self.reservas.retornar_reserva(self.textinput1.text)
                if (type(r) == str):
                    self.label5.text = r
                else:
                    self.label2.opacity = 1
                    self.label3.opacity = 1
                    self.label4.opacity = 1
                    self.textinput2.opacity = 1
                    self.textinput3.opacity = 1
                    self.textinput4.opacity = 1 
                    '''
                    self.textinput2.text = r.dia
                    self.textinput3.text = r.horario
                    self.textinput4.text = r.valor
                    '''
                    self.label5.text = self.reservas.atualizar_reserva(chave = self.textinput1.text, dia = self.textinput2.text, horario = self.textinput3.text , valor = self.textinput4.text)


class painelApp(App):
    def build(self):
        return Painel()          
painelApp().run()