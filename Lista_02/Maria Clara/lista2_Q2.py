print('Para responder: 1 = Sim e 0 = Não:')
perguntas = ["Telefonou para a vítima? ",
                   "Esteve no local do crime? ",
                   "Mora perto da vítima? ",
                   "Devia para a vítima? ",
                   "Já trabalhou com a vítima? "]
res = []
respostas = 0
for c in range(len(perguntas)):
    print(perguntas[c])
    res.append(input())
    respostas += int(res[c])

status = ["Suspeito(a)","Cúmplice","Inocente","Assassino"]
if respostas == 2:
    print(status[0])
elif 3 <= respostas <= 4:
    print(status[1])
elif respostas <= 1:
    print(status[2])
elif respostas == 5:
    print(status[3])
