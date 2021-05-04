contador = 0

pergunta1 = str(input("Telefonou para a vítima? (S ou N): ")).lower()
if pergunta1 in 's':
    contador += 1
pergunta2 = str(input("esteve no local do crime? (S ou N): ")).lower()
if pergunta2 in 's':
    contador += 1
pergunta3 = str(input("mora perto da vítima? (S ou N): ")).lower()
if pergunta3 in 's':
    contador += 1
pergunta4 = str(input("devia para a vítima? (S ou N): ")).lower()
if pergunta4 in 's':
    contador += 1
pergunta5 = str(input("já trabalhou com a vítima? (S ou N): ")).lower()
if pergunta5 in 's':
    contador += 1

if contador == 2:
    print("Suspeito(a)")

elif contador == 3 or contador == 4:
    print("Cúmplice")

elif contador == 5:
    print("Assassino!")

else:
    print("Inocente!")