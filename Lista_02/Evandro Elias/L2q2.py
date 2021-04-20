n = str(input("Nome do atleta: "))
while n > '':
    g1 = float(input("Distancia do primeiro salto: "))
    g2 = float(input("Distancia do segundo salto?: "))
    g3 = float(input("Distancia do terceiro salto?:" ))
    g4 = float(input("Distancia do quarto salto?: "))
    g5 = float(input("Distancia do quinto salto"))
    print("-----------------------------------------------------------------------")

    print("Atleta: ",n)
    print("Primeiro salto:",g1)
    print("Segundo salto:",g2)
    print("Terceiro salto:",g3)
    print("Quarto salto:",g4)
    print("Quinto salto:",g5)
    print("--------------RESULTADO------------------")
    print("atleta: ", n)
    resultado = [g1,  g2, g3,  g4, g5]
    print("saltos: ", resultado)
    M = (g1 + g2 + g3 + g4 + g5) / 5
    print("media dos saltos: ", M)
    break
