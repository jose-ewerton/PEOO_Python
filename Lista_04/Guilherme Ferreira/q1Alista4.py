def numero(N):
    N = []
    cont = 0
    while cont == 0:
        num = float(input("numero: "))
        conti = str(input("continuar? S/N: "))
        if conti == "S":
            N.append(num)
        elif conti == "N":
            N.append(num)
            print(sum(N))
            break
numero(1)
