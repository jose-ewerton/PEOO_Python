sla = 1

while sla == 1:  
    atleta = input("Atleta: ")

    s1 = float(input("Primeiro salto: "))
    s2 = float(input("Segundo salto: "))
    s3 = float(input("Terceiro salto: "))
    s4 = float(input("Quarto salto: "))
    s5 = float(input("Quinto salto: "))

    m = (s1 + s2 + s3 + s4 + s5)/5 

    print("Resultado:")
    print("Atleta: %s" % atleta)
    print("Saltos: %.1f - %.1f - %.1f - %.1f - %.1f" % (s1, s2, s3, s4, s5))
    print("Média: %.1f" % m)