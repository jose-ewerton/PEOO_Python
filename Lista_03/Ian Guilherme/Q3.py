def func(x):
    if x >= 12:
        P = x-12
        return P
    else:
        A = x
        return A
        
def func2():
    while True:
        x = int(input("Digite a hora: "))
        y = int(input("Digite os minutos: "))
        if x >= 12:
            print("A hora convertida é {}:{} P.M.".format(func(x),y))
        else:
            print("A hora converdita é {}:{} A.M.".format(func(x),y))
        
        z = input("Quer continuar (S/N)? ")
        if z == "N":
            break

func2()