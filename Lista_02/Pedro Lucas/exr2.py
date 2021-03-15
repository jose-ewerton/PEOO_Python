nome_atleta = True

salto = []

saltos =[]

while nome_atleta == True:
    nome_atleta = input("Digite o nome do atleta: ")

    print("")
    for tic in range(5):
        saltos.append(float(input("{}: ".format("Digite a distancia do salto"))))



    print("")

    media = sum(saltos)/len(saltos)

    print("Melhor salto: ", max(saltos), " m")
    print("Pior salto: ", min(saltos), " m")
    print("Resultados:\nnome_atleta: {}\nSaltos: {}\nMédia dos saltos: {}\n".format(nome_atleta,saltos,media))