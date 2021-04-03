media = []
nome = str(input("nome do atleta: "))
p1 = float(input("primeiro salto: "))
media.append(p1)
p2 = float(input("segundo salto: "))
media.append(p2)
p3 = float(input("terceiro salto: "))
media.append(p3)
p4 = float(input("quarto salto: "))
media.append(p4)
p5 = float(input("quinto salto: "))
media.append(p5)

media2 = sum(media)/5
print("Resultado:")
print("Atleta: {}" .format(nome))
print("saltos:", p1, p2, p3, p4, p5)
print("media: ", media2)