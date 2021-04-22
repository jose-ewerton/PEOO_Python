class Reserva:
    def __init__(self, chave=0,dia=None, horario=None,valor=None):
        self.chave = chave
        self.dia = dia
        self.horario = horario
        self.valor = valor
        self.lista_reservas =[]
    
    def adicionar_reserva(self,dia, horario,valor):
        self.chave += 1
        #verificar s eo horario está disponivel naquele dia
        self.lista_reservas.append(Reserva(self.chave,dia,horario,valor))
        print(self.chave,dia,horario,valor)
        return f'Reserva realizada com sucesso! Guarde sua chave de acesso {self.chave}'

    def listar_reservas(self):
        if len(self.lista_reservas) != 0:
            texto = ""
            for item in self.lista_reservas:
                print(item.chave,item.dia,item.horario,item.valor)
                texto += f' Chave: {item.chave}, Dia: {item.dia}, Horario: {item.horario}, Valor: {item.valor}\n'
            return texto 
        else:
            return 'Lista de reservas vazia!'

    def deletar_reserva(self,cod):
        cond = 0
        for reserva in self.lista_reservas:
            if (int(cod) == reserva.chave):
                cond = 1
                texto = f'Removendo a reserva {reserva.chave}, {reserva.dia}, {reserva.horario}, {reserva.valor}'
                self.lista_reservas.remove(reserva)
                return texto
        if  not cond:
            return f'Reserva {cod} não existe!'
    
    def retornar_reserva(self,cod):
        res = 0
        for item in self.lista_reservas:
            if (int(cod) == item.chave):
                res = item
        if res == 0:
            return "Chave não encontrada"
        else:
            return res

    def atualizar_reserva(self,**kwargs):
        cod = 0
        for variavel,atributo in kwargs.items():
            if (variavel == 'chave'):
                cod = int(atributo)
                break

        for item in self.lista_reservas:
            if (item.chave == cod):
                for variavel,atributo in kwargs.items():
                    if (variavel == 'dia'):
                        item.dia = atributo 
                        for variavel,atributo in kwargs.items():
                            print("Print aqui",variavel,atributo)
                    if (variavel == 'horario'):
                        item.horario = atributo 
                    if (variavel == 'valor'):
                        item.valor = atributo
                self.lista_reservas.insert(item.chave,item)
                self.lista_reservas.remove(item)
                return f'Atualizados os dados de chave {item.chave}'
           
if (__name__ == '__main__'):
    r = Reserva()
    print(r.adicionar_reserva('Quinta','12:00', 'R$ 30,00'))
    print(r.adicionar_reserva('Sexta','10:00', 'R$ 30,00'))
    print(r.adicionar_reserva('Sábado','11:00', 'R$ 30,00'))
    #r.listar_reservas()
    #r.deletar_reserva(2)
    r.listar_reservas()
    r.atualizar_reserva(chave = 2,dia = 'Segunda',horario = '19:00', valor = 'R$ 60,00')
    r.listar_reservas()
    r.atualizar_reserva(chave = 9,dia = 'Terça',horario = '19:00', valor = 'R$ 60,00')
    r.listar_reservas()
    #r.listar_reservas()


