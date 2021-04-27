from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from agendamento import Agendamento

class MeuApp(FloatLayout):
    lbnome = ObjectProperty(None)  
    lbdata = ObjectProperty(None)  
    lbhora = ObjectProperty(None)  
    lbtipo = ObjectProperty(None) 
    lbmedico = ObjectProperty(None)  
    lbpreencher = ObjectProperty(None)  
    lbmdisp = ObjectProperty(None)  
    lbian = ObjectProperty(None)  
    lbjess = ObjectProperty(None)  
    lbnat = ObjectProperty(None) 
    lbchave = ObjectProperty(None)
    lblista = ObjectProperty(None) 
    lblista1 = ObjectProperty(None)
    lblista2 = ObjectProperty(None)
    lblistanome = ObjectProperty(None)
    lbconsultas = ObjectProperty(None)

    tinome = ObjectProperty(None)  
    tidata = ObjectProperty(None)  
    tihora = ObjectProperty(None)  
    titipo = ObjectProperty(None)  
    timedico = ObjectProperty(None)
    tichave = ObjectProperty(None)  

    btenviar = ObjectProperty(None)   

    agenda = Agendamento()
    confirm = 0

    def limpar(self,x=0):
        if x == 1:
            self.lbnome.opacity = 0
            self.lbdia.opacity = 0
            self.lbhora.opacity = 0
            self.lbtipo.opacity = 0
            self.lbmedico.opacity = 0
            self.lbpreencher.opacity = 0
            self.lbmdisp.opacity = 0
            self.lbian.opacity = 0
            self.lbjess.opacity = 0
            self.lbnat.opacity = 0
            self.lbchave.opacity = 0
            self.lblista.opacity = 0
            self.lblista1.opacity = 0
            self.lblista2.opacity = 0
            self.lblistanome.opacity = 0
            self.lbconsultas.opacity = 0

            self.tinome.opacity = 0     
            self.tidia.opacity = 0
            self.tihora.opacity = 0
            self.titipo.opacity = 0
            self.timedico.opacity = 0
            self.tichave.opacity = 0

            self.btenviar.opacity = 0
        else:
            self.lbnome.opacity = 0
            self.lbdia.opacity = 0
            self.lbhora.opacity = 0
            self.lbtipo.opacity = 0
            self.lbmedico.opacity = 0
            self.lbpreencher.opacity = 0
            self.lbmdisp.opacity = 0
            self.lbian.opacity = 0
            self.lbjess.opacity = 0
            self.lbnat.opacity = 0
            self.lbchave.opacity = 0
            self.lblista.opacity = 0
            self.lblista1.opacity = 0
            self.lblista2.opacity = 0
            self.lblistanome.opacity = 0
            self.lbconsultas.opacity = 0

            self.tinome.opacity = 0     
            self.tidia.opacity = 0
            self.tihora.opacity = 0
            self.titipo.opacity = 0
            self.timedico.opacity = 0
            self.tichave.opacity = 0

            self.btenviar.opacity = 0
            self.btenviar.text = ""

            self.tinome.text = ""   
            self.tidia.text = ""  
            self.tihora.text = ""  
            self.titipo.text = ""  
            self.timedico.text = ""  
            self.tichave.text = "" 
    
    def nova(self):
        self.limpar()
        self.confirm = 1
        self.lbnome.opacity = 1
        self.lbdia.opacity = 1
        self.lbhora.opacity = 1
        self.lbtipo.opacity = 1
        self.lbmedico.opacity = 1
        self.lbmdisp.opacity = 1
        self.lbian.opacity = 1
        self.lbjess.opacity = 1
        self.lbnat.opacity = 1

        self.tinome.opacity = 1     
        self.tidia.opacity = 1
        self.tihora.opacity = 1
        self.titipo.opacity = 1
        self.timedico.opacity = 1

        self.btenviar.opacity = 1
        self.btenviar.text = "Enviar"  

    def atualizar(self):
        self.limpar()
        self.confirm = 2
        self.lbnome.opacity = 1
        self.lbdia.opacity = 1
        self.lbhora.opacity = 1
        self.lbtipo.opacity = 1
        self.lbmedico.opacity = 1

        self.tinome.opacity = 1     
        self.tidia.opacity = 1
        self.tihora.opacity = 1
        self.titipo.opacity = 1
        self.timedico.opacity = 1

        self.btenviar.opacity = 1
        self.btenviar.text = "Enviar" 

    def deletar(self):
        self.limpar()
        self.confirm = 3
        self.lbnome.opacity = 1
        self.tinome.opacity = 1 

        self.btenviar.opacity = 1
        self.btenviar.text = "Deletar"

    def listar(self):
        self.limpar()
        self.lblista.opacity = 1
        self.lblista.text = self.agenda.listar_agendamentos()

    def tipos(self):
        self.limpar()
        self.lblista1.opacity = 1
        self.lblista2.opacity = 1
        self.lblistanome.opacity = 1
        self.lblista1.text = self.agenda.tipos_consulta(1)
        self.lblista2.text = self.agenda.tipos_consulta(2)

    def enviar(self):
        if self.confirm == 1:
            if self.tinome.text == '' or self.tidia.text == '' or self.tihora.text == '' or self.titipo.text == '' or self.timedico.text == '':
                self.lbpreencher.opacity = 1
                self.lbpreencher.text = 'Preencha todos os campos'
            else:
                self.lbpreencher.text = self.agenda.agendar_consulta(self.tinome.text,self.tidia.text,self.tihora.text,self.titipo.text,self.timedico.text)
                self.lbpreencher.opacity = 1

                if self.lbpreencher.text != f"Reserva realizada com sucesso com o(a) médico(a) {self.timedico.text.upper()}":
                    pass
                else:
                    self.tinome.text = ""   
                    self.tidia.text = ""  
                    self.tihora.text = ""  
                    self.titipo.text = ""  
                    self.timedico.text = ""

        elif self.confirm == 2:
            if self.tinome.text == '' or self.tidia.text == '' or self.tihora.text == '' or self.titipo.text == '' or self.timedico.text == '':
                self.lbpreencher.opacity = 1
                self.lbpreencher.text = 'Preencha todos os campos'
            else:
                self.lbpreencher.text = self.agenda.atualizar_agendamento(self.tinome.text,self.tidia.text,self.tihora.text,self.titipo.text,self.timedico.text)
                self.lbpreencher.opacity = 1

                if self.lbpreencher.text == f"Ops, o agendamento de {self.tinome.text} existe mas o nome do médico está errado.":
                    pass
                elif self.lbpreencher.text == "Ops, o nome do(a) medico(a) está errado!":
                    pass
                elif self.lbpreencher.text == "Ops, você digitou o nome de outro médico":
                    pass
                elif self.lbpreencher.text == f"Ops, o agendamento de {self.tinome.text} não existe":
                    pass
                elif self.lbpreencher.text == "Você tem mais de um agendamentos, para selecionar o exato digite a chave":
                    self.limpar(1)
                    self.lbpreencher.opacity = 1
                    self.lbchave.opacity = 1
                    self.tichave.opacity = 1
                    self.btenviar.opacity = 1
                    self.btenviar.text = "Enviar"
                    self.lbconsultas.opacity = 1
                    self.lbconsultas.text = self.agenda.listar_repetido(self.tinome.text)
                    if self.tichave.text == "":
                        pass
                    else:
                        self.lbpreencher.text = self.agenda.atualizar_agendamento(self.tinome.text,self.tidia.text,self.tihora.text,self.titipo.text,self.timedico.text,self.tichave.text)

                        self.tinome.text = ""   
                        self.tidia.text = ""  
                        self.tihora.text = ""  
                        self.titipo.text = ""  
                        self.timedico.text = ""
                        self.tichave.text = ""
                else:
                    self.tinome.text = ""   
                    self.tidia.text = ""  
                    self.tihora.text = ""  
                    self.titipo.text = ""  
                    self.timedico.text = ""

        elif self.confirm == 3:
            if self.tinome.text == '':
                self.lbpreencher.opacity = 1
                self.lbpreencher.text = 'Preencha o campo da chave'
            else:
                self.lbpreencher.text = self.agenda.deletar_agendamento(self.tinome.text)
                self.lbpreencher.opacity = 1

                if self.lbpreencher.text == f"Ops, o agendamento de {self.tinome.text} não existe":
                    pass
                elif self.lbpreencher.text == "Você tem mais de um agendamentos, para selecionar o exato digite a chave":
                    self.limpar(1)
                    self.lbpreencher.opacity = 1
                    self.lbchave.opacity = 1
                    self.tichave.opacity = 1
                    self.btenviar.opacity = 1
                    self.btenviar.text = "Deletar"
                    self.lbconsultas.opacity = 1
                    self.lbconsultas.text = self.agenda.listar_repetido(self.tinome.text)
                    if self.tichave.text == "":
                        pass
                    else:
                        self.lbpreencher.text = self.agenda.deletar_agendamento(self.tinome.text,self.tichave.text)

                        self.tinome.text = ""   
                        self.tichave.text = ""
                else:
                    self.tinome.text = ""    


class main(App):
    def build (self):
        return MeuApp()

main().run()