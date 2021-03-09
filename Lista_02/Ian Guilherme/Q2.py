i = True

sal = ["Primeiro Salto","Segundo Salto","Terceiro Salto","Quarto Salto","Quinto Salto"]
toc = 0
salv =[]

while i == True:
    atl = input("Atleta: ")
    print("")
    for tic in range(5):
        salv.append(float(input("{}: ".format(sal[toc]))))
        toc += 1

    print("")

    m = sum(salv)/len(salv)

    print("Resultados:\nAtleta: {}\nSaltos: {}\nMédia dos saltos: {}\n".format(atl,salv,m))