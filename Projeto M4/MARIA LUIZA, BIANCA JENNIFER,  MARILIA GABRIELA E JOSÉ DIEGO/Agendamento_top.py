import PySimpleGUI as sg
import collections

pacientes = {}


# JANELAS

def janela_login():
    sg.theme('Reddit')
    Layout = [
        [sg.Text('Usuário:', size=(6, 1)), sg.Input(key='usuario', size=(29, 1))],
        [sg.Text('Senha:', size=(6, 1)), sg.Input(key='senha', password_char='*', size=(29, 1))],
        [sg.Text('', size=(17, 1)), sg.Button('Entrar', size=(14, 1))]

    ]
    return sg.Window('Login', layout=Layout, finalize=True)


def janela_principal():
    sg.theme('Reddit')
    Layout = [
        [sg.Text('Nome do Paciente:'), sg.Input(key='paciente')],
        [sg.Button('Buscar')],
        [sg.Text('')],
        [sg.Button('Adicionar', size=(20, 1)), sg.Button('Remover', size=(20, 1))],
        [sg.Button('Atualizar', size=(20, 1)), sg.Button('Exibir Dados', size=(20, 1))],
        [sg.Text('')],
        [sg.Button('Sair', size=(6, 1))]
    ]
    return sg.Window('Agendamento de Consultas', layout=Layout, finalize=True)


def janela_adicionar():
    sg.theme('Reddit')
    Layout = [
        [sg.Text('Nome do Paciente:', size=(15, 1)), sg.Input(key='paciente', size=(30, 1))],
        [sg.Text('Horário:', size=(15, 1)), sg.Input(key='horario', size=(30, 1))],
        [sg.Text('Médico(a):', size=(15, 1)), sg.Input(key='medico', size=(30, 1))],
        [sg.Text('Valor da Consulta', size=(15, 1)), sg.Input(key='valor', size=(30, 1))],
        [sg.Button('Adicionar', size=(15, 1)), sg.Button('Voltar')]
    ]
    return sg.Window('Adicionar', layout=Layout, finalize=True)


def janela_remover():
    Layout = [
        [sg.Text('Nome do Paciente'), sg.Input(key='paciente')],
        [sg.Button('Remover'), sg.Button('Voltar')]
    ]
    return sg.Window('Remover', layout=Layout, finalize=True)


def janela_atualizar():
    Layout = [
        [sg.Text('Nome do Paciente:', size=(15, 1)), sg.Input(key='paciente')],
        [sg.Button('Verificar')],
        [sg.Text('Novo Nome:', size=(10, 1)), sg.Input(key='nome', size=(15, 1))],
        [sg.Text('Novo Horário:', size=(10, 1)), sg.Input(key='horario', size=(15, 1))],
        [sg.Text('Novo Médico:', size=(10, 1)), sg.Input(key='medico', size=(15, 1))],
        [sg.Text('Novo Valor:', size=(10, 1)), sg.Input(key='valor', size=(15, 1))],
        [sg.Button('Atualizar', size=(10, 1)), sg.Button('Voltar')]
    ]
    return sg.Window('Atualizar', layout=Layout, finalize=True)


