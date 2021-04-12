i = 1

while i == 1:  
    atleta = input("Informe o nome do atleta: ")

    ps = float(input("Primeiro salto: "))
    ss = float(input("Segundo salto: "))
    ts = float(input("Terceiro salto: "))
    quas = float(input("Quarto salto: "))
    quis = float(input("Quinto salto: "))

    m = (ps + ss + ts + quas + quis)/5 

    print("-"*35)
    print("Resultado:")
    print("Atleta: %s" % atleta)
    print("Saltos: %.1f - %.1f - %.1f - %.1f - %.1f" % (ps, ss, ts, quas, quis))
    print("Média: %.1f" % m)
    print("-"*35)
