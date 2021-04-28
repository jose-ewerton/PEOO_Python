#valor inicial
lista = []

print("QUESTIONÁRIO SOBRE UM ASSASSINATO")

#código principal
a = str(input("Telefonou para a vítima? (Sim ou Não): ")).lower()
if 's' in a:
    lista.append(a)
b = str(input("Esteve no local do crime? (Sim ou Não): ")).lower()
if 's' in b:
    lista.append(b)
c = str(input("Mora perto da vítima? (Sim ou Não): ")).lower()
if 's' in c:
    lista.append(c)
d = str(input("Devia para a vítima? (Sim ou Não): ")).lower()
if 's' in d:
    lista.append(d)
e = str(input("Já trabalhou com a vítima? (Sim ou Não): ")).lower()
if 's' in e:
    lista.append(e)


#saída
if len(lista) == 2:
    print("Resultado:Suspeito(a)")
elif len(lista) == 3:
    print("Resultado:Cúmplice")
elif len(lista) == 4:
    print("Resultado:Cúmplice")
elif len(lista) == 5:
    print("Resultado:Assassino!")
else:
    print("Resultado:Inocente!")