def janela_exibir():
    dic_hora = {}
    dados_guardados = []

    for chave, dados in pacientes.items():
        for pos, infor in dados.items():
            dados_guardados.append(infor)
            if pos == "Horario":
                chave_nova = None
                chave_nova = infor.replace(":", "0")
                chave_nova = int(chave_nova)

        dic_hora[chave_nova] = {"Paciente": dados_guardados[0], "Horario": dados_guardados[1],
                                "Medico": dados_guardados[2], "Valor": dados_guardados[3]}
        dados_guardados.clear()
    dic_hora = collections.OrderedDict(sorted(dic_hora.items()))
    dic_hora = dict(dic_hora)

    dic_final = {}
    dados_finais = []
    n = "Nome:"
    h = "Horario:"
    me = "Medico:"
    va = "Valor:"

    div_nome = []
    div_hora = []
    div_medico = []
    div_valor = []
    for lugar, di in dic_hora.items():
        for po, valores in di.items():
            dados_finais.append(valores)
            if po == "Paciente":
                chave_final = None
                chave_final = valores
        dic_final[chave_final] = {"Paciente": dados_finais[0], "Horario": dados_finais[1],
                                  "Medico": dados_finais[2], "Valor": dados_finais[3]}
        dados_finais.clear()
    for name, da in dic_final.items():
        div_nome.append(name)
        for ch, inf in da.items():
            if ch == "Horario":
                div_hora.append(inf)

            elif ch == "Medico":
                div_medico.append(inf)

            else:
                if ch == "Valor":
                    div_valor.append(inf)

    Layout = [
        [sg.Text(n, size=(6, 1)), sg.Text(div_nome)],
        [sg.Text(h, size=(6, 1)), sg.Text(div_hora, size=(20, 1))],
        [sg.Text(me, size=(6, 1)), sg.Text(div_medico, size=(20, 1))],
        [sg.Text(va, size=(6, 1)), sg.Text(div_valor, size=(20, 1))],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Atualizar', layout=Layout, finalize=True)


def janela_buscar():
    div_nome = []
    div_hora = []
    div_medico = []
    div_valor = []
    name = values['paciente']

    if name in pacientes:
        for nome, da in pacientes.items():
            if nome == name:
                div_nome.append(nome)
                for ch, inf in da.items():
                    if ch == "Horario":
                        div_hora.append(inf)

                    elif ch == "Médico":
                        div_medico.append(inf)

                    else:
                        if ch == "Valor":
                            div_valor.append(inf)
    elif name not in pacientes:
        variavel = 'Paciente não encontrado!'

    Layout = [
        [sg.Text("Paciente:", size=(6, 1)), sg.Text(div_nome)],
        [sg.Text("Horario:", size=(6, 1)), sg.Text(div_hora, size=(20, 1))],
        [sg.Text("Médico:", size=(6, 1)), sg.Text(div_medico, size=(20, 1))],
        [sg.Text("Valor:", size=(6, 1)), sg.Text(div_valor, size=(20, 1))],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Buscar', layout=Layout, finalize=True)


# ============================================================================================

# DEFINIÇÃO DAS JANELAS
janela0, janela1, janela2, janela3, janela4, janela5, janela6, janela7 = janela_login(), None, None, None, None, None, None, None

# ============================================================================================

# LOOP DE EVENTOS
while True:
    window, event, values = sg.read_all_windows()

    # ============================================================================================

    # JANELA LOGIN

    if window == janela0 and event == 'Entrar':
        if values['usuario'] == 'IFRN' and values['senha'] == '1234':
            janela1 = janela_principal()
            janela0.hide()
        else:
            sg.popup('Usuário ou senha incorretos!')

    # Quando a janela for fechada
    if window == janela0 and event == sg.WINDOW_CLOSED:
        break

    # ============================================================================================

    # JANELA PRINCIPAL

    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    if window == janela1 and event == 'Sair':
        janela1.hide()
        janela0.un_hide()

    # BUSCAR

    if window == janela1 and event == 'Buscar':
        janela7 = janela_buscar()

    if window == janela7 and event == 'Voltar':
        janela7.hide()

    # BOTÃO ADICIONAR
    if window == janela1 and event == 'Adicionar':
        janela2 = janela_adicionar()
        janela1.hide()

    # BOTÃO REMOVER
    if window == janela1 and event == 'Remover':
        janela3 = janela_remover()
        janela1.hide()

    # BOTÃO ATUALIZAR
    if window == janela1 and event == 'Atualizar':
        janela4 = janela_atualizar()
        janela1.hide()

    # BOTÃO EXIBIR DADOS
    if window == janela1 and event == 'Exibir Dados':
        janela6 = janela_exibir()

    if window == janela6 and event == 'Voltar':
        janela6.hide()
        janela1.un_hide()

    # ============================================================================================

    # JANELA ADICIONAR

    # BOTÃO VOLTAR
    if window == janela2 and event == 'Voltar':
        janela1.un_hide()
        janela2.hide()


    # FUNCÃO PARA ADICIONAR PACIENTE
    def adicionar_consulta():
        nome = values['paciente']
        hora = values['horario']
        medicu = values['medico']
        preço = values['valor']
        verificar = 0

        for name, dados in pacientes.items():
            for dado, infor in dados.items():
                if dado == "Horario":
                    if hora == infor:
                        sg.popup("Não pode ser adicionado, pois o horário está indisponível")
                        verificar = 1

        if verificar == 0:
            pacientes[nome] = {"Paciente": nome, "Horario": hora, "Médico": medicu, "Valor": preço}
            sg.popup('Adicionado')


    # BOTÃO ADICIONAR NA JANELA 'ADICIONAR'
    if window == janela2 and event == 'Adicionar':
        adicionar_consulta()

    # ============================================================================================

    # JANELA REMOVER

    # BOTÃO VOLTAR
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()


    # FUNÇÃO PRA REMOVER PACIENTE
    def eliminar():
        nome = values['paciente']
        if nome in pacientes:
            del pacientes[nome]
            sg.popup('Removido')

        elif nome not in pacientes:
            sg.popup("Não encontrado!")


    # BOTÃO REMOVER NA JANELA 'REMOVER'
    if window == janela3 and event == 'Remover':
        eliminar()

    # ============================================================================================

    # JANELA ATUALIZAR

    # BOTÃO VOLTAR
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()


    # FUNÇÃO PRA VERIFICAR SE O PACIENTE JÁ EXISTE OU NÃO
    def verificado():
        name = values['paciente']
        if name in pacientes:
            sg.popup('Paciente encontrado! Você pode atualizar suas informações.')

        elif name not in pacientes:
            sg.popup('Paciente não encontrado!')


    # BOTÃO VERIFICAR
    if window == janela4 and event == 'Verificar':
        verificado()


    # FUNÇÃO PARA ATUALIZAR OS DADOS DO PACIENTE
    def novo_usuario():
        nome_antigo = values['paciente']

        nome = values['nome']
        hora = values['horario']
        medicu = values['medico']
        preço = values['valor']

        verificar = 0

        for name, dados in pacientes.items():
            for dado, infor in dados.items():
                if dado == "Horario":
                    if hora == infor:
                        sg.popup("Não pode ser atualizado, pois o horário está indisponível")
                        verificar = 1

        if verificar == 0:
            del pacientes[nome_antigo]
            pacientes[nome] = {"Paciente": nome, "Horario": hora, "Médico": medicu, "Valor": preço}
            sg.popup('Atualizado')


    # BOTÃO ATUALIZAR NA JANELA 'ATUALIZAR'
    if window == janela4 and event == 'Atualizar':
        novo_usuario()

    # ============================================================================================

    # JANELA EXIBIR DADOS

    # BOTÃO VOLTAR
    if window == janela5 and event == 'Voltar':
        janela1.un_hide()
        janela5.hide()


    # FUNÇÃO PARA MOSTRAR POR ORDEM DE ATENDIMENTO
    def mostrar():
        dic_hora = {}
        dados_guardados = []

        for chave, dados in pacientes.items():
            for pos, infor in dados.items():
                dados_guardados.append(infor)
                if pos == "Horario":
                    chave_nova = None
                    chave_nova = infor.replace(":", "0")
                    chave_nova = int(chave_nova)

            dic_hora[chave_nova] = {"Paciente": dados_guardados[0], "Horario": dados_guardados[1],
                                    "Medico": dados_guardados[2], "Valor": dados_guardados[3]}
            dados_guardados.clear()
        dic_hora = collections.OrderedDict(sorted(dic_hora.items()))
        dic_hora = dict(dic_hora)

        dic_final = {}
        dados_finais = []

        for lugar, di in dic_hora.items():
            for po, valores in di.items():
                dados_finais.append(valores)
                if po == "Paciente":
                    chave_final = None
                    chave_final = valores
            dic_final[chave_final] = {"Paciente": dados_finais[0], "Horario": dados_finais[1],
                                      "Medico": dados_finais[2], "valor": dados_finais[3]}
            dados_finais.clear()

        sg.popup(dic_final)
