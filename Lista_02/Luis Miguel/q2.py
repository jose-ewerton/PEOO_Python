cond = 1
while cond:
    a = str(input("qual o nome do atleta?: "))
    while a > '':
        s1 = float(input("qual a distancia do primeiro salto?: "))
        s2 = float(input("qual a distancia do segundo salto?: "))
        s3 = float(input("qual a distancia do terceiro salto?: " ))
        s4 = float(input("qual a distancia do quarto salto?: "))
        s5 = float(input("qual a distancia do quinto salto?: "))


        print("resultado: ")
        print("nome do atleta: ", a)
        res = [s1, s2, s3, s4, s5]
        print("saltos: ", res)
        media = (s1 + s2 + s3 + s4 + s5) / 5
        print("media dos saltos: ", media)
        break
    cond = int(input("Deja continuar?"))