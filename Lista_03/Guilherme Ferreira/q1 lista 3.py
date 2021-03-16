def numero(*args):
    N = []
    N += args
    cont = 0
    while cont < 1:
        
        N.append(float(input("digite um numero: ")))
        continuar = str(input("continuar? S/N: "))
        if continuar == "S":
            cont = 0
        else:
            cont = 1
            
    print(sum(N))
numero(0)
