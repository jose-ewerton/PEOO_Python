from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()



class Consulta():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        root.mainloop()

    def inserir(self):
        if self.id_entry.get() == "" or self.entry_nome.get() == "" or self.medico_entry.get() == "" or self.dia_entry.get() == "" or self.horario_entry.get() == "" or self.valor_entry == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
            return
        self.listar.insert("", "end", values=(self.id_entry.get(), self.entry_nome.get(), self.medico_entry.get(), self.dia_entry.get(), self.horario_entry.get(), self.valor_entry.get()))
        self.id_entry.delete(0, END)
        self.entry_nome.delete(0, END)
        self.medico_entry.delete(0, END)
        self.dia_entry.delete(0, END)
        self.horario_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.id_entry.focus()

    def deletar(self):
        try:
            self.item_selecionado = self.listar.selection()[0]
            self.listar.delete(self.item_selecionado)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

    def tela(self):
        self.root.title('Formulário de consulta')
        self.root.configure(background= '#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True,True)

    # CRIAÇÃO DOS FRAMES (para separar itens da tela)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee', highlightbackground= '#187db2',highlightthickness= 3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#187db2',highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        #Botões
    def widgets_frame_1(self):

        self.bt_ligar = Button(self.frame_1, text="Adicionar", bd=4, bg='#187db2', fg='white', command= self.inserir)
        self.bt_ligar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_ligar = Button(self.frame_1, text= "Deletar", bd = 4, bg= '#187db2', fg= 'white', command = self.deletar)
        self.bt_ligar.place(relx=0.8,rely=0.1,relwidth=0.1, relheight=0.15)

        # CRIAÇÃO DA LABEL PARA O USUÀRIO DIGITAR
        self.lb_id = Label(self.frame_1, text='ID consulta', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_id.place(relx=0.05, rely=0.05, )
        self.id_entry = Entry(self.frame_1, bd=4, bg='white')
        self.id_entry.place(relx=0.05, rely=0.15, relwidth=0.2)

        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.entry_nome = Entry(self.frame_1, bd=4, bg='white')
        self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.2)

        self.lb_medico = Label(self.frame_1, text='Medico', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_medico.place(relx=0.05, rely=0.65, )
        self.medico_entry = Entry(self.frame_1, bd=4, bg='white')
        self.medico_entry.place(relx=0.05, rely=0.75, relwidth=0.2)

        self.lb_dia = Label(self.frame_1, text='Dia', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_dia.place(relx=0.35, rely=0.05, )
        self.dia_entry = Entry(self.frame_1, bd=4, bg='white')
        self.dia_entry.place(relx=0.35, rely=0.15, relwidth=0.2)

        self.lb_horario = Label(self.frame_1, text='Horário', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_horario.place(relx=0.35, rely=0.35, )
        self.horario_entry = Entry(self.frame_1, bd=4, bg='white')
        self.horario_entry.place(relx=0.35, rely=0.45, relwidth=0.2)

        self.lb_valor = Label(self.frame_1, text='Valor', bg='#dfe3ee', fg='#187db2', font=('arial', 9, 'bold'))
        self.lb_valor.place(relx=0.35, rely=0.65, )
        self.valor_entry = Entry(self.frame_1, bd=4, bg='white')
        self.valor_entry.place(relx=0.35, rely=0.75, relwidth=0.2)

        # Criação da Treeview
    def lista_frame_2(self):
        self.listar = ttk.Treeview(self.frame_2, height=1, column=('col1, col2, col3, col4, col5, col6'))
        self.listar.heading('#0', text='')
        self.listar.heading('#1', text='ID Consulta')
        self.listar.heading('#2', text='Nome')
        self.listar.heading('#3', text='Médico')
        self.listar.heading('#4', text='Dia')
        self.listar.heading('#5', text='Horário')
        self.listar.heading('#6', text='Valor')

        self.listar.column('#0', width=0)
        self.listar.column('#1', width=50)
        self.listar.column('#2', width=125)
        self.listar.column('#3', width=125)
        self.listar.column('#4', width=50)
        self.listar.column('#5', width=50)
        self.listar.column('#6', width=50)

        self.listar.place(relx=0.01, rely=0.1, relwidth=0.97, relheight=0.85)

Consulta()