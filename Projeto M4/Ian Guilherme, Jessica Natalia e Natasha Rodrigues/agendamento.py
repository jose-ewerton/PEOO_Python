class Agendamento:
    def __init__(self,nome=None,dia=None,hora=None,tipo_consulta=None,medico=None):
        self.nome = nome
        self.dia = dia
        self.hora = hora
        self.tipo_consulta = tipo_consulta
        self.medico = medico
        self.lista_reserva = []
        self.lista_reservai = []
        self.lista_reservaj = []
        self.lista_reservan = []
        self.repet = 0

    def agendar_consulta(self,nome,dia,hora,tipo_consulta,medico):
        x = medico.upper()
        lmed = ["IAN","JESSICA","NATASHA"]
        lcont = 0
        lreser = [self.lista_reservai,self.lista_reservaj,self.lista_reservan]
        soma = 0

        while lcont <= 2:
            if x == lmed[lcont]:
                if len(lreser[lcont]) != 0:
                    for cont1 in lreser[lcont]:
                        if cont1.dia == dia and cont1.hora == hora:
                            return f"Dia e horário indisponivel com o(a) médico(a) {lmed[lcont]}"
                        else:
                            soma += 1
                    if soma == len(lreser[lcont]):
                        self.lista_reserva.append(Agendamento(nome,dia,hora,tipo_consulta,medico))
                        lreser[lcont].append(Agendamento(nome,dia,hora,tipo_consulta,medico))
                        print(nome,dia,hora,tipo_consulta,medico)
                        return f"Reserva realizada com sucesso com o(a) médico(a) {lmed[lcont]}"
                else:
                    self.lista_reserva.append(Agendamento(nome,dia,hora,tipo_consulta,medico))
                    lreser[lcont].append(Agendamento(nome,dia,hora,tipo_consulta,medico))
                    print(nome,dia,hora,tipo_consulta,medico)
                    return f"Reserva realizada com sucesso com o(a) médico(a) {lmed[lcont]}"
            else:
                lcont += 1 
        
        if lcont == 3:
            return "Ops, o nome do(a) médico(a) está errado!"       
    
    def listar_agendamentos(self):
        if len(self.lista_reserva) != 0:
            j = ""
            for i in self.lista_reserva:
                j += f'Nome: {i.nome}, Dia: {i.dia}, Horario: {i.hora}, Tipo de Consulta: {i.tipo_consulta}, Médico(a): {i.medico}\n'
            return j
        else:
            return 'Lista de reservas vazia!'

    def atualizar_agendamento(self,nome,dia,hora,tipo_consulta,medico,chave=9999999999):
        x = medico.upper()
        especial = 0
        especial1 = 0
        tatata = 0
        lmed = ["IAN","JESSICA","NATASHA"]
        lcont = 0
        lreser = [self.lista_reservai,self.lista_reservaj,self.lista_reservan]

        while lcont <= 2:
            if x == lmed[lcont]:
                for contar in self.lista_reserva:
                    if contar.nome == nome and contar.medico == medico:
                        for cont in self.lista_reserva:
                            if cont.nome == nome:
                                especial += 1
                            if especial == int(chave) and cont.medico == medico:
                                cont.dia = dia
                                cont.hora = hora
                                cont.tipo_consulta = tipo_consulta
                                for cont2 in lreser[lcont]:
                                    if cont2.nome == nome:
                                        especial1 += 1
                                    if especial1 == int(chave):
                                        cont2.dia = dia
                                        cont2.hora = hora
                                        cont2.tipo_consulta = tipo_consulta
                                return f"Agendamento de {nome} com o(a) médico(a) {cont2.medico} atualizado!"
                            if especial == int(chave) and cont.medico != medico:
                                return "Ops, você digitou o nome de outro médico"
                    else:
                        tatata += 1
                if tatata == len(self.lista_reserva):
                    for zaa in self.lista_reserva:
                        if zaa.nome == nome and zaa.medico != medico:
                            return f"Ops, o agendamento de {nome} existe mas o nome do médico está errado."
                        if zaa.nome != nome and zaa.medico == medico:
                            return f"Ops, o agendamento de {nome} não existe"

                if especial > 1:
                    return "Você tem mais de um agendamentos, para selecionar o exato digite a chave"
                else:
                    for cont in self.lista_reserva:
                        y = cont.medico.upper()
                        if cont.nome == nome and y == x:
                            cont.dia = dia
                            cont.hora = hora
                            cont.tipo_consulta = tipo_consulta
                    for cont2 in lreser[lcont]:
                        if cont2.nome == nome:
                            cont2.dia = dia
                            cont2.hora = hora
                            cont2.tipo_consulta = tipo_consulta
                            if nome == cont2.nome:
                                return f"Agendamento de {nome} com o(a) médico(a) {cont2.medico} atualizado!"   
            else:
                lcont += 1

        if lcont == 3:
            return "Ops, o nome do(a) medico(a) está errado!"

    def listar_repetido(self,nome):
        self.repet = 0
        replista = ''
        for i in self.lista_reserva:
            if i.nome == nome:
                self.repet += 1
                replista += f'Nome: {i.nome}, Dia: {i.dia}, Horario: {i.hora}, Tipo de Consulta: {i.tipo_consulta}, Médico(a): {i.medico}\n'

        if self.repet > 1:
            return replista

    def deletar_agendamento(self,nome,chave=9999999999):
        especial = 0
        especial1 = 0
        lmed = ["IAN","JESSICA","NATASHA"]
        lcont = 0
        lreser = [self.lista_reservai,self.lista_reservaj,self.lista_reservan]

        for cont in self.lista_reserva:
            if cont.nome == nome:
                especial += 1
            if especial == int(chave):
                x = cont.medico.upper()
                for z in range(3):
                    if x == lmed[lcont]:
                        break
                    else:
                        lcont += 1
                t = f"Agendamento de {cont.nome} com o(a) médico(a) {cont.medico} removido!"
                self.lista_reserva.remove(cont)
                for cont2 in lreser[lcont]:
                    if cont2.nome == nome:
                        especial1 += 1
                    if especial1 == int(chave):
                        lreser[lcont].remove(cont2)
                return t
        if especial > 1:
            return "Você tem mais de um agendamentos, para selecionar o exato digite a chave"
        else:
            for cont3 in self.lista_reserva:
                if cont3.nome == nome:
                    x = cont3.medico.upper()
                    for z in range(3):
                        if x == lmed[lcont]:
                            break
                        else:
                            lcont += 1
                    t = f"Agendamento de {cont3.nome} com o(a) médico(a) {cont3.medico} removido!"
                    self.lista_reserva.remove(cont3)
            for cont4 in lreser[lcont]:
                if cont4.nome == nome:
                    lreser[lcont].remove(cont4)
        if nome == cont3.nome:
            return t
        else:
            return f"Ops, o agendamento de {nome} não existe" 

    def tipos_consulta(self,x=0):
        tipos = ['1 - Clareamento dental','2 - Manutenção de aparelho', '3 - Tratamento de canal', '4 - Extração dentária', '5 - Limpeza', '6 - Restauração dental', '7 - Implante dentário', '8 - Prótese dentária']
        k = ''
        c = ''
        l = 0
        while l <= 7:
            if l <= 3:
                k += f'{tipos[l]}\n'
                l += 1
            elif 3 < l <=7:
                c += f'{tipos[l]}\n'
                l += 1
        if x == 1:
            return k
        elif x == 2:
            return c

if __name__ == "__main__":
    c1 = Agendamento()
    print(c1.agendar_consulta("Ian","23","14:00","Limpeza simples","ian"))
    print(c1.listar_agendamentos())
    #print(c1.atualizar_agendamento("Ian","14","15:00","Raio-x","ian"))
    print(c1.listar_agendamentos())
    
    print(c1.agendar_consulta("Felipe","15","15:00","raio-x","ian"))
    #print(c1.agendar_consulta("Felipe","14","16:00","fezes","jessica"))
    print(c1.atualizar_agendamento('Felipe','12','18:00','txu',"ian"))
    print(c1.atualizar_agendamento("Ian","14","15:00","Raio-x","ian"))
    print(c1.listar_agendamentos())
    '''
    print(c1.agendar_consulta("Tião","15","15:00","raio-x","natasha"))
    print(c1.listar_agendamentos())
    print(c1.deletar_agendamento("Felipe",2))
    print(c1.listar_agendamentos())
    '''